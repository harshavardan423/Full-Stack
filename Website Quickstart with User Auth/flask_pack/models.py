
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_pack import db,app,login_manager,bcrypt
from flask_login import UserMixin
from hashlib import sha256
import json


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin) : 
    
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=True,nullable = False)
    email = db.Column(db.String(120),unique=True,nullable = False)
    image_file = db.Column(db.String(20),nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60),nullable = False)
    posts = db.relationship('Post', backref='author' , lazy=True)

    
    def __repr__(self) :
        return f"User('{self.username}', '{self.email}','{self.image_file}')"

class Post(db.Model) : 
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable= False)
    date_posted = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    user_id= db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    content = db.Column(db.Text,nullable=False)


    def __repr__(self) :
        return f"Post('{self.title}', '{self.date_posted}')"




def init_db():
    db.create_all()

   

