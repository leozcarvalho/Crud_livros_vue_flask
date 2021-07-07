import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS
from markupsafe import escape

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Dom Casmurro',
        'author': 'Machado de Assis',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter e a pedra filosofal',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'O Menino maluqinho',
        'author': 'Ziraldo',
        'read': True
    }
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

@app.route('/books', methods=['POST'])
def add_books():
    response_object = {'status': 'success'}
    post_data = request.get_json()
    BOOKS.append({
        'id': uuid.uuid4().hex,
        'title': post_data.get('title'),
        'author': post_data.get('author'),
        'read': post_data.get('read')
    })
    response_object['message'] = 'Book added!'
    
@app.route('/books', methods=['GET'])
def get_all_books():
        response_object = {'status': 'success'}
        response_object['books'] = BOOKS
        return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
        return jsonify(response_object)

@app.route('/books/<book_id>', methods=['DELETE'])
def dele_book(book_id):
        response_object = {'status': 'success'}
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    

if __name__ == '__main__':
    app.run()