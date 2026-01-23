"""
E-commerce Database Creator
This script creates a SQLite database with sample e-commerce data
for SQL practice problems.
"""

import sqlite3
from datetime import datetime, timedelta
import random

def create_database():
    # Connect to SQLite database (creates if not exists)
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    # Drop existing tables if they exist
    tables = ['order_items', 'orders', 'products', 'categories', 'customers', 'reviews']
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
    
    # Create Categories table
    cursor.execute('''
        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL,
            description TEXT
        )
    ''')
    
    # Create Products table
    cursor.execute('''
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category_id INTEGER,
            price DECIMAL(10, 2) NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    ''')
    
    # Create Customers table
    cursor.execute('''
        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            city TEXT,
            country TEXT,
            registration_date DATE
        )
    ''')
    
    # Create Orders table
    cursor.execute('''
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            order_date DATETIME,
            status TEXT CHECK(status IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled')),
            total_amount DECIMAL(10, 2),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Create Order_Items table
    cursor.execute('''
        CREATE TABLE order_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER NOT NULL,
            unit_price DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Create Reviews table
    cursor.execute('''
        CREATE TABLE reviews (
            review_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            customer_id INTEGER,
            rating INTEGER CHECK(rating BETWEEN 1 AND 5),
            review_text TEXT,
            review_date DATE,
            FOREIGN KEY (product_id) REFERENCES products(product_id),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Insert Categories
    categories = [
        ('Electronics', 'Electronic devices and gadgets'),
        ('Clothing', 'Apparel and fashion items'),
        ('Home & Kitchen', 'Home decor and kitchen appliances'),
        ('Books', 'Physical and digital books'),
        ('Sports & Outdoors', 'Sports equipment and outdoor gear'),
        ('Beauty & Personal Care', 'Cosmetics and personal care products'),
        ('Toys & Games', 'Toys and board games')
    ]
    cursor.executemany("INSERT INTO categories (category_name, description) VALUES (?, ?)", categories)
    
    # Insert Products
    products = [
        ('iPhone 15 Pro', 1, 999.99, 50),
        ('Samsung Galaxy S24', 1, 899.99, 45),
        ('Sony WH-1000XM5 Headphones', 1, 349.99, 100),
        ('MacBook Pro 14"', 1, 1999.99, 30),
        ('iPad Air', 1, 599.99, 75),
        ('Nike Air Max 270', 2, 150.00, 200),
        ('Levi\'s 501 Jeans', 2, 89.99, 150),
        ('Adidas Ultraboost', 2, 180.00, 120),
        ('North Face Jacket', 2, 250.00, 80),
        ('Calvin Klein T-Shirt', 2, 45.00, 300),
        ('Instant Pot Duo', 3, 89.99, 60),
        ('KitchenAid Mixer', 3, 349.99, 40),
        ('Dyson V15 Vacuum', 3, 749.99, 35),
        ('Nespresso Machine', 3, 199.99, 55),
        ('Air Fryer Pro', 3, 129.99, 90),
        ('The Great Gatsby', 4, 14.99, 500),
        ('Atomic Habits', 4, 16.99, 400),
        ('Python Crash Course', 4, 39.99, 200),
        ('The Midnight Library', 4, 15.99, 350),
        ('Clean Code', 4, 44.99, 180),
        ('Yoga Mat Premium', 5, 49.99, 150),
        ('Dumbbells Set 20kg', 5, 79.99, 100),
        ('Running Shoes Pro', 5, 129.99, 80),
        ('Camping Tent 4-Person', 5, 199.99, 45),
        ('Mountain Bike', 5, 599.99, 25),
        ('Vitamin C Serum', 6, 29.99, 200),
        ('Face Moisturizer', 6, 24.99, 250),
        ('Perfume Collection', 6, 89.99, 100),
        ('Hair Dryer Pro', 6, 149.99, 70),
        ('Skincare Set', 6, 79.99, 120),
        ('LEGO Star Wars Set', 7, 159.99, 60),
        ('PlayStation 5 Controller', 7, 69.99, 150),
        ('Monopoly Board Game', 7, 29.99, 200),
        ('Nintendo Switch Games', 7, 59.99, 180),
        ('Remote Control Car', 7, 49.99, 100)
    ]
    cursor.executemany("INSERT INTO products (product_name, category_id, price, stock_quantity) VALUES (?, ?, ?, ?)", products)
    
    # Insert Customers
    customers = [
        ('John', 'Smith', 'john.smith@email.com', 'New York', 'USA', '2023-01-15'),
        ('Emily', 'Johnson', 'emily.j@email.com', 'Los Angeles', 'USA', '2023-02-20'),
        ('Michael', 'Williams', 'michael.w@email.com', 'Chicago', 'USA', '2023-03-10'),
        ('Sarah', 'Brown', 'sarah.b@email.com', 'Houston', 'USA', '2023-04-05'),
        ('David', 'Jones', 'david.j@email.com', 'Phoenix', 'USA', '2023-05-12'),
        ('Jessica', 'Garcia', 'jessica.g@email.com', 'Philadelphia', 'USA', '2023-06-18'),
        ('Christopher', 'Martinez', 'chris.m@email.com', 'San Antonio', 'USA', '2023-07-22'),
        ('Amanda', 'Robinson', 'amanda.r@email.com', 'San Diego', 'USA', '2023-08-30'),
        ('Daniel', 'Clark', 'daniel.c@email.com', 'Dallas', 'USA', '2023-09-14'),
        ('Ashley', 'Rodriguez', 'ashley.r@email.com', 'San Jose', 'USA', '2023-10-25'),
        ('James', 'Lee', 'james.lee@email.com', 'Toronto', 'Canada', '2023-01-28'),
        ('Olivia', 'Walker', 'olivia.w@email.com', 'Vancouver', 'Canada', '2023-03-15'),
        ('Robert', 'Hall', 'robert.h@email.com', 'London', 'UK', '2023-04-20'),
        ('Emma', 'Allen', 'emma.a@email.com', 'Manchester', 'UK', '2023-06-05'),
        ('William', 'Young', 'william.y@email.com', 'Sydney', 'Australia', '2023-07-10'),
        ('Sophia', 'King', 'sophia.k@email.com', 'Melbourne', 'Australia', '2023-08-18'),
        ('Benjamin', 'Wright', 'ben.wright@email.com', 'Berlin', 'Germany', '2023-09-22'),
        ('Isabella', 'Scott', 'isabella.s@email.com', 'Paris', 'France', '2023-10-30'),
        ('Alexander', 'Green', 'alex.g@email.com', 'Tokyo', 'Japan', '2023-11-15'),
        ('Mia', 'Baker', 'mia.baker@email.com', 'Seoul', 'South Korea', '2023-12-01')
    ]
    cursor.executemany("INSERT INTO customers (first_name, last_name, email, city, country, registration_date) VALUES (?, ?, ?, ?, ?, ?)", customers)
    
    # Insert Orders
    orders = [
        (1, '2024-01-05 10:30:00', 'Delivered', 1149.98),
        (2, '2024-01-08 14:15:00', 'Delivered', 349.99),
        (3, '2024-01-10 09:00:00', 'Delivered', 239.98),
        (4, '2024-01-12 16:45:00', 'Shipped', 999.99),
        (5, '2024-01-15 11:20:00', 'Delivered', 179.97),
        (1, '2024-01-18 13:30:00', 'Delivered', 599.99),
        (6, '2024-01-20 10:00:00', 'Processing', 449.98),
        (7, '2024-01-22 15:45:00', 'Delivered', 89.99),
        (8, '2024-01-25 09:30:00', 'Shipped', 1999.99),
        (9, '2024-01-28 12:00:00', 'Delivered', 330.00),
        (10, '2024-02-01 14:30:00', 'Cancelled', 599.99),
        (11, '2024-02-03 10:15:00', 'Delivered', 749.99),
        (12, '2024-02-05 16:00:00', 'Delivered', 199.99),
        (13, '2024-02-08 11:45:00', 'Shipped', 879.98),
        (14, '2024-02-10 09:20:00', 'Pending', 159.99),
        (15, '2024-02-12 13:00:00', 'Delivered', 629.98),
        (16, '2024-02-15 15:30:00', 'Delivered', 79.99),
        (17, '2024-02-18 10:45:00', 'Processing', 1349.98),
        (18, '2024-02-20 14:00:00', 'Delivered', 269.97),
        (19, '2024-02-22 12:30:00', 'Shipped', 899.99),
        (20, '2024-02-25 09:15:00', 'Delivered', 189.98),
        (1, '2024-03-01 11:00:00', 'Processing', 449.99),
        (2, '2024-03-03 14:45:00', 'Pending', 299.99),
        (3, '2024-03-05 10:30:00', 'Delivered', 579.98),
        (4, '2024-03-08 16:15:00', 'Delivered', 129.99),
        (5, '2024-03-10 13:00:00', 'Shipped', 849.97),
        (6, '2024-03-12 09:45:00', 'Delivered', 199.99),
        (7, '2024-03-15 15:00:00', 'Cancelled', 349.99),
        (8, '2024-03-18 11:30:00', 'Delivered', 674.98),
        (9, '2024-03-20 14:15:00', 'Processing', 399.99)
    ]
    cursor.executemany("INSERT INTO orders (customer_id, order_date, status, total_amount) VALUES (?, ?, ?, ?)", orders)
    
    # Insert Order Items
    order_items = [
        (1, 1, 1, 999.99),
        (1, 6, 1, 150.00),
        (2, 3, 1, 349.99),
        (3, 6, 1, 150.00),
        (3, 7, 1, 89.99),
        (4, 1, 1, 999.99),
        (5, 17, 2, 33.98),
        (5, 21, 1, 49.99),
        (5, 26, 2, 59.98),
        (6, 5, 1, 599.99),
        (7, 12, 1, 349.99),
        (7, 15, 1, 129.99),
        (8, 11, 1, 89.99),
        (9, 4, 1, 1999.99),
        (10, 8, 1, 180.00),
        (10, 6, 1, 150.00),
        (11, 5, 1, 599.99),
        (12, 13, 1, 749.99),
        (13, 14, 1, 199.99),
        (14, 2, 1, 899.99),
        (15, 31, 1, 159.99),
        (16, 5, 1, 599.99),
        (16, 26, 1, 29.99),
        (17, 22, 1, 79.99),
        (18, 3, 1, 349.99),
        (18, 1, 1, 999.99),
        (19, 9, 1, 250.00),
        (19, 18, 1, 39.99),
        (20, 2, 1, 899.99),
        (21, 27, 2, 49.98),
        (21, 33, 1, 29.99),
        (21, 34, 2, 119.98),
        (22, 12, 1, 349.99),
        (22, 15, 1, 129.99),
        (23, 9, 1, 250.00),
        (23, 21, 1, 49.99),
        (24, 4, 1, 1999.99),
        (25, 15, 1, 129.99),
        (26, 1, 1, 999.99),
        (27, 14, 1, 199.99),
        (28, 3, 1, 349.99),
        (29, 13, 1, 749.99),
        (30, 12, 1, 349.99),
        (30, 21, 1, 49.99)
    ]
    cursor.executemany("INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?)", order_items)
    
    # Insert Reviews
    reviews = [
        (1, 1, 5, 'Amazing phone! Best purchase ever.', '2024-01-20'),
        (1, 4, 4, 'Great phone but battery could be better.', '2024-01-25'),
        (2, 2, 5, 'Excellent Samsung device!', '2024-02-01'),
        (3, 3, 5, 'Best headphones I have ever owned.', '2024-01-15'),
        (4, 9, 4, 'Powerful laptop for work.', '2024-03-01'),
        (5, 5, 5, 'Perfect tablet for entertainment.', '2024-02-10'),
        (6, 8, 4, 'Comfortable running shoes.', '2024-01-28'),
        (7, 11, 3, 'Fits well but color faded after wash.', '2024-02-05'),
        (8, 10, 5, 'Most comfortable shoes ever!', '2024-02-15'),
        (11, 1, 2, 'Price is too high for what you get.', '2024-01-30'),
        (11, 13, 5, 'Instant Pot changed my cooking!', '2024-02-08'),
        (12, 14, 4, 'Great mixer but noisy.', '2024-02-20'),
        (13, 15, 5, 'Best vacuum on the market!', '2024-02-25'),
        (14, 16, 4, 'Great coffee every time.', '2024-03-05'),
        (15, 17, 5, 'Classic book, must read!', '2024-03-10'),
        (16, 18, 5, 'Life-changing book about habits.', '2024-03-12'),
        (17, 19, 4, 'Good for beginners learning Python.', '2024-03-15'),
        (18, 26, 5, 'High quality yoga mat.', '2024-03-18'),
        (19, 31, 4, 'Kids love it!', '2024-03-20'),
        (20, 28, 3, 'Serum is good but overpriced.', '2024-03-22')
    ]
    cursor.executemany("INSERT INTO reviews (product_id, customer_id, rating, review_text, review_date) VALUES (?, ?, ?, ?, ?)", reviews)
    
    # Commit and close
    conn.commit()
    conn.close()
    
    print("=" * 60)
    print("E-commerce Database Created Successfully!")
    print("=" * 60)
    print("\nDatabase: ecommerce.db")
    print("\nTables created:")
    print("  - categories (7 records)")
    print("  - products (35 records)")
    print("  - customers (20 records)")
    print("  - orders (30 records)")
    print("  - order_items (44 records)")
    print("  - reviews (20 records)")
    print("\nYou can now practice SQL queries on this database!")
    print("=" * 60)

if __name__ == "__main__":
    create_database()
