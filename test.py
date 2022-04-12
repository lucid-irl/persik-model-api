from class_text_preprocess import callmodel

doc = {"article": "kh\u00f4ng kh\u00f4ng th\u00eam v\u00e0 "}
lable = callmodel(doc["article"])
print(lable)



data = """
Chủ tịch tập đoàn Tân Hoàng Minh bị bắt
HÀ NỘIÔng Đỗ Anh Dũng, Chủ tịch Tập đoàn Tân Hoàng Minh, bị khởi tố với cáo buộc lừa đảo chiếm đoạt tài sản.

Ngày 5/4, ông Dũng, 61 tuổi, bị Cơ quan Cảnh sát điều tra Bộ Công an tạm giam.

Chủ tịch Tân Hoàng Minh Đỗ Anh Dũng. Ảnh: Anh Tú
Chủ tịch Tân Hoàng Minh Đỗ Anh Dũng. Ản""h: Anh Tú""

Ông Đỗ Anh Dũng, sinh năm 1961, hiện là Chủ tịch HĐQT kiêm Tổng giám đốc Tập đoàn Tân Hoàng Minh, Chủ tịch HĐQT Công ty cổ phần quản lý quỹ đầu tư chứng khoán Minh Việt.

Gần đây, Tân Hoàng Minh liên quan một số sự việc gây xôn xao dư luận. Ngày 10/12/2021, Công ty trách nhiệm hữu hạn Đầu tư Bất động sản Ngôi Sao Việt (thành viên của Tân Hoàng Minh) trúng thầu lô đất 3-12 ở Thủ Thiêm với giá 24.500 tỷ đồng, gấp 8,3 lần giá chào. Từ đây, đơn giá mỗi m2 lô đất này lên ngưỡng 2,43 tỷ đồng một m2, lập đỉnh tại thị trường Việt Nam.

Sau khi trúng thầu, ông Dũng giải thích lo ngại mảnh đất đẹp nhất Thủ Thiêm về tay người nước ngoài nên "trào lên lòng tự hào dân tộc" để quyết định trả giá cao hơn 3%, tương đương 700 tỷ đồng và giành quyền trúng thầu.

Đặt cọc 588,4 tỷ đồng, Tân Hoàng Minh ký hợp đồng mua bán 7 ngày sau phiên đấu giá. Đến ngày 10/1, Chủ tịch Tân Hoàng Minh bất ngờ xin đơn phương chấm dứt hợp đồng mua bán đấu giá lô đất 2,45 tỷ đồng một m2 ở Thủ Thiêm.

Ông Dũng sau đó tâm thư gửi Tổng Bí thư Nguyễn Phú Trọng và các lãnh đạo Đảng, Nhà nước về việc xin bỏ cọc. Ông Dũng thừa nhận kết quả đấu giá hơn 2,4 tỷ đồng một m2 đất có thể dẫn đến những hệ luỵ không tốt cho thị trường" nên xin chấp nhận mọi chế tài về việc đơn phương chấm dứt hợp đồng. Ngày 28/1, Tân Hoàng Minh chính thức bỏ cọc."""