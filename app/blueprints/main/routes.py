import imp
from flask import render_template, current_app as app, request, redirect, url_for, flash
from datetime import datetime as dt
from app.blueprints.posts.models import Post
from app import db

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method =='POST':
        data = request.form.get('posts')
        p = Post(body=data, author='1ad38e4632eb450fbe9b2206fa9f10e5')
        db.session.add(p)
        db.session.commit()

        flash('Nice. Your post has been created!')
        return  redirect(url_for('home'))
    return render_template('main/home.html', posts_list=[post.to_dict() for post in Post.query.order_by(Post.date_created.desc()).all()])

@app.route('/popular')
def popular():
    return 'Popular'

@app.route('/genre')
def genre():
    return 'Genre'

@app.route('/logout')
def logout():
    return 'Logout'

@app.route('/register')
def register():
    return 'Register'