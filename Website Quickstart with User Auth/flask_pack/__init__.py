from flask import Flask, request, render_template, url_for, flash, redirect,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


## FLASK

app =  Flask(__name__, template_folder="templates")



app.config['SECRET_KEY'] = 'e627c60f18856c86381b84da6cfbaf321d0c7fa4d26c99c0242862c53b84f43f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

import run
# from models import User, Post
from flask_pack import routes