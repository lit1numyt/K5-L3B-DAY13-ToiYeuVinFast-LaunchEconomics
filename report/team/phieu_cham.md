# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ToiYeuVinFast · L3B
- Nhóm được chấm: Ghidorah · L3B (bằng chứng: bài trình bày Lab 13 của nhóm, dẫn hồ sơ launch v0 ở commit `5d22b97`)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 5 | Nhóm nêu đủ con số bất lợi: 12.415 đ/việc khi xem lại 100% và làm lại 15,3 phút, vượt 12.000 đ (simulated); power 64,18% nếu tác động thật 5 điểm. Có ba điều kiện kèm vai trò phụ trách. Nhưng No-go chưa khớp với số chính của nhóm: trong phạm vi đề xuất, chi phí là 4.599 đ/việc = 0,38× và cả hệ thống 5.751 đ/yêu cầu = 0,48× (simulated). Kịch bản vượt 12.000 đ là kịch bản cực đoan (xem lại 100%, trong khi đợt chạy thử chỉ xem lại 177/1.200 = 14,75%). Điều kiện 1 (chốt CP3) là việc của nhóm làm lab, không phải bằng chứng về trợ lý; mốc "trước 17:00" không có ngày |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mọi số từ cột phút đều có nhãn simulated (4.472 đ, cơ cấu 51,8% / 40,7%, 5.751 đ, 4.599 đ, 5.784 đ, 11.743 đ, 12.415 đ). Hoá đơn token và tool 274,7 đ đúng là không gắn nhãn. Phạm vi thu hẹp về nội địa + hàng nặng có số: quốc tế 22.515 đ/việc, thành công 27,3%, lần chạy ok 30,0% → 11,4% → 2,2%. Riêng đối tác (10.215 đ, dưới 12.000 đ) chưa có lý do loại bằng số trên slide |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Đối chứng đồng thời, ngẫu nhiên theo staff_id, phân tầng theo depot, 20 + 20 nhân viên; 299 yêu cầu/người = 5.980 thô, 859,20 hiệu dụng mỗi nhánh với DE 6,96; nêu đánh đổi mức chênh 6 điểm. Luật dừng có ngưỡng và thời hạn: mở lại > 6% hoặc cao hơn đối chứng ≥ 2 điểm trong 3 lần rà; hoàn trùng ≥ 1 ca; chi phí biến đổi > 8.000 đ trong 2 tuần; sửa hoặc bỏ gợi ý > 40% trong 1 tuần; Giám đốc vận hành tắt trợ lý trong 30 phút. Còn thiếu trên slide: vai trò phụ trách luật chi phí và luật sử dụng, ngày quyết định |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Số của chính nhóm Ghidorah ủng hộ chạy pilot trong phạm vi nội địa + hàng nặng: 4.599 đ/việc = 0,38× và 5.751 đ/yêu cầu cả hệ thống = 0,48× (simulated), thiết kế pilot đủ đối chứng và cỡ mẫu. Hội đồng đồng ý với ba điều kiện nhóm nêu và thêm hai điều kiện trước ngày khởi động: (1) có hai bộ nhãn lập độc lập, đồng thuận từ 16/20; (2) tính ngưỡng chi phí gồm cả chi phí cố định, vì ở nửa khối lượng ngưỡng 8.000 đ biến đổi tương đương 10.370 đ = 0,86× (simulated), gần sát 12.000 đ.

**Câu hỏi cho đội trình:**

1. Luật an toàn chỉ rà trên yêu cầu đã theo dõi đủ 7 ngày, rồi cần 3 lần rà. Như vậy phải mất ít nhất khoảng 10 ngày mới thấy vấn đề, trong khi mỗi bậc rollout chỉ kéo dài 1 tuần. Một sự cố ở bậc 10% có thể chỉ bị phát hiện khi đã lên bậc 25–50%. Luật có vế "KHÔNG THÌ" chặn việc chuyển bậc không?
2. Khi phát hiện từ 1 ca hoàn trùng trở lên thì ai làm gì, và trong bao lâu? Ngày quyết định của pilot là ngày nào?
3. Nếu chỉ có 20 nhân viên đủ điều kiện như trong mẫu thì chia 10 + 10, tối đa chỉ được 500 mẫu hiệu dụng, thấp hơn 859 cần có. Phương án dự phòng của nhóm là gì?

**Câu trả lời của đội trình (ghi lại tại buổi):** Chưa có câu trả lời.
