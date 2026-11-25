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

**Câu trả lời của đội trình (ghi lại tại buổi):**

1. **Về độ trễ 10 ngày và vế "KHÔNG THÌ" chặn chuyển bậc.** Luật an toàn của nhóm có vế "KHÔNG THÌ" chặn việc chuyển bậc rõ ràng. Cụ thể, luật dừng an toàn quy định: "NẾU tỷ lệ mở lại trong 7 ngày của nhánh trợ lý vượt 6% hoặc cao hơn đối chứng từ 2 điểm phần trăm TRONG 3 lần rà hằng ngày liên tiếp trên các yêu cầu đủ 7 ngày theo dõi ở cả hai nhánh THÌ Giám đốc vận hành tắt trợ lý trong 30 phút KHÔNG THÌ giữ bước hiện tại cho đến khi hoàn tất rà an toàn". Đồng thời, luật dừng số 4 cũng chốt chặn: "KHÔNG THÌ chỉ chuyển bước sau khi điều kiện an toàn và chi phí đạt". Dù mỗi bậc rollout dự kiến diễn ra trong 1 tuần, vế "KHÔNG THÌ giữ bước hiện tại..." cấm hệ thống tự động nhảy từ 10% lên 25–50% khi chưa hoàn tất chu kỳ theo dõi 7 ngày và 3 ngày rà liên tiếp (tối thiểu 10 ngày). Bậc 10% bắt buộc phải giữ nguyên cho đến khi dữ liệu theo dõi 7 ngày của bậc đó vượt qua toàn bộ các lần rà an toàn.

2. **Xử lý sự cố hoàn trùng và ngày quyết định của pilot.** Khi phát hiện từ 1 ca hoàn trùng trở lên trong bất kỳ lần đối soát hằng ngày nào:
   - *Ai làm gì:* Giám đốc vận hành LogiX-VN thực hiện tắt trợ lý qua cờ cấu hình trong 30 phút, chuyển toàn bộ yêu cầu mới và yêu cầu đang chờ về luồng nhân viên xử lý thủ công (rollback), đồng thời giao bộ phận Kế toán đối soát toàn bộ các bút toán hoàn tiền.
   - *Ngày quyết định (decision date):* Là ngày thứ 8 sau yêu cầu cuối cùng của mẫu phân tích chính (ngày lịch cụ thể sẽ được chốt trước khi khởi động). Mốc này được chọn vì chỉ số chính yêu cầu theo dõi cửa sổ mở lại trong đủ 7 ngày; đến ngày thứ 8 dữ liệu mới đóng băng hoàn toàn để chạy phân tích hiệu quả chính một lần duy nhất.

3. **Phương án dự phòng khi chỉ có 20 nhân viên (10 + 10, tối đa 500 mẫu hiệu dụng).** Với 10 nhân viên mỗi nhánh, trần cỡ mẫu hiệu dụng là c / ICC = 10 / 0,02 = 500, không thể đạt 859 để nhận biết mức chênh 6 điểm ở Power 80%. Nhóm xử lý theo các phương án:
   - *Bảo vệ trạng thái No-go tại Gate 2a:* Đợt thử trước mới chạy ở 6 depot nên chỉ có 20 nhân viên. Toàn mạng lưới LogiX-VN có 12 depot với khoảng 40 nhân viên CSKH. Nhóm giữ đề xuất No-go cho đến khi Giám đốc vận hành xác nhận và huy động đủ 40 nhân viên (20 người/nhánh) từ mạng lưới 12 depot với cam kết sản lượng tối thiểu 299 yêu cầu/người.
   - *Phương án dự phòng kỹ thuật nếu chỉ có 20 người:* Nhóm buộc phải tính lại cỡ mẫu và trình cấp thẩm quyền ký chấp nhận đánh đổi thống kê — nới lỏng MDE lên mức cao hơn (khoảng 8–9 điểm phần trăm thay vì 6 điểm) để với 500 mẫu hiệu dụng vẫn giữ được Power 80%; hoặc nếu giữ MDE 6 điểm thì phải chấp nhận rủi ro Power sụt giảm sâu (dưới 60%).
   - *Tái ước lượng thực tế:* Trước khi phân tích, nhóm tiến hành kiểm đếm mẫu thực tế theo từng nhân viên, tính lại cỡ mẫu hiệu dụng nếu bị thiếu hụt hoặc lệch cụm và báo cáo kết quả kèm khoảng tin cậy mở rộng thay vì đưa ra kết luận khẳng định sai lầm.
