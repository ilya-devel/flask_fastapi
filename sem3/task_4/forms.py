from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email, Length


class RegistrationForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired(),
                                             Length(max=80)])
    email = StringField('Email', validators=[DataRequired(),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(),
                                                                     Length(min=8, max=20),
                                                                     EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    login = StringField('Login', validators=[DataRequired(),
                                             Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8, max=20)])
    submit = SubmitField('Register')