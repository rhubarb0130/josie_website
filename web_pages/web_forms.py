"""Copyright (c) 2020 Josephine Peacock all rights reserved"""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, InputRequired


class LoginForm(FlaskForm):

    firstname = StringField('First Name', validators=[InputRequired(), Length(min=4, max=25)])
    lastname = StringField('Last Name', validators=[InputRequired(), Length(max=25)])
    email = StringField('Email', validators=[Email(), InputRequired()])
    message = TextAreaField('message')
    submit = SubmitField('Submit')
    recaptcha = RecaptchaField()



