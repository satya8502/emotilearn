from flask_project import db

class books(db.Model):
    #_tablename_='book'
    id= db.Column(db.Integer,primary_key=True)
    book_title=db.Column(db.String(200),unique=True,nullable=False)
    author=db.Column(db.String(200),unique=False,nullable=False)
    book_text=db.Column(db.VARCHAR(10000),unique=False,nullable=False)

def _repr1_(self):
    return f'{self.id} : {self.book_title} : {self.author} : {self.book_text}'