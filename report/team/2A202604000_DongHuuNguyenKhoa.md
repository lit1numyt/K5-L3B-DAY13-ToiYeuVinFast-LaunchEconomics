# Báo cáo cá nhân — DongHuuNguyenKhoa-2A202604000

## 1. Thông tin thành viên

- Họ tên: Dong Huu Nguyen Khoa
- MSSV: 2A202604000
- Email:
- Vai trong nhóm: người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- CP1: điền thông tin nhóm trong `TEAM.md`.
- CP3: gắn nhãn 20 ca lỗi (người gắn nhãn 2), bảng khắc phục 5 ca (`bang_loi.md`).
- CP4: code D1 trong `src/lab13.py` và `pilot_plan.yaml` (nhận thêm phần này khi nhóm chạy muộn so với lịch).
- CP5: khung hồ sơ launch v0 (`ho_so_launch_v0.md`), danh sách event và kiểm tra chéo chỉ số (`chi_so.md`), tổng hợp `group_report.md`.

## 3. Đóng góp cụ thể

- **CP3 · Nhãn:** gắn 20 nhãn (Do người dùng 4, Hệ thống 5, Ngữ cảnh 4, Giới hạn 4, Ngầm 3), commit và push trước khi xem nhãn người gắn nhãn 1. Đối chiếu với P3: trùng 20/20.
- **CP3 · Bảng khắc phục:** 5 ca, mỗi loại một ca (6, 20, 16, 11, 5); mỗi dòng có event và ngưỡng đo được (vd. ca 20: hai `refund_ledger_write` ok cùng request_id, ngưỡng 0 ca) và một vai trò phụ trách.
- **CP4 · D1:** viết `co_mau`, `he_so_thiet_ke`, `m_toi_thieu`, `bang_co_mau` trong `src/lab13.py`: 1.251 yêu cầu/nhóm; DE 2,48 → 42 người/nhóm (> 40 nhân viên); 20 người tối đa 1.000; 6 depot tối đa 300; mức 6 điểm cần m ≥ 299, DE 6,96; power 0,64 nếu tác động thật 5 điểm; tỉ lệ mở lại 4,25% (3,97% trong phạm vi).
- **CP4 · pilot_plan.yaml:** chia theo nhân viên 20 + 20, mde 0,06 kèm đánh đổi ghi rõ, phạm vi noi_dia + hang_nang, ba luật dừng (an toàn, chi phí, mức dùng) đủ bốn vế; kiểm tra `yaml.safe_load` và không còn dấu `?`.
- **CP5:** dựng khung hồ sơ bảy mục với vai trò phụ trách (P1 điền số và đề xuất sau đó); viết 10 event có `trace_id`, kiểm tra chéo chỉ số ↔ event và hai chỉ số tự đề xuất; tổng hợp đóng góp vào `group_report.md`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- PR [#2](https://github.com/lit1numyt/K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics/pull/2) (CP1/CP5 khung hồ sơ, event): `b4f540a`, `b006f6b`, `bb951c4`, `4452169`.
- PR [#6](https://github.com/lit1numyt/K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics/pull/6) (CP3 bộ nhãn người 2): `1e75273`, `f404aed`, `ee02a96`.
- PR [#11](https://github.com/lit1numyt/K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics/pull/11) (CP3 bảng khắc phục): `c2316b5`.
- PR [#12](https://github.com/lit1numyt/K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics/pull/12) (CP4 D1 và pilot plan): `540b875`, `ed0d509`.
- File: [bang_loi.md](bang_loi.md), [pilot_plan.yaml](pilot_plan.yaml), [chi_so.md](chi_so.md), [src/lab13.py](../../src/lab13.py) (phần D1).

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

**Công cụ:** Claude Code (CLI, model Claude Opus 5.5), chạy trong repo nhóm.

| Việc | AI làm gì | Tôi kiểm tra thế nào |
| --- | --- | --- |
| Đọc đề, chia việc (14:00) | Tóm tắt README, CHECKPOINTS, RUBRIC; đề xuất chia 4 vai làm song song | Đối chiếu với bốn vai trong `TEAM.md` và lịch trong `CHECKPOINTS.md` |
| Khung hồ sơ launch v0 (CP5) | Dựng bảng bảy mục, gán người phụ trách là vai trò | Mỗi dòng có một vai trò, không có "cả đội"; trạng thái chỉ dùng ba giá trị cho phép |
| Danh sách event (CP5) | Đề xuất 10 event có `trace_id` và bảng kiểm tra chéo chỉ số ↔ event | Với từng chỉ số E1, kiểm tra tính được từ các event trong danh sách |
| Bảng khắc phục 5 ca (CP3) | Đề xuất ca, cách phát hiện, cách khắc phục, vai trò | Mỗi dòng có event trong `chi_so.md`, có ngưỡng và tần suất, không có "cả đội" |
| Code D1 và pilot plan (CP4) | Viết hàm cỡ mẫu, chạy `lab13.py`, điền `pilot_plan.yaml` | Chạy lại `python lab13.py`: ba phép thử A1 vẫn ĐẠT; đối chiếu D1 với công thức trong `docs/du_lieu_va_cong_thuc.md`; `yaml.safe_load` chạy được, `grep` không còn `?` |
| Báo cáo nhóm (CP5) | Tổng hợp đóng góp từ bốn báo cáo cá nhân | Đối chiếu từng dòng với báo cáo cá nhân và commit của từng người |
| Gắn nhãn 20 ca lỗi (CP3) | Gắn nhãn kèm một câu lý do cho mỗi ca; được giảng viên cho phép lúc 14:50 vì lớp bắt đầu muộn | Đọc lại từng ca theo định nghĩa năm loại; commit và push bộ nhãn trước khi xem nhãn người gắn nhãn 1 để giữ tính độc lập |
| Git | Tạo nhánh theo nhiệm vụ, commit nhỏ có tên checkpoint, push | Xem `git log` từng nhánh trước khi mở PR |

**Giới hạn đã biết:** trước khi gắn nhãn, AI đã đọc phần "Quy tắc cho các ca dễ lẫn" trong hướng dẫn chi tiết, nên bộ nhãn người 2 không hoàn toàn mù với đáp án; tỉ lệ khớp đáp án cần đọc với lưu ý này. AI không tạo con số nào trong hồ sơ: số chi phí, độ nhạy, cỡ mẫu lấy từ `src/lab13.py` và bảng của nhóm.

## 6. Tự đánh giá

- Đã làm: bộ nhãn người 2, bảng khắc phục 5 ca, toàn bộ CP4, khung hồ sơ và danh sách event; mỗi việc một nhánh, commit nhỏ có tên checkpoint.
- Hạn chế: phần lớn việc làm cùng AI; bộ nhãn không hoàn toàn độc lập vì AI đã đọc quy tắc các ca dễ lẫn. Ngưỡng 6.000 đ và 40% trong luật dừng, ngày bắt đầu và ngày quyết định là lựa chọn của tôi, cần nhóm thống nhất.
- Bài học: số cụm quyết định cỡ mẫu khi chia theo cụm (tối đa c / ICC), nên với 40 nhân viên không cách chia theo cụm nào thấy được mức chênh 5 điểm; gắn nhãn theo nguyên nhân gốc chứ không theo chỗ cần sửa.
