from books import *

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'Books': Book.get_all_books()})

@app.route('/books/<int:id>', methods=['GET'])
def get_book_by_id(id):
    return_value = Book.get_book(id)
    return jsonify(return_value)

@app.route('/books', methods=['POST'])
def add_book():
    request_data = request.get_json()
    Book.add_book(request_data["title"], request_data["author"],
                    request_data["read"])
    response = Response("Book added", 201, mimetype='application/json')
    return response

@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    request_data = request.get_json()
    Book.update_book(id, request_data['title'], request_data['author'],
    request_data['read'])
    response = Response("Book Updated", status=200, mimetype='application/json')
    return response

@app.route('/books/<int:id>', methods=['DELETE'])
def remove_book(id):
    Book.delete_book(id)
    response = Response("Book Deleted", status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)
