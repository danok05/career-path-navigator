from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[Length(max=64)])
    location = StringField('Location', validators=[Length(max=64)])
    skills = TextAreaField('Skills (comma-separated)')
    submit = SubmitField('Update Profile')