# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: ToiYeuVinFast
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí, mức sử dụng và rủi ro của trợ lý hoàn phí LogiX-VN trên mẫu 1.200 yêu cầu giả lập; từ đó đề xuất kế hoạch pilot có đối chứng và luật dừng.

## 3. Giải pháp

Tóm tắt cách nhóm làm từng nhiệm vụ A–E và link tới file hồ sơ tương ứng.

- **A–B:** tính chi phí, so sánh theo loại và thử các kịch bản tại [bảng chi phí](bang_chi_phi.md), dùng [code của nhóm](../../src/lab13.py).
- **C:** đối chiếu hai bộ nhãn, đề xuất cách phát hiện và xử lý năm loại lỗi tại [bảng lỗi](bang_loi.md).
- **D:** tính cỡ mẫu, chọn cách chia và luật dừng tại [kế hoạch pilot](pilot_plan.yaml).
- **E:** xác định chỉ số, event và rủi ro tại [chỉ số](chi_so.md); tổng hợp đề xuất tại [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

Con số chính (ghi nhãn `simulated` khi cần) và đề xuất cuối của `ho_so_launch_v0.md`. Kết quả duyệt chéo nhóm nhận được từ hội đồng.

| Nhiệm vụ | Con số chính |
| --- | --- |
| A · Chi phí | 4.472 đ/việc thành công trên toàn mẫu (simulated), chưa gồm cố định; trong phạm vi noi_dia + hang_nang 4.599 đ/việc gồm cố định 40 triệu/tháng ở 45.000 yêu cầu/tháng (simulated), bằng 0,38 lần 12.000 đ |
| A3 · Phạm vi | noi_dia 0,22×, hang_nang 0,69×; loại quoc_te 1,88× (thành công 27,3%) và doi_tac 0,85× (thành công 54,4%) (simulated) |
| B · Độ nhạy | Làm lại gấp đôi +51,8%; xem lại gấp đôi +40,7%; lương +25% → +23,1% (simulated). Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống: 6.901.220 đ (simulated). Xem lại 100%: 11.743 đ/việc = 0,98× (simulated) |
| C · Lỗi | Hai bộ nhãn trùng 20/20; bảng khắc phục đủ năm loại, mỗi dòng có event, ngưỡng và vai trò |
| D · Pilot | Chia theo nhân viên 20 + 20; mde 6 điểm, 859/nhóm, m ≥ 299 yêu cầu/người, DE 6,96; power 0,64 nếu tác động thật 5 điểm |
| E · Chỉ số | Trong đợt chạy thử: chỉ số chính 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại 4,25% (51/1.200) |

Đề xuất: **Go có điều kiện** cho pilot noi_dia và hàng nặng; các điều kiện, vai trò phụ trách và ngày kiểm tra nằm trong hồ sơ launch. Con số bất lợi đã nêu: power 0,64 ở mức 5 điểm và xem lại 100% gần hoà vốn (0,98–1,03×). Kết quả duyệt chéo: chờ hội đồng đánh giá và bổ sung bằng chứng tại buổi.

## 5. Khó khăn và cách xử lý

- **Cỡ mẫu:** với 40 nhân viên, không cách chia theo cụm nào thấy được mức chênh 5 điểm (20 người tối đa 1.000 < 1.251). Nhóm đề xuất mức chênh 6 điểm, cần Giám đốc vận hành chấp nhận đánh đổi và xác nhận thời gian thu mẫu.
- **Lớp bắt đầu muộn:** giảng viên cho phép dùng AI hỗ trợ gắn nhãn lúc 14:50 để kịp phần tranh luận. Cả hai bộ nhãn đều có AI hỗ trợ, và AI đã đọc nhãn tham khảo hoặc quy tắc các ca dễ lẫn, nên kết quả 20/20 không chứng minh được tính độc lập; cả hai người gắn nhãn đều ghi rõ trong `bang_loi.md` và báo cáo cá nhân. Mỗi bộ nhãn được commit trước khi đối chiếu.
- **Môi trường:** máy của P2 thiếu `statsmodels` nên chưa chạy hết phần power; P4 tạo `.venv` trong `src/` theo `requirements.txt` và chạy hết `lab13.py` (ba phép thử A1 ĐẠT, D1 và power in ra đủ).
- **Làm song song:** mỗi người một nhánh, PR vào `main`; phân việc theo file để tránh xung đột.

## 6. Tổng hợp đóng góp

Tổng hợp từ bốn báo cáo cá nhân; chi tiết và bằng chứng trong `TEAM.md` và từng file `report/team/MSSV_HoTen.md`.

| Thành viên | Vai | Đóng góp chính | Công cụ AI |
| --- | --- | --- | --- |
| Chu Nguyen Tung Duong (2A202604016) | P1 · Người viết code | Ba hàm A1, mô hình A2, A3 theo loại, kịch bản B1–B4; điền số và đề xuất trong hồ sơ launch (PR #1, #3, #5, #8, #13, #16) | Codex |
| Tu Huy Bao (2A202604021) | P2 · Người kiểm số | Tính tay yêu cầu RF-70000 (12.262,694 đ, simulated) để đối chiếu A2; điền và đối chiếu B1–B4; ba chỉ số E1; hai rủi ro E2; kiểm tra lại kết quả D1 (PR #7, #14) | Codex |
| Nguyen Duc Khuong Lam (2A202604020) | P3 · Người gắn nhãn 1 | Bộ nhãn người 1 kèm căn cứ từng ca, chốt trước khi đối chiếu; bảng đối chiếu và tỉ lệ đồng thuận 20/20 (PR #10, #15) | Codex |
| Dong Huu Nguyen Khoa (2A202604000) | P4 · Người gắn nhãn 2, kiêm giữ hồ sơ | Bộ nhãn người 2; bảng khắc phục 5 ca; code D1 và `pilot_plan.yaml`; khung hồ sơ, 10 event và kiểm tra chéo chỉ số; tổng hợp báo cáo nhóm (PR #2, #6, #11, #12) | Claude Code |

Mọi con số trong hồ sơ do `src/lab13.py` tính hoặc tính tay có ghi cách tính; mỗi thành viên ghi cách tự kiểm tra kết quả AI trong mục 5 báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

- Chi phí xem lại và làm lại dựa trên thời gian simulated; trong pilot thay bằng phút đo thật từ `staff_review_decision` và `staff_rework_completed`.
- Kết quả 20/20 nhãn trùng cần đọc cùng lưu ý về AI ở mục 5; lần sau gắn nhãn tay trước, dùng AI chỉ để so.
- Ngưỡng chi phí 6.000 đ và mức bỏ qua gợi ý 40% trong luật dừng là lựa chọn của nhóm, cần kiểm tra lại sau tuần đầu pilot.
- Đợt chạy thử không có đối chứng: chỉ nói "chỉ số trong đợt chạy thử là…", chưa kết luận tác động của trợ lý.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức của lab](../../docs/du_lieu_va_cong_thuc.md).
- [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- [Quy tắc và cách sử dụng AI](../../RULES.md).
