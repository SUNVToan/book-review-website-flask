# Get 'works' key

https://openlibrary.org/api/books?bibkeys=ISBN:0380795272&jscmd=details&format=json

# Get ratings data

https://openlibrary.org/" + openlibrary_workskey + "/ratings.json

# get cover book

https://openlibrary.org/api/books?bibkeys=ISBN:{result.isbn}&jscmd=data&format=json

# get descriptions

https://openlibrary.org/works/OL554685W.json

export DATABASE_URL="postgresql://postgres:toan123@localhost:5435/book_review_website_flask"
export FLASK_APP=application.py
export DB_URL="postgresql://root:q8AiOgRQxlAzexLV9kPALYYc7Q4nm9Fa@dpg-cmo2jhmg1b2c73892edg-a.singapore-postgres.render.com/book_review_website_flask"
export API_KEY="AIzaSyA21Hcxik7d9Mht73qBIpl08-NT0c86-bQ"
