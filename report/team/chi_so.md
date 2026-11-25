# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 994/1.200 = 82,83% |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 48/177 = 27,12% |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 51/1.200 = 4,25% |
| Dùng | Nhóm tự đề xuất: % yêu cầu trong nhóm can thiệp được mở bằng trợ lý | số `agent_suggestion_shown` có `arm = treatment` chia số `refund_request_created` có `arm = treatment` | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm) | số `audit_sample_checked` có `so_tien_da_hoan ≠ so_tien_dung` chia tổng số đơn được kiểm tra trong tuần | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách / cổng CSKH | request_id, loai, so_tien_vnd, depot, arm, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status (ok / loi), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| staff_review_decision | Nhân viên | staff_id, quyet_dinh (giu / sua / bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm giữ / sửa / bỏ |
| staff_rework_completed | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| handoff_to_staff | Agent | reason (het_3_lan / thieu_du_lieu / ngoai_pham_vi), tom_tat, trace_id | Khi chuyển cho nhân viên |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| ticket_closed | Hệ thống ticket | closed_at, created_at, trace_id | Khi ticket đóng |
| ticket_reopened | Khách / hệ thống ticket | reopened_at, reason, trace_id | Khi ticket mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, mẫu ngẫu nhiên |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created` (mẫu số) + `ticket_closed` (closed_at − created_at ≤ 24 giờ) + không có `ticket_reopened` trong 7 ngày, nối bằng trace_id.
- Tỉ lệ bỏ qua gợi ý: `staff_review_decision` (quyet_dinh là sua hoặc bo) chia tổng số `staff_review_decision`.
- Tỉ lệ lỗi lọt đến khách: `ticket_reopened` trong 7 ngày sau `ticket_closed` chia số `refund_request_created`.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created`, lọc arm = treatment.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked` (so_tien_da_hoan ≠ so_tien_dung) chia số đơn kiểm tra.
- Chi phí mỗi việc thành công (A2) đo lại được: `agent_run_completed` (token, tool) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số việc thành công. Hai cột phút hiện là simulated, thay bằng phút đo thật từ hai event này.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí tăng 51,8% lên 6.787 đ/việc thành công simulated, so với 4.472 đ simulated | Theo dõi tỉ lệ làm lại và chi phí mỗi tuần | Rà soát trace làm lại, xử lý nguyên nhân và cân nhắc thu hẹp phạm vi | PM trợ lý hoàn phí |
| Phải xem lại toàn bộ yêu cầu có lần chạy thành công trong phạm vi | 11.743 đ/việc simulated (0,98 lần 12.000 đ); nếu làm lại 15,3 phút/ca: 12.415 đ simulated (1,03 lần) | Theo dõi tỉ lệ và thời gian xem lại, thời gian làm lại thực tế mỗi tuần | Đo thời gian thực và giảm xem lại theo bậc khi dữ liệu an toàn cho phép | Trưởng nhóm CSKH |
