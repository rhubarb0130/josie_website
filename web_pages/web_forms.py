"""Copyright (c) 2020 Josephine Peacock all rights reserved"""

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, InputRequired


class LoginForm(FlaskForm):

    firstname = StringField('First Name', validators=[InputRequired(), Length(max=50)])
    lastname = StringField('Last Name', validators=[InputRequired(), Length(max=50)])
    email = StringField('Email', validators=[Email(), InputRequired(), Length(max=100)])
    message = TextAreaField('Message <br> (500 Max)', validators=[Length(max=500)])
    # submit = SubmitField('Submit')
    recaptcha = RecaptchaField()



