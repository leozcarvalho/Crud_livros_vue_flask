from livros import *

@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify({'Movies': Livro.get_all_books()})

@app.route('/livros/<int:id>', methods=['GET'])
def get_movie_by_id(id):
    return_value = Livro.get_livro(id)
    return jsonify(return_value)

@app.route('/movies', methods=['POST'])
def add_livro():
    request_data = request.get_json()
    Livro.add_livro(request_data["title"], request_data["author"],
                    request_data["read"])
    response = Response("Book added", 201, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)