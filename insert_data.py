import sqlite3

conn = sqlite3.connect("comparex.db")
cursor = conn.cursor()

# Clear old data (optional)
cursor.execute("DELETE FROM prices")
cursor.execute("DELETE FROM products")

# Insert products
products = [
    ("iPhone 16", "images/iphone16.png"),
    ("MacBook Air M4", "images/macbook-air-m4.png"),
    ("Sony XM5", "images/sony-xm5.png"),
    ("PlayStation 5", "images/ps5.png")
]

cursor.executemany(
    "INSERT INTO products (name, image) VALUES (?, ?)",
    products
)

# Get product IDs
cursor.execute("SELECT id, name FROM products")
product_ids = {name: pid for pid, name in cursor.fetchall()}

# Insert prices
prices = [
    (product_ids["iPhone 16"], "Amazon", 71999),
    (product_ids["iPhone 16"], "Flipkart", 71499),
    (product_ids["iPhone 16"], "Croma", 72499),
    (product_ids["iPhone 16"], "Reliance Digital", 72199),

    (product_ids["MacBook Air M4"], "Amazon", 94999),
    (product_ids["MacBook Air M4"], "Flipkart", 95499),
    (product_ids["MacBook Air M4"], "Croma", 96999),

    (product_ids["Sony XM5"], "Amazon", 22999),
    (product_ids["Sony XM5"], "Flipkart", 29990),
    (product_ids["Sony XM5"], "Croma", 22799),

    (product_ids["PlayStation 5"], "Amazon", 49990),
    (product_ids["PlayStation 5"], "Flipkart", 50290),
    (product_ids["PlayStation 5"], "Reliance Digital", 49890)
]

cursor.executemany(
    "INSERT INTO prices (product_id, store, price) VALUES (?, ?, ?)",
    prices
)

conn.commit()
conn.close()

print("✅ Sample products inserted successfully!")