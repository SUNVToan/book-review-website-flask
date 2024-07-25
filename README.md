# Book Review Website
# Overview
- Đây là một dự án nhỏ cho học phần công nghệ web trường yêu cầu. 
- Yêu cầu là dùng API bên khác như là Goodreads, bất kỳ... để phát đọc được dữ liệu sách. 
- Tính năng chính của web này là Đăng ký, đăng nhập, đăng xuất tài khoản và tìm kiếm sách, trang sách, xem chi tiết sách và gửi đánh giá, bình luận. 
- File book.csv có sẵn.
- Công nghệ sử dụng trong dự án cụ thể là:
  - Flask framework.
  - Python.
  - Postgres.
  - API thì dùng của Open Library API, lấy cách thông tin cơ bản như, ảnh bìa, đánh giá,... 
  - Dùng Beautiful Soup 4 crawl dữ liệu đánh giá từ website amazon book để người dùng tham khảo chất lượng của một quyển sách.
  - Về phía Frontend dùng HTML, CSS và Jinja cơ bản.

# Installation

## Chuẩn bị môi trường develop
* postgreSQL (Có thể dùng docker để build)
* Python 3.11.x

## Tham khảo
1. Clone the repository
2. Trong terminal truy cập vào đúng thư mục hệ thống
3. Run `pip3 install -r requirements.txt` để chắc chắn cài đặt đầy đủ thư viện
4. Cài đặt biến môi trường:
	  * On Ubuntu: `export FLASK_APP=application.py`.
    - Sử dụng Open library API `https://openlibrary.org/developers/api`
    - `DATABASE_URL` = kết nối dạng string vào database postgres (for example: `postgres://username:password@localhost:5432/databasename` )
5. Dùng `tables.sql` để tạo cơ sở dữ liệu.
6. Run `python3 import.py` để import dữ liệu từ book.csv vào database
7. Chạy lệnh `flask run` trong terminal để chạy app trên local

# Cảm xúc và kiến Thức Thu Nhận Được Qua Dự Án Này
Tuy là một dự án nhỏ, cơ bản nhưng nó sẽ có ích với ai đang học tập thử dùng framework phát triển web. Này là dự án đầu tay phát triển bằng framework nên học được rất nhiều thứ từ, kết nối postgres với app, cách gọi, tương tác với API endpoint, cách mã hóa mật khẩu người dùng cần thiết, cách phát triển cách tính năng cho một website, cách đọc dữ liệu trả về sau xử lý, cách bắt lỗi xảy ra, cách giải quyết vấn đề, trên hết là làm việc cùng team các đồng đội tuyệt vời có cùng xuất phát điểm cố gắng đọc hiểu và xây dựng website này. Xin cảm ơn tác giả mã nguồn nữa. Chúc tác giả sẽ luôn phát triển hơn trong sự nghiệp.
