# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ToiYeuVinFast · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc trên toàn mẫu, chưa gồm cố định; trong phạm vi pilot là 4.599 đ/việc gồm cố định ở giả định 45.000 yêu cầu/tháng (simulated). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại gấp đôi +51,8%; xem lại gấp đôi +40,7%; lương tăng 25% làm chi phí tăng 23,1% (simulated). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Nhân viên: 12.000 đ/yêu cầu. Toàn mẫu, theo giả định B3 cộng 12.000 đ cho mỗi ca không thành công: 5.865 đ/yêu cầu, khoảng 0,49 lần; chưa gồm cố định (simulated). | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: đóng trong 24 giờ và không mở lại 7 ngày 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177 ca xem lại); mở lại 4,25% (51/1.200). Chưa có đối chứng để kết luận tác động. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn trùng 20/20; đã có 5 ca khắc phục cho 5 loại. Lưu ý P3 được AI hỗ trợ sau khi AI đã xem nhãn tham khảo; xem ghi chú trong bảng lỗi khi đánh giá tính độc lập. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Ngẫu nhiên theo nhân viên: 20 người mỗi nhóm, 859 mẫu hiệu dụng/nhóm cho mức chênh 6 điểm; mỗi người cần ít nhất 299 yêu cầu. Nếu chênh thật 5 điểm, power khoảng 0,64; ngày quyết định dự kiến 11/01/2027. | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi: 6.787 đ/việc, +51,8%; xem lại toàn bộ yêu cầu có lần chạy `ok` trong phạm vi: 11.743 đ/việc, hoặc 12.415 đ nếu làm lại 15,3 phút/ca (simulated). Đã có 2 dòng theo dõi và hành động trong `chi_so.md`. | Giả lập | PM trợ lý hoàn phí |

Phạm vi đề xuất: chỉ `noi_dia` và `hang_nang`. Loại `quoc_te` có chi phí 22.515 đ/việc (simulated) và chỉ 27,3% yêu cầu thành công; `doi_tac` có chi phí 10.215 đ/việc (simulated), thành công 54,4% và có điều khoản riêng.

- **Trước 04/12/2026:** Kỹ sư trưởng agent kiểm tra khóa chống hoàn trùng và đối soát sổ cái; PM trợ lý hoàn phí rà lại chi phí cả hệ thống và ngưỡng theo dõi hai rủi ro E2.
- **Trước 04/12/2026:** Giám đốc vận hành xác nhận chấp nhận đánh đổi mức chênh 6 điểm và power 0,64 nếu tác động thực là 5 điểm; kiểm tra đủ thời gian thu ≥ 299 yêu cầu/người và theo dõi mở lại 7 ngày trước ngày quyết định.
- **Trước 07/12/2026:** PM trợ lý hoàn phí kiểm tra đủ event có `trace_id`; Trưởng nhóm CSKH chốt cách giảm xem lại an toàn và đo thời gian thực, kiểm tra lại sau tuần đầu vào 14/12/2026.

**Đề xuất: Go có điều kiện** cho kế hoạch pilot: hoàn thành các điều kiện trước 07/12/2026 và kiểm tra lại số đo sau tuần đầu vào 14/12/2026.
