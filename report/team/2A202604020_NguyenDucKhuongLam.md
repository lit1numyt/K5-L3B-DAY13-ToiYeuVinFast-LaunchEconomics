# Báo cáo cá nhân — Nguyễn Đức Khương Lam-2A202604020

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Khương Lam
- MSSV: 2A202604020
- Email: khuonglam.ai@gmail.com
- Vai trong nhóm: P3, người gắn nhãn 1

## 2. Phần việc phụ trách

- CP3: phân loại 20 ca theo 5 loại lỗi của Google PAIR, chốt bộ nhãn và đối chiếu với P4.

## 3. Đóng góp cụ thể

- Rà nguyên nhân chính của từng ca, ghi căn cứ và chốt đủ 20 nhãn trước khi xem bộ nhãn P4.
- Cập nhật bảng đối chiếu sau khi hai bộ nhãn đã chốt. Hai bộ trùng 20/20 ca (100%) và khớp bảng nhãn tham khảo 20/20 ca.

## 4. Bằng chứng

- Chốt bộ 20 nhãn trước khi đối chiếu với P4. [Bộ nhãn và căn cứ từng ca tại `5527354`](https://github.com/lit1numyt/K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics/blob/5527354/report/team/2A202604020_NguyenDucKhuongLam.md)
- Kết quả đối chiếu đã được merge vào `main` tại `a8f97f2`. [PR #10](https://github.com/lit1numyt/K5-L3B-DAY13-ToiYeuVinFast-LaunchEconomics/pull/10), [bảng đối chiếu nhãn](bang_loi.md).

## 5. Công cụ AI đã dùng

Dùng OpenAI Codex trong repo nhóm.

| Việc | AI làm gì | Cách kiểm tra |
| --- | --- | --- |
| Đọc đề (CP3) | Rà yêu cầu và rubric của nhiệm vụ C. | Đối chiếu năm loại lỗi và điều kiện gắn nhãn với đề gốc và `RULES.md`. |
| Gắn nhãn (CP3) | Đề xuất 20 nhãn và căn cứ theo mô tả ca. | P3 rà từng nhãn và căn cứ, xác nhận chốt trước khi so với P4. |
| Đối chiếu (CP3) | So hai cột nhãn và tổng hợp số ca trùng. | Đối chiếu 20 cặp nhãn trong `bang_loi.md` với commit chốt nhãn và kiểm tra kết quả trên PR đã merge. |
| Báo cáo cá nhân (CP5) | Soát cách trình bày và gắn link bằng chứng. | Kiểm tra đủ 6 mục theo mẫu, đối chiếu các số với `bang_loi.md` và PR #10. |

Codex đã đọc bảng nhãn tham khảo trước khi đề xuất. Cần đọc kết quả khớp bảng tham khảo cùng với giới hạn này.

## 6. Tự đánh giá

- Ca 6 cho thấy cần phân biệt nguyên nhân với cách khắc phục. Khách chọn sai mục, còn hỏi lại là cách trợ lý có thể phát hiện và xử lý.
- Ca 12 có chi phí bất thường suốt 3 tuần mà không ai phát hiện. Ở ca 15, nhân viên phát hiện mức hoàn sai trước khi gửi. Thời điểm phát hiện giúp phân biệt lỗi ngầm và lỗi hệ thống trong hai ca này.
