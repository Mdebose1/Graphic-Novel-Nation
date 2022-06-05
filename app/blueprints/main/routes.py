import imp
from flask import render_template, current_app as app
from datetime import datetime as dt
from app.blueprints.posts.models import Post

@app.route('/')
def home():
    return render_template('main/home.html', posts_list=[post.to_dict() for post in Post.query.all()])

@app.route('/popular')
def popular():
    return 'Popular'

@app.route('/genre')
def genre():
    return 'Genre'

@app.route('/login')
def login():
    return 'Login'

@app.route('/logout')
def logout():
    return 'Logout'

@app.route('/register')
def register():
    return 'Register'