from flask import Flask, jsonify, request

app = Flask(book store)

# Sample data (you could replace this with a database later)
books = [
    {"id": 1, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "price": 9.99},
    {"id": 2, "title": "1984", "author": "George Orwell", "price": 8.99},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 7.99},
]

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)  # Return books as JSON

# Endpoint to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Endpoint to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()  # Get JSON data from request body
    books.append(new_book)  # Add the new book to the list
    return jsonify(new_book), 201  # Return the new book as JSON

if book == '__main__':
    app.run(debug=True)
