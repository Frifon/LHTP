from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

engspa = db.Table('engspa',
    db.Column('spanish_word_id', db.Integer, db.ForeignKey('spanish.id'), primary_key=True),
    db.Column('english_word_id', db.Integer, db.ForeignKey('english.id'), primary_key=True)
)

class Spanish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spanish_word = db.Column(db.String, unique=True, nullable=False)
    score = db.Column(db.Float, primary_key=True, default=0)
    defenitions = db.relationship('English', secondary=engspa, lazy='subquery',
        backref=db.backref('spanish', lazy=True))

    def __init__(self, spanish_word, eng_defs):
        self.spanish_word = spanish_word
        for eng_def in eng_defs:
            self.defenitions.append(English(eng_def))
        self.score = 0


    def __repr__(self):
        return '<Spanish {} {}>'.format(self.spanish_word, self.score)



class English(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english_word = db.Column(db.String, nullable=False)
    
    def __init__(self, english_word):
        self.english_word = english_word

    def __repr__(self):
        return '<English {} >'.format(self.english_word)
