import sqlite3
import sys

from amazon import get_amazon_price
from flipkart import get_flipkart_price
from croma import get_croma_price
# Get product name from Flask
product_name = sys.argv[1]

conn = sqlite3.connect("comparex.db")
cursor = conn.cursor()

# Get product id
cursor.execute(
    """
    SELECT id
    FROM products
    WHERE name=?
    """,
    (product_name,)
)

product = cursor.fetchone()

if not product:
    print("❌ Product not found!")
    conn.close()
    exit()

product_id = product[0]

print("Product ID:", product_id)

# Get live prices
amazon_price = get_amazon_price(product_name)
flipkart_price = get_flipkart_price(product_name)
croma_price = get_croma_price(product_name)
print("Croma Price:", croma_price)
print("Amazon Price:", amazon_price)
print("Flipkart Price:", flipkart_price)

# ---------------- Amazon ----------------

if amazon_price is not None:

    cursor.execute(
        """
        UPDATE prices
        SET price=?
        WHERE product_id=? AND store='Amazon'
        """,
        (amazon_price, product_id)
    )

    print("Amazon rows updated:", cursor.rowcount)

# ---------------- Flipkart ----------------

if flipkart_price is not None:

    cursor.execute(
        """
        UPDATE prices
        SET price=?
        WHERE product_id=? AND store='Flipkart'
        """,
        (flipkart_price, product_id)
    )

    print("Flipkart rows updated:", cursor.rowcount)
if croma_price is not None:

    cursor.execute(
        """
        UPDATE prices
        SET price=?
        WHERE product_id=? AND store='Croma'
        """,
        (croma_price, product_id)
    )

    print("Croma rows updated:", cursor.rowcount)

conn.commit()

print("\nCurrent Prices:")

cursor.execute(
    """
    SELECT store, price
    FROM prices
    WHERE product_id=?
    """,
    (product_id,)
)

for row in cursor.fetchall():
    print(row)

conn.close()

print("\n✅ Live prices updated successfully!")