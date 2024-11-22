from flask import Flask, jsonify, request

app = Flask(__name__)  # Initialize the Flask app

# Sample data (you could replace this with a database later)
books = [
    {"id": 1, "title": "Melania", "author": "Melania Trump", "price": 40.00, "year_published": 2024, "groupMember_name": ""},
    {"id": 2, "title": "The Alchemist", "author": "Paulo Coelho", "price": 7.21, "year_published": 1988, "groupMember_name": ""},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 22.19, "year_published": 1988, "groupMember_name": ""},
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

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
