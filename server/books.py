from settings import *

db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'author': self.author, 'read': self.read}

    def add_book(_title, _author, _read):
            new_book = Book(title=_title, author=_author, read=_read)
            db.session.add(new_book)
            db.session.commit()

    def get_all_books():
            return [Book.json(book) for book in Book.query.all()]

    def get_book(_id):
        return [Book.json(Book.query.filter_by(id=_id).first())]

    def update_book(_id, _title, _author, _read):
        book_to_update = Book.query.filter_by(id=_id).first()
        book_to_update.title = _title
        book_to_update.author = _author
        book_to_update.read = _read
        db.session.commit()

    def delete_book(_id):
        Book.query.filter_by(id=_id).delete()
        db.session.commit()