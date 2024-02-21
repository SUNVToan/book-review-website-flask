# Import packages
import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
import csv

# Header to set the requests as a browser requests
headers = {
    # Địa chỉ máy chủ mà yêu cầu đang được gửi tới
    "authority": "www.amazon.com",
    #  cho biết các loại nội dung (content types) mà trình duyệt web có thể hiểu và chấp nhận.
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "en-US,en;q=0.9,bn;q=0.8",
    #  trình duyệt và phiên bản trình duyệt của người dùng. Trong trường hợp này, đây là một trình duyệt Chromium/Chrome.
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    # cho thấy yêu cầu được gửi từ một trình duyệt web chạy trên hệ điều hành Linux, giả mạo là Chrome.
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    # "user-agent": Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
}

# URL of The amazon Review page
# reviews_url = "https://www.amazon.com/product-reviews/0380795272/?ie=UTF8&reviewerType=all_reviews/"

# Define Page No
len_page = 2


# Extra Data as Html object from amazon Review page
def reviewsHtml(url, len_page):
    # Empty List define to store all pages html data
    soups = []

    # Loop for gather all 3000 reviews from 300 pages via range
    for page_no in range(1, len_page + 1):
        review_url = f"{url}&pageNumber={page_no}"

        # Request make for each page
        response = requests.get(review_url, headers=headers)

        # Save Html object by using BeautifulSoup4 and lxml parser
        soup = BeautifulSoup(response.text, "lxml")

        # Add single Html page data in master soups list
        soups.append(soup)

    return soups


# Grab Reviews name, description, date, stars, title from HTML
def getReviews(html_data, isbn):
    # Create Empty list to Hold all data
    data_dicts = []

    # Select all Reviews BOX html using css selector
    boxes = html_data.select('div[data-hook="review"]')

    # Iterate all Reviews BOX
    for box in boxes:
        # Select Name using css selector and cleaning text using strip()
        # If Value is empty define value with 'N/A' for all.
        try:
            name = box.select_one('[class="a-profile-name"]').text.strip()
        except Exception as e:
            name = "N/A"

        try:
            stars = (
                box.select_one('[data-hook="review-star-rating"]')
                .text.strip()
                .split(" out")[0]
            )
        except Exception as e:
            stars = "N/A"

        try:
            title = box.select_one('[data-hook="review-title"]').text.strip()
        except Exception as e:
            title = "N/A"

        try:
            # Convert date str to dd/mm/yyy format
            datetime_str = (
                box.select_one('[data-hook="review-date"]')
                .text.strip()
                .split(" on ")[-1]
            )
            date = datetime.strptime(datetime_str, "%B %d, %Y").strftime("%d/%m/%Y")
            """
                %B: Biểu diễn tên của tháng (ví dụ: January, February, ..., December).
                %d: Biểu diễn ngày trong tháng (01 đến 31).
                %Y: Biểu diễn năm dưới dạng bốn chữ số.
                Ví dụ, nếu datetime_str là "January 15, 2023", thì phương thức strptime sẽ chuyển đổi chuỗi này thành một đối tượng datetime.
            """
        except Exception as e:
            date = "N/A"

        try:
            description = box.select_one('[data-hook="review-body"]').text.strip()
        except Exception as e:
            description = "N/A"

        # create Dictionary with al review data
        data_dict = {
            "Isbn": isbn,
            "Name": name,
            "Stars": stars,
            "Title": title,
            "Date": date,
            "Description": description,
        }

        # Add Dictionary in master empty List
        data_dicts.append(data_dict)

    return data_dicts


# ################


# Định nghĩa hàm để lấy dữ liệu HTML từ trang Amazon cho mỗi ISBN
def get_reviews_for_isbn(isbn, len_page):
    # Tạo URL cho mỗi cuốn sách
    reviews_url = f"https://www.amazon.com/product-reviews/{isbn}/?ie=UTF8&reviewerType=all_reviews/"

    # Lấy dữ liệu từ trang Amazon cho mỗi cuốn sách
    html_datas = reviewsHtml(reviews_url, len_page)

    # Empty List để lưu trữ tất cả dữ liệu đánh giá
    reviews = []

    # Lặp qua tất cả các trang HTML
    for html_data in html_datas:
        # Lấy dữ liệu đánh giá từ trang HTML và thêm ISBN cho mỗi review
        reviews.extend(getReviews(html_data, isbn))

    print("Data scraping completed for the book with ISBN:", isbn)
    return reviews


# Empty List để lưu trữ tất cả dữ liệu đánh giá từ tất cả các cuốn sách
all_reviews = []

# Mở file CSV để đọc
f = open("bookscopy.csv", "r")

# Đọc dữ liệu từ file CSV
csvreader = csv.reader(f)

# Bỏ qua dòng tiêu đề nếu cần
next(csvreader)

# Lặp qua từng dòng trong file CSV
for row in csvreader:
    reviews = get_reviews_for_isbn(row[0], len_page)
    all_reviews.extend(reviews)

f.close()

# Tạo DataFrame từ tất cả dữ liệu đánh giá
df_reviews = pd.DataFrame(all_reviews)

# Lưu dữ liệu vào tệp CSV
df_reviews.to_csv("reviews2.csv", index=False)

"""
# Mở file CSV để đọc
with open("bookscopy.csv", "r") as f:
    # Đọc dữ liệu từ file CSV
    csvreader = csv.reader(f)
    
    # Bỏ qua dòng tiêu đề nếu cần
    next(csvreader)
    
    # Lặp qua từng dòng trong file CSV
    for row in csvreader:
        reviews = get_reviews_for_isbn(row[0], len_page)
        all_reviews.extend(reviews)

# Tạo DataFrame từ tất cả dữ liệu đánh giá
df_reviews = pd.DataFrame(all_reviews)

# Lưu dữ liệu vào tệp CSV
df_reviews.to_csv("reviews1.csv", index=False)
"""
