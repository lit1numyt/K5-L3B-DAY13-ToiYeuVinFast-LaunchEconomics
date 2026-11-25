# Báo cáo cá nhân — Nguyễn Đức Khương Lam-2A202604020

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Khương Lam
- MSSV: 2A202604020
- Email:
- Vai trong nhóm: P3, người gắn nhãn 1

## 2. Phần việc phụ trách

- CP3: gắn nhãn 20 ca lỗi, rà và chốt bộ nhãn trước khi đối chiếu với P4.

## 3. Đóng góp cụ thể

- CP3: rà và chốt bộ 20 nhãn có căn cứ theo từng ca.

## 4. Bằng chứng

- Bộ nhãn đã chốt được lưu tại commit `5527354`. Sau khi đối chiếu, hai bộ trùng 20/20 ca (100%). [Bảng đối chiếu nhãn](bang_loi.md)

### Bộ nhãn CP3

P3 đã rà và chốt bộ nhãn trước khi đối chiếu với P4.

| Ca | Nhãn | Căn cứ |
| ---: | --- | --- |
| 1 | Do người dùng | Khách nhập số tài khoản thiếu hai chữ số. |
| 2 | Hệ thống | Tool tra giá nhận tham số hàng thường cho kiện 28 kg, dẫn tới hoàn thiếu. |
| 3 | Ngữ cảnh | Tiền được hoàn vào ví đúng thiết kế. Khách chờ tiền về ngân hàng. |
| 4 | Giới hạn hệ thống | LogiX thiếu dữ liệu của chặng do hãng nước ngoài giao. |
| 5 | Ngầm | Hoàn theo giá trước giảm và chỉ phát hiện khi kiểm tra mẫu. |
| 6 | Do người dùng | Khách chọn mục giao trễ cho yêu cầu về hàng bị vỡ. |
| 7 | Hệ thống | Trợ lý báo đã hoàn dù ghi sổ cái thất bại sau ba lần thử. |
| 8 | Hệ thống | Trợ lý viện dẫn một điều khoản không có trong chính sách hiện hành. |
| 9 | Do người dùng | Khách nhập mã đơn sàn vào trường yêu cầu mã vận đơn. |
| 10 | Ngữ cảnh | Từ chối đúng điều khoản bất khả kháng. Cam kết hiển thị tạo kỳ vọng hoàn phí. |
| 11 | Giới hạn hệ thống | Trợ lý chưa xử lý được tin nhắn thoại. |
| 12 | Ngầm | Chi phí token của D05 tăng gấp ba suốt ba tuần mà không ai phát hiện. |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm thuộc sản phẩm đối tác, ngoài phạm vi trợ lý. |
| 14 | Do người dùng | Khách bấm xác nhận đã nhận tiền khi tiền chưa về. |
| 15 | Hệ thống | Trợ lý tính hoàn 100% thay vì 50% theo chính sách. Nhân viên phát hiện trước khi gửi. |
| 16 | Ngữ cảnh | Trợ lý gửi ngay theo thiết kế vào 2:14 sáng, thời điểm khách thấy bị làm phiền. |
| 17 | Ngầm | Bảng giá cũ làm sai tiền hoàn ở 212 đơn trong chín ngày và khách không mở lại. |
| 18 | Ngữ cảnh | Tiền hoàn đúng chính sách. Thiếu cách tính nên khách tưởng bị hoàn thiếu. |
| 19 | Giới hạn hệ thống | Đơn 14 tháng vượt quá cửa sổ dữ liệu 12 tháng. |
| 20 | Hệ thống | Lệnh hoàn thứ hai thiếu khóa chống trùng, dẫn đến hoàn hai lần. |

## 5. Công cụ AI đã dùng

**Công cụ** OpenAI Codex.

| Việc | AI làm gì | Cách kiểm tra |
| --- | --- | --- |
| Đọc đề (CP3) | Rà yêu cầu và rubric của nhiệm vụ C. | Đối chiếu năm loại lỗi và điều kiện gắn nhãn với đề gốc và `RULES.md`. |
| Gắn nhãn (CP3) | Đề xuất 20 nhãn và căn cứ theo mô tả ca. | P3 rà từng nhãn và căn cứ, xác nhận chốt trước khi so với P4. |

**Giới hạn** Codex đã đọc bảng nhãn tham khảo trong lượt rà tài liệu trước khi lập bộ đề xuất. Bộ đề xuất được lập trước khi xem nhãn P4.

## 6. Tự đánh giá

- Ca 12 là lỗi ngầm vì chi phí bất thường kéo dài 3 tuần mà không ai phát hiện. Ca 15 là lỗi hệ thống vì tính sai mức hoàn và đã bị nhân viên phát hiện trước khi gửi.
