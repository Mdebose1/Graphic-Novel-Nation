from flask import render_template, current_app as app

@app.route('/shop')
def shop():
    return 'Shop'

@app.route('/checkout')
def checkout():
    return 'Checkout'

@app.route('/cart')
def cart():
    return 'Cart'