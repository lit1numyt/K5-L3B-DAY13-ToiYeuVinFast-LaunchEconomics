# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Đức Khương Lam (đã rà và chốt) · Người gắn nhãn 2: Dong Huu Nguyen Khoa (gắn trong 8 phút, không trao đổi)

Ghi chú: bộ nhãn người 2 gắn với hỗ trợ của Claude Code, được giảng viên cho phép lúc 14:50 vì lớp bắt đầu muộn. Bộ nhãn này được commit trước khi xem nhãn người 1.

Ghi chú người 1: Codex hỗ trợ đề xuất 20 nhãn từ mô tả ca. Codex đã đọc bảng nhãn tham khảo trong lượt rà tài liệu trước đó. P3 đã rà và chốt bộ nhãn trước khi đối chiếu với người 2.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20/20 ca (100%).

**Khớp bảng nhãn tham khảo:** 20/20 ca.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Có 0 ca cần thêm quy tắc phân biệt.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 6 | Do người dùng | `refund_request_created` có mục đã chọn khác loại suy ra từ mô tả (vd. chọn giao trễ, mô tả hàng vỡ), nối `ticket_reopened` qua trace_id; cảnh báo khi > 2% yêu cầu/tuần | Trợ lý so mục đã chọn với nội dung mô tả; lệch thì hỏi lại khách "Bạn muốn khiếu nại hàng hư hỏng?" trước khi từ chối | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ: hai `refund_ledger_write` ok cho cùng request_id; ngưỡng 0 ca, có ca là dừng gửi tiền tự động | Bắt buộc `idempotency_key` theo request_id cho mọi lệnh hoàn; yêu cầu gửi lại trong 24 giờ nối vào ticket cũ | Kỹ sư trưởng agent |
| 16 | Ngữ cảnh | Số phản ánh "làm phiền" trên tin nhắn gửi 22:00–07:00, theo tuần; ngưỡng > 0,5% tin nhắn đêm | Gom tin nhắn hoàn tiền ban đêm, gửi lúc 07:00; vẫn ghi sổ ngay để tiền về đúng hạn | Trưởng nhóm CSKH |
| 11 | Giới hạn hệ thống | `handoff_to_staff` với reason = dau_vao_khong_ho_tro (thoại, ảnh), đếm theo ngày và theo kênh | Báo rõ trợ lý chỉ đọc chữ, gợi ý mẫu câu ngắn hoặc chuyển nhân viên kèm tệp thoại; không để khách tự gõ lại từ đầu | PM trợ lý hoàn phí |
| 5 | Ngầm | `audit_sample_checked` 100 đơn/tuần, lọc riêng đơn có mã giảm giá; ngưỡng 1% đơn có so_tien_da_hoan ≠ so_tien_dung | Tool tính hoàn dùng giá sau giảm; thêm phép thử đơn có mã giảm giá vào bộ kiểm tra trước mỗi lần đổi prompt hoặc bảng giá | Kế toán trưởng |
