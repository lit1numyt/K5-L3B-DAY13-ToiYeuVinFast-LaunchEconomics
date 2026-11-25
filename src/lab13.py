"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP1: mô hình chi phí theo docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md.
# CP2 có thể gọi lại với tham số khác.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()

    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def chi_phi_theo_loai(runs, reqs):
    """A3: tính chi phí và tỉ lệ thành công cuối cùng cho từng loại yêu cầu."""
    ket_qua = []
    for loai, nhom in reqs.groupby('loai', sort=False):
        mo_hinh_nhom = mo_hinh(runs, nhom)
        so_yeu_cau = len(nhom)
        so_lan_chay = runs['request_id'].isin(nhom['request_id']).sum()
        ket_qua.append({
            'loai': loai,
            'so_yeu_cau': so_yeu_cau,
            'ti_le_thanh_cong': mo_hinh_nhom['thanh_cong'] / so_yeu_cau,
            'lan_chay_moi_yeu_cau': so_lan_chay / so_yeu_cau,
            'chi_phi_moi_viec': mo_hinh_nhom['cps'],
            'so_voi_baseline': mo_hinh_nhom['cps'] / BASELINE,
        })
    return ket_qua


def bang_do_nhay(runs, reqs):
    """Tính B1 và B2 bằng cách đổi tham số của mô hình A2."""
    kich_ban = {
        'Token gap doi': dict(gia_vao=52, gia_ra=260),
        'Token giam nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi': dict(he_so_xem_lai=2),
        'Xem lai giam nua': dict(he_so_xem_lai=0.5),
        'Lam lai gap doi': dict(he_so_lam_lai=2),
        'Lam lai giam nua': dict(he_so_lam_lai=0.5),
        'Luong tang 25%': dict(luong_phut=2500),
        'Toi da 2 lan chay': dict(max_lan_chay=2),
        'Toi da 1 lan chay': dict(max_lan_chay=1),
        'Token va xem lai gap doi': dict(gia_vao=52, gia_ra=260, he_so_xem_lai=2),
    }
    goc = mo_hinh(runs, reqs)['cps']
    return {ten: (cps, (cps / goc - 1) * 100)
            for ten, tham_so in kich_ban.items()
            for cps in [mo_hinh(runs, reqs, **tham_so)['cps']]}


def xem_lai_tat_ca(runs, reqs, phut_lam_lai=9):
    """B4: xem lại 5 phút mỗi yêu cầu có ít nhất một lần chạy ok."""
    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])].copy()
    co_ok = runs.loc[runs['status'] == 'ok', 'request_id']
    pham_vi['phut_xem_lai_simulated'] = pham_vi['request_id'].isin(co_ok).astype(int) * 5
    pham_vi['phut_lam_lai_simulated'] = (pham_vi['ket_qua'] == 'lam_lai').astype(int) * phut_lam_lai
    return mo_hinh(runs, pham_vi)


# ---------- Nhiệm vụ D1 · Cỡ mẫu pilot ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (công thức trong docs/du_lieu_va_cong_thuc.md)."""
    from statistics import NormalDist
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def he_so_thiet_ke(m, icc=0.02):
    """DE = 1 + (m − 1) × ICC, m là số yêu cầu mỗi cụm."""
    return 1 + (m - 1) * icc


def m_toi_thieu(n_can, so_cum, icc=0.02):
    """Số yêu cầu tối thiểu mỗi cụm để c·m / DE ≥ n_can; None nếu không thể (n_can ≥ c / ICC)."""
    mau = so_cum - n_can * icc
    return None if mau <= 0 else math.ceil(n_can * (1 - icc) / mau)


