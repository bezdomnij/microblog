from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # not from flask_wtf
from wtforms.validators import DataRequired  # not from flask_wtf

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')
