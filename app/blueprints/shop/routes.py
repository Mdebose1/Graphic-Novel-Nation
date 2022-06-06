from math import prod
from flask import current_app as app, render_template
import stripe

stripe.api_key = "sk_test_51L7nhTKW2PHafdlZ2JG2Qs0B1s93zhy5dxHQTIIwkl11s1qHWLQgpn4nzIDUeXBuApzW1fq5GBZ0snR8Lj9r9Vl500SDgU5KmF"


@app.route('/items')
def items():
    products = []
    for product in stripe.Product.list()['data']:
        product_dict = {
            'id': product['id'],
            'name': product['name'],
            'description': product['description'] ,
            'price':stripe.Price.retrieve(product['default_price']) ['unit_amount'] /100,
            'image': product['images'][0],
        }
        products.append(product_dict)
    return render_template('shop/items.html', products=products )

@app.route('/checkout')
def checkout():
    return 'Checkout'

@app.route('/cart')
def cart():
    return 'Cart'