from flask import current_app as app, render_template, request, redirect, url_for, flash
from .models import User

@app.route('/posts')
def posts():
    return 'Posts'

@app.route('/user')
def user():
    return 'User'

@app.route('/profile')
def profile():
    return render_template('main/profile.html')

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_data = request.form
        user = User.query.filter_by(email=form_data.get('email')).first()

        if user is None:
            flash('That email address or password cannot be found. Please try again.')
            return redirect(url_for('login'))

        flash('Log in successful.')
        return redirect(url_for('home'))
    return render_template('users/login.html')

