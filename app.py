import os
import subprocess
from flask import Flask, render_template, request, redirect,url_for
import sqlite3
from predictor import predict_price

app = Flask(__name__)

def get_connection():
    conn = sqlite3.connect("comparex.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():

    keyword = request.args.get("product", "")

    conn = get_connection()

    results = conn.execute(
        """
        SELECT *
        FROM products
        WHERE name LIKE ?
        """,
        ('%' + keyword + '%',)
    ).fetchall()

    conn.close()

    return render_template(
        "search.html",
        keyword=keyword,
        results=results
    )
@app.route("/compare/<product_name>")
def compare(product_name):
    print("Database:", os.path.abspath("comparex.db"))
    conn = get_connection()

    # Get product details
    product = conn.execute(
        """
        SELECT *
        FROM products
        WHERE LOWER(name)=LOWER(?)
        """,
        (product_name,)
    ).fetchone()

    if product is None:
        conn.close()
        return "Product not found"

    # Get all store prices
    prices = conn.execute(
        """
        SELECT store, price,link
        FROM prices
        WHERE product_id=?
        ORDER BY price ASC
        """,
        (product["id"],)
    ).fetchall()
    print(product["id"])
    print(prices)
    conn.close()

    lowest_store = prices[0]["store"] if prices else None
    prediction = None

    if prices:
        prediction = predict_price(prices[0]["price"])
    return render_template(
    "compare.html",
    product=product,
    prices=prices,
    lowest_store=lowest_store,
    prediction=prediction
)
@app.route("/admin")
def admin():

    conn = get_connection()

    products = conn.execute(
        "SELECT * FROM products"
    ).fetchall()

    conn.close()

    return render_template(
        "admin.html",
        products=products
    )
@app.route("/add_product", methods=["POST"])
def add_product():

    name = request.form["name"]
    image = request.form["image"]

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO products(name, image)
        VALUES (?, ?)
        """,
        (name, image)
    )

    conn.commit()
    conn.close()

    return redirect("/admin")
print(app.url_map)
@app.route("/prices/<int:product_id>")
def prices(product_id):

    conn = get_connection()

    product = conn.execute(
        "SELECT * FROM products WHERE id=?",
        (product_id,)
    ).fetchone()

    store_prices = conn.execute(
        """
        SELECT *
        FROM prices
        WHERE product_id=?
        """,
        (product_id,)
    ).fetchall()

    conn.close()

    return render_template(
        "prices.html",
        product=product,
        store_prices=store_prices
    )
@app.route("/add_price/<int:product_id>", methods=["POST"])
def add_price(product_id):

    store = request.form["store"]
    price = request.form["price"]

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO prices(product_id, store, price)
        VALUES (?, ?, ?)
        """,
        (product_id, store, price)
    )

    conn.commit()
    conn.close()

    return redirect(f"/prices/{product_id}")
@app.route("/update_prices/<product_name>")
def update_prices(product_name):

    subprocess.run(["python3", "scrapers/update_prices.py", product_name])

    return redirect(url_for("compare", product_name=product_name))
@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):

    conn = get_connection()

    # Delete prices first
    conn.execute(
        "DELETE FROM prices WHERE product_id=?",
        (product_id,)
    )

    # Delete product
    conn.execute(
        "DELETE FROM products WHERE id=?",
        (product_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/admin")
print(app.url_map)
if __name__ == "__main__":
    
    app.run(debug=True)