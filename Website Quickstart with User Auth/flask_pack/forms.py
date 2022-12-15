from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField, Field

from wtforms.validators import DataRequired,Length, Email, EqualTo, ValidationError
from  flask_pack.models import User,Transaction


class RegistrationForm(FlaskForm) :
    username = StringField('Username', validators=[DataRequired(),Length(min=3,max=20)])
    email = StringField('E-Mail', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])


    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Username already exists')

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already exists')


class LoginForm(FlaskForm) :
    email = StringField('E-Mail', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember User')

    submit = SubmitField('Login')

class PostForm(FlaskForm) :
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SongForm(FlaskForm) :
    title = StringField('Audio Name', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

class TransactionForm(FlaskForm) :
    id = StringField('ID', validators=[DataRequired()])
    amount = StringField('Amount', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SeedingForm(FlaskForm) :
    seeding = SubmitField('Seed')

class SeedingSongForm(FlaskForm) :
    seeding_song = SubmitField('Seed')