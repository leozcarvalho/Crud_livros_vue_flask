from settings import *
import json

db = SQLAlchemy(app)

class Livro(db.Model):
    __tablename__ = 'livros'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

def json(self):
    return {'id': self.id, 'title': self.title,
            'author': self.author, 'read': self.read}

def add_livro(_title, _author, _read):
        new_livro = Livro(title=_title, author =_author, read =_read)
        db.session.add(new_livro)
        db.session.commit() 

def get_all_books():
        return [Livro.json(livro) for livro in Livro.query.all()]

def get_livro(_id):
        return [Livro.json(Livro.query.filter_by(id=_id).first())]

def delete_livro(_id):
        Livro.query.filter_by(id=_id).delete()
        db.session.commit()