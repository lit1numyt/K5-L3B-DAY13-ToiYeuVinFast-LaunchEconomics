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

Chi phí trên toàn mẫu là 4.472 đ/việc thành công (simulated), chưa gồm chi phí cố định. Làm lại gấp đôi làm chi phí tăng 51,8% (simulated); chỉ số đóng trong 24 giờ và không mở lại trong 7 ngày là 82,83% trong đợt chạy thử.

Đề xuất: **Go có điều kiện** cho pilot nội địa và hàng nặng, sau khi đáp ứng các điều kiện trong hồ sơ launch. Kết quả duyệt chéo: chờ hội đồng đánh giá và bổ sung bằng chứng tại buổi.

## 5. Khó khăn và cách xử lý

Với 20 nhân viên mỗi nhóm, mức chênh 5 điểm không đạt đủ cỡ mẫu hiệu dụng theo ICC giả định. Nhóm đề xuất mức chênh 6 điểm, cần giám đốc vận hành chấp nhận đánh đổi và xác nhận thời gian thu mẫu.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Chi phí nhân viên xem lại và làm lại hiện dựa trên thời gian simulated; cần đo thực tế trong pilot. Kết quả 20/20 nhãn trùng cần được đọc cùng ghi chú P3 dùng AI đã xem nhãn tham khảo; đánh giá tính độc lập theo bằng chứng trong bảng lỗi.

## 8. Tài liệu tham khảo

- [Dữ liệu và công thức của lab](../../docs/du_lieu_va_cong_thuc.md).
- [Hướng dẫn Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md).
- [Quy tắc và cách sử dụng AI](../../RULES.md).
