from flask import render_template, current_app as app

@app.route('/posts')
def posts():
    return 'Posts'

@app.route('/user')
def user():
    return 'User'

@app.route('/profile')
def profile():
    return render_template('main/profile.html')

