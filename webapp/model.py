from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()

defenitions = db.Table('defenitions',
    db.Column('spanish_word_id', db.Integer, db.ForeignKey('spanish.id'), primary_key=True),
    db.Column('english_word_id', db.Integer, db.ForeignKey('english.id'), primary_key=True)
)

class Spanish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spanish_word = db.Column(db.String, unique=True, nullable=False)
    score = db.Column(db.Float, primary_key=True, default=0)
    defenitions = db.relationship('English', secondary=defenitions, lazy='subquery',
        backref=db.backref('spanish', lazy=True))

    def __repr__(self):
        return '<WordToLearn {} {}>'.format(self.spanish_word, self.score)



class English(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    english_word = db.Column(db.String, nullable=False)
    

