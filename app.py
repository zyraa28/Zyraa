from flask import Flask, render_template, request

app = Flask(__name__)

# ---------- HOME PAGE ----------
@app.route('/')
def home():
    products = [
        {'id': 1, 'name': 'T-shirt', 'price': 19.99, 'image': 'shirt.jpg'},
        {'id': 2, 'name': 'Jeans', 'price': 39.99, 'image': 'jeans.jpg'},
        {'id': 3, 'name': 'Shoes', 'price': 59.99, 'image': 'shoes.jpg'}
    ]
    return render_template('index.html', products=products)


# ---------- SHOP PAGE ----------
@app.route('/shop')
def shop():
    products = [
        {'id': 1, 'name': 'T-shirt', 'price': 19.99, 'image': 'shirt.jpg'},
        {'id': 2, 'name': 'Jeans', 'price': 39.99, 'image': 'jeans.jpg'},
        {'id': 3, 'name': 'Shoes', 'price': 59.99, 'image': 'shoes.jpg'}
    ]
    return render_template('shop.html', products=products)


# ---------- PRODUCT PAGE ----------
@app.route('/product/<int:product_id>')
def product_page(product_id):
    products = [
        {'id': 1, 'name': 'T-shirt', 'price': 19.99, 'image': 'shirt.jpg'},
        {'id': 2, 'name': 'Jeans', 'price': 39.99, 'image': 'jeans.jpg'},
        {'id': 3, 'name': 'Shoes', 'price': 59.99, 'image': 'shoes.jpg'}
    ]
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template('product.html', product=product)


# ---------- CART PAGE ----------
@app.route('/cart')
def cart():
    return render_template('cart.html')


# ---------- CONTACT PAGE ----------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save to a text file
        with open('messages.txt', 'a') as f:
            f.write(f"Name: {name}\nEmail: {email}\nMessage: {message}\n---\n")

        return render_template('contact.html', success=True)

    return render_template('contact.html')


# ---------- ADMIN PAGE ----------
@app.route('/admin')
def admin():
    try:
        with open('messages.txt', 'r') as f:
            messages = f.read()
    except FileNotFoundError:
        messages = "No messages yet."

    return render_template('admin.html', messages=messages)


# ---------- RUN THE APP ----------
if __name__ == '__main__':
    app.run(debug=True)