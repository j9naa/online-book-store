import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (you could replace this with a database later)
books = [
    {"id": 1, "title": "Melania", "author": "Melania Trump", "price": 40.00, "year_published": 2024, "groupMember_name": ""},
    {"id": 2, "title": "The Alchemist", "author": "Paulo Coelho", "price": 7.21, "year_published": 1988, "groupMember_name": ""},
    {"id": 3, "title": "The 48 Laws of Power", "author": "Robert Greene", "price": 22.19, "year_published": 1988, "groupMember_name": ""},
]

# Endpoint to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

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
    return jsonify(new_book), 201

# Endpoint to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    updated_data = request.get_json()  # Get JSON data from request body
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(updated_data)  # Update the book with the new data
        return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

# Endpoint to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books = [b for b in books if b['id'] != book_id]  # Remove the book from the list
        return jsonify({"message": "Book deleted"}), 200
    return jsonify({"message": "Book not found"}), 404

# Run the application
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
