
import time
import json
from flask import Flask, request, render_template, url_for, flash, redirect,current_app, request,jsonify,send_file,send_from_directory,Response
from flask_pack.forms import RegistrationForm, LoginForm,PostForm, TransactionForm, SongForm, SeedingForm,SeedingSongForm
import sys
from flask_login import login_user, current_user,logout_user, login_required
from random import randint
from flask_caching import Cache
import pyaudio
import wave







from flask_pack import app,db,bcrypt






with app.app_context():

    from flask_pack.models import User,Post,init_db

    
    init_db()
    cache = Cache()
    cache.init_app(app) 
    

    
    
    

 

    @app.route('/')
    def index () :
        
        
        
        return render_template('home_page.html', title="MCoin")
    


        
    
    ## REGISTER ACCOUNT
    @app.route("/register",methods=['GET','POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegistrationForm()
        if form.validate_on_submit():
            hash_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data,email=form.email.data,password=hash_password)
            db.session.add(user)
            db.session.commit()


            flash(f'Welcome {form.username.data}!', 'success')
            print("success")
            return redirect(url_for('login'))

        return render_template('register_page.html', form = form)


    

            

        

    @app.route("/login",methods=['GET','POST'])         
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = LoginForm()
        if form.validate_on_submit():
                user = User.query.filter_by(email=form.email.data).first()
                if user and bcrypt.check_password_hash(user.password,form.password.data):
                    login_user(user,remember=form.remember.data)
                    next_page = request.args.get('next')
                    return redirect(next_page) if next_page else redirect(url_for('index'))
                else:
                    flash('Login Unsuccessful', 'danger')
        return render_template('login_page.html', form = form)

    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for('get_chain'))



    @app.route("/account",methods=['GET','POST'])
    @login_required
    def account():
        


        return render_template('account.html', tittle = 'Account')

