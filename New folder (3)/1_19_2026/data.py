import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# -----------------------------
# CONNECT TO SQLITE DB
# -----------------------------
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# -----------------------------
# DROP TABLES IF EXIST
# -----------------------------
tables = ["customers", "products", "orders", "order_items", "payments"]
for t in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {t}")

# -----------------------------
# CREATE TABLES
# -----------------------------

cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    country TEXT,
    signup_date DATE
)
""")

cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER
)
""")

cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    status TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

cursor.execute("""
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    item_price REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
""")

cursor.execute("""
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    payment_date DATE,
    payment_method TEXT,
    amount REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
)
""")

# -----------------------------
# GENERATE DATA
# -----------------------------

np.random.seed(42)
random.seed(42)

countries = ["USA", "UK", "Canada", "Germany", "Philippines"]
categories = ["Electronics", "Clothing", "Home", "Books", "Sports"]
payment_methods = ["Credit Card", "PayPal", "GCash", "Bank Transfer"]
order_statuses = ["Completed", "Pending", "Cancelled"]

# -----------------------------
# CUSTOMERS
# -----------------------------
customers = []
for i in range(1, 101):
    customers.append((
        i,
        f"Customer_{i}",
        f"customer{i}@email.com",
        random.choice(countries),
        datetime.now() - timedelta(days=random.randint(30, 1500))
    ))

cursor.executemany("""
INSERT INTO customers VALUES (?, ?, ?, ?, ?)
""", customers)

# -----------------------------
# PRODUCTS
# -----------------------------
products = []
for i in range(1, 51):
    products.append((
        i,
        f"Product_{i}",
        random.choice(categories),
        round(random.uniform(10, 500), 2),
        random.randint(0, 300)
    ))

cursor.executemany("""
INSERT INTO products VALUES (?, ?, ?, ?, ?)
""", products)

# -----------------------------
# ORDERS
# -----------------------------
orders = []
for i in range(1, 301):
    orders.append((
        i,
        random.randint(1, 100),
        datetime.now() - timedelta(days=random.randint(1, 700)),
        random.choice(order_statuses)
    ))

cursor.executemany("""
INSERT INTO orders VALUES (?, ?, ?, ?)
""", orders)

# -----------------------------
# ORDER ITEMS
# -----------------------------
order_items = []
order_item_id = 1

for order_id in range(1, 301):
    for _ in range(random.randint(1, 4)):
        product_id = random.randint(1, 50)
        quantity = random.randint(1, 5)

        cursor.execute(
            "SELECT price FROM products WHERE product_id = ?",
            (product_id,)
        )
        price = cursor.fetchone()[0]

        order_items.append((
            order_item_id,
            order_id,
            product_id,
            quantity,
            price
        ))
        order_item_id += 1

cursor.executemany("""
INSERT INTO order_items VALUES (?, ?, ?, ?, ?)
""", order_items)

# -----------------------------
# PAYMENTS
# -----------------------------
payments = []
payment_id = 1

cursor.execute("""
SELECT o.order_id, SUM(oi.quantity * oi.item_price)
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE o.status = 'Completed'
GROUP BY o.order_id
""")

completed_orders = cursor.fetchall()

for order_id, total_amount in completed_orders:
    payments.append((
        payment_id,
        order_id,
        datetime.now() - timedelta(days=random.randint(1, 700)),
        random.choice(payment_methods),
        round(total_amount, 2)
    ))
    payment_id += 1

cursor.executemany("""
INSERT INTO payments VALUES (?, ?, ?, ?, ?)
""", payments)

# -----------------------------
# COMMIT & CLOSE
# -----------------------------
conn.commit()
conn.close()

print("✅ ecommerce.db created successfully!")
