import sqlite3

print("Starting database creation...")

conn = sqlite3.connect("comparex.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    store TEXT NOT NULL,
    price INTEGER NOT NULL,
    link TEXT,
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")

conn.commit()
conn.close()

print("✅ comparex.db created successfully!")