# Team

## Thông tin nhóm

- Tên nhóm: ToiYeuVinFast
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/lit1numyt/K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics · `main` · (chốt khi nộp)

## Thành viên

| STT | Họ tên              | MSSV        | Email | GitHub    | Vai trò                                 |
| --: | --------------------- | ----------- | ----- | --------- | ---------------------------------------- |
|   1 | Nguyen Duc Khuong Lam | 2A202604020 |       |           | Người gắn nhãn 1                     |
|   2 | Chu Nguyen Tung Duong | 2A202604016 |       |           | Người code                             |
|   3 | Tu Huy Bao            | 2A202604021 |       |           | Người kiếm số                       |
|   4 | Dong Huu Nguyen Khoa  | 2A202604000 |       | lit1numyt | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

### Đóng góp cụ thể

### Bằng chứng

## NguyenDucKhuongLam-2A202604020

### Phần việc phụ trách

- Người gắn nhãn 1 (P3): gắn nhãn 20 ca lỗi ở CP3 và đối chiếu với P4 sau khi chốt hai bộ nhãn.

### Đóng góp cụ thể

- Rà và chốt 20 nhãn. Đối chiếu với P4, trùng 20/20 ca.

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202604020_NguyenDucKhuongLam.md), [bảng đối chiếu nhãn](report/team/bang_loi.md).

## ChuNguyenTungDuong-2A202604016

### Phần việc phụ trách

- Người viết code (P1): `src/lab13.py` phần A1–A3, B1–B4; điền hồ sơ launch CP5.

### Đóng góp cụ thể

- Ba hàm A1, mô hình A2, A3 theo loại, kịch bản B1–B4; cập nhật hồ sơ launch từ kết quả của nhóm.

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202604016_ChuNguyenTungDuong.md); PR #1, #3, #4, #5, #8, #13, #16.

## TuHuyBao-2A202604021

### Phần việc phụ trách

- Người kiểm số (P2): đối chiếu A2, bảng B1–B4, chỉ số E1, rủi ro E2.

### Đóng góp cụ thể

- Tính tay RF-70000 (12.262,694 đ, simulated); E1 82,83% · 27,12% · 4,25%; hai dòng rủi ro E2; kiểm tra lại D1.

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202604021_TuHuyBao.md); PR #7, #14; commit `47537b1`, `6e0f0f9`, `e0a386f`.

## DongHuuNguyenKhoa-2A202604000

### Phần việc phụ trách

- Người gắn nhãn 2 (CP3), người giữ hồ sơ (CP5); nhận thêm CP4 (code D1, `pilot_plan.yaml`).

### Đóng góp cụ thể

- Bộ nhãn người 2 (trùng P3 20/20); bảng khắc phục 5 ca đủ năm loại.
- Code D1 trong `src/lab13.py` và `report/team/pilot_plan.yaml` (20 + 20 nhân viên, mde 0,06, ba luật dừng).
- Khung hồ sơ launch, 10 event có `trace_id`, kiểm tra chéo chỉ số; tổng hợp `report/team/group_report.md`.

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202604000_DongHuuNguyenKhoa.md); PR #2, #6, #9, #11, #12 và nhánh `p4/cp5-reports`.
