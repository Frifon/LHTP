from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class SpanishForm(FlaskForm):
    spanish_word = StringField('spanish word', validators=[DataRequired()], render_kw = {'class' : 'form-control'})
    english_words = StringField('english words', validators=[DataRequired()], render_kw = {'class' : 'form-control'})
    submit = SubmitField('done', render_kw = {'class' : 'btn btn-warning'})