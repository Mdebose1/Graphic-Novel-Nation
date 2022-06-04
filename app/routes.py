from app import app

@app.route("/")
def home():
    return 'Home Page'

@app.route("/popular")
def popular():
    return "Popular"

@app.route("/genre")
def genre():
    return "Genre"

@app.route("/login")
def login():
    return "Login"

@app.route("/logout")
def logout():
    return "Logout"

@app.route("/register")
def register():
    return "Register"

@app.route("/shop")
def shop():
    return "Shop"

@app.route("/checkout")
def checkout():
    return "Checkout"

@app.route("/cart")
def cart():
    return "Cart"

@app.route("/posts")
def posts():
    return "Posts"

@app.route("/user")
def user():
    return "User"













