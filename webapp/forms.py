from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('your name', validators=[DataRequired()], render_kw = {'class' : 'form-control'})
    password = PasswordField('your pass', validators=[DataRequired()], render_kw = {'class' : 'form-control'})
    submit = SubmitField('done', render_kw = {'class' : 'btn btn-warning'})