def bang_co_mau(baseline=0.70, muc_tieu=0.05, icc=0.02):
    """Năm câu D1."""
    n = co_mau(baseline, baseline + muc_tieu)
    de_b = he_so_thiet_ke(75, icc)
    n6 = co_mau(baseline, baseline + 0.06)
    m_e = m_toi_thieu(n6, 20, icc)
    return dict(
        a_theo_yeu_cau=n,
        b_de=de_b, b_n=math.ceil(n * de_b), b_nguoi_moi_nhom=math.ceil(n * de_b / 75),
        c_toi_da_20_nguoi=20 / icc,
        d_toi_da_6_depot=6 / icc,
        e_n_6_diem=n6, e_m=m_e, e_de=he_so_thiet_ke(m_e, icc),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        nhan = ' [simulated]' if ten in ('xem_lai', 'lam_lai', 'tong', 'cps') else ''
        so_chu_so = 1 if ten == 'hoa_don_moi_yc' else 0
        print(f'{ten:14s} {gia_tri:>14,.{so_chu_so}f}{nhan}')
    print('\nA3: theo loai yeu cau; chi phi va so voi baseline [simulated]')
    print(f"{'Loai':12s} {'Yeu cau':>8s} {'Thanh cong':>11s} {'Lan chay/YC':>12s} "
          f"{'Chi phi/viec':>14s} {'So voi 12,000 d':>16s}")
    for dong in chi_phi_theo_loai(runs, reqs):
        print(f"{dong['loai']:12s} {dong['so_yeu_cau']:>8d} "
              f"{dong['ti_le_thanh_cong']:>10.1%} {dong['lan_chay_moi_yeu_cau']:>12.2f} "
              f"{dong['chi_phi_moi_viec']:>14,.0f} {dong['so_voi_baseline']:>15.2f}x")
    runs_quoc_te = runs[runs['request_id'].isin(reqs.loc[reqs['loai'] == 'quoc_te', 'request_id'])]
    print('A3 quoc_te: ti le lan chay co trang thai ok theo lan thu')
    for lan_thu, nhom in runs_quoc_te.groupby('attempt'):
        so_ok = (nhom['status'] == 'ok').sum()
        print(f'Lan {lan_thu}: {so_ok}/{len(nhom)} = {so_ok / len(nhom):.1%}')
    print('\nB1-B2: chi phi moi viec thanh cong [simulated]')
    for ten, (cps, thay_doi) in bang_do_nhay(runs, reqs).items():
        print(f'{ten:26s} {cps:>10,.0f} d  {thay_doi:>+6.1f}%')

    print('\nB3: chi phi ca he thong [simulated]')
    for gioi_han in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = len(reqs) - ket_qua['thanh_cong']
        ca_he_thong = ket_qua['tong'] + BASELINE * khong_thanh_cong
        print(f"{gioi_han} lan: tro ly {ket_qua['tong']:,.0f} d; "
              f"khong thanh cong {khong_thanh_cong}; ca he thong {ca_he_thong:,.0f} d; "
              f"moi viec thanh cong {ket_qua['cps']:,.0f} d")

    print('\nB4: xem lai tat ca [simulated]')
    for phut in (9, 15.3):
        ket_qua = xem_lai_tat_ca(runs, reqs, phut_lam_lai=phut)
        print(f"Lam lai {phut} phut/ca: {ket_qua['cps']:,.0f} d/viec thanh cong; "
              f"{ket_qua['cps'] / BASELINE:.2f} lan 12,000 d")

    # CP4 · Nhiệm vụ D: cỡ mẫu.
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    d1 = bang_co_mau()
    print('\nD1: co mau (baseline 0,70; +5 diem; alpha 0,05; power 0,8; ICC 0,02)')
    print(f"a) Theo yeu cau: {d1['a_theo_yeu_cau']:,} yeu cau moi nhom")
    print(f"b) Theo nhan vien, m=75: DE {d1['b_de']:.2f}; {d1['b_n']:,} moi nhom = "
          f"{d1['b_nguoi_moi_nhom']} nguoi moi nhom, tong {2 * d1['b_nguoi_moi_nhom']} > 40 nhan vien")
    print(f"c) 20 nhan vien moi nhom: toi da {d1['c_toi_da_20_nguoi']:,.0f} < {d1['a_theo_yeu_cau']:,}")
    print(f"d) 6 depot moi nhom: toi da {d1['d_toi_da_6_depot']:,.0f}")
    print(f"e) Chenh 6 diem ({d1['e_n_6_diem']} moi nhom), 20 nguoi moi nhom: "
          f"m >= {d1['e_m']} yeu cau moi nguoi; DE {d1['e_de']:.2f}")
    es5 = proportion_effectsize(0.75, 0.70)
    power5 = NormalIndPower().power(effect_size=es5, nobs1=d1['e_n_6_diem'], alpha=0.05)
    print(f"Power neu tac dong that chi 5 diem voi n={d1['e_n_6_diem']}: {power5:.2f}")
    pham_vi = reqs['loai'].isin(['noi_dia', 'hang_nang'])
    print(f"mo_lai_trong_7_ngay hien tai: {reqs['mo_lai_trong_7_ngay'].mean():.2%} "
          f"({reqs['mo_lai_trong_7_ngay'].sum()}/{len(reqs)}); "
          f"noi_dia + hang_nang: {reqs.loc[pham_vi, 'mo_lai_trong_7_ngay'].mean():.2%}")
