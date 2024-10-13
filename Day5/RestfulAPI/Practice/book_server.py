from flask import Flask, request, jsonify

app = Flask(__name__)

books_db = []

@app.route("/")
def index():
    return "Book server is running ..."

@app.route("/books/list")
def get_list_books():
    return jsonify(books_db)

@app.route("/books/create")
def add_new_book():
    param = request.args
    new_id = param.get("id")

    check_id = find_book(new_id)

    result = {
        "status": 200,
        "message": "New book had been created and added to dataset"
    }

    if check_id >= 0:
        result["status"] = 401
        result["message"] = "This id had existed in dataset"
        return jsonify(result)

    new_title = param.get("title")
    new_author = param.get("author")

    new_book = {
        "id": new_id,
        "title": new_title,
        "author": new_author
    }

    db_old_len = len(books_db)

    books_db.append(new_book)

    if len(books_db) > db_old_len:
        return jsonify(result)
    else:
        result["status"] = 401
        result["message"] = "Error when creating or adding new book"
        return jsonify(result)
    
@app.route("/books/update")
def update_book():
    param = request.args
    id = param.get("id")

    result = {
        "status": 200,
        "message": "Book had been updated successfully"
    }

    check_id = find_book(id)

    if check_id < 0:
        result["status"] = 401
        result["message"] = "This book id is not existed in dataset"
        return jsonify(result)

    new_title = param.get("title")
    new_author = param.get("author")

    update_book = {
        "id": id,
        "title": new_title,
        "author": new_author
    }

    books_db[check_id] = update_book

    return jsonify(result)

@app.route("/book/remove")
def remove_book():
    param = request.args
    id = param.get("id")

    result = {
        "status": 200,
        "message": "Book had been removed"
    }

    check_id = find_book(id)

    if check_id < 0:
        result["status"] = 401
        result["message"] = "This book id is not existed in dataset"
        return jsonify(result)
    
    db_old_len = len(books_db)

    books_db.pop(check_id)

    if len(books_db) < db_old_len:
        return jsonify(result)
    else:
        result["status"] = 401
        result["message"] = "Error when creating or adding new book"
        return jsonify(result)

def find_book(id):
    for i, book in enumerate(books_db):
        if book["id"] == id:
            return i
    return -1


if __name__ == "__main__":
    app.run()