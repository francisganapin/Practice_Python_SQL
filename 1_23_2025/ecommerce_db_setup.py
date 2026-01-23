"""
E-Commerce Database Setup Script
Creates an SQLite database with e-commerce transaction data for practice.
"""

import sqlite3
from datetime import datetime, timedelta
import random

# Database connection
def create_database():
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    
    # Create Tables
    
    # Customers Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT,
            address TEXT,
            city TEXT,
            country TEXT,
            registration_date DATE NOT NULL
        )
    ''')
    
    # Categories Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            category_id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL,
            description TEXT
        )
    ''')
    
    # Products Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            category_id INTEGER,
            price DECIMAL(10, 2) NOT NULL,
            stock_quantity INTEGER DEFAULT 0,
            description TEXT,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    ''')
    
    # Orders Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_date DATETIME NOT NULL,
            status TEXT DEFAULT 'pending',
            shipping_address TEXT,
            total_amount DECIMAL(10, 2),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    ''')
    
    # Order Items Table (Transaction Details)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS order_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price DECIMAL(10, 2) NOT NULL,
            subtotal DECIMAL(10, 2) NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # Payments Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            payment_date DATETIME NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            payment_method TEXT NOT NULL,
            status TEXT DEFAULT 'completed',
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    ''')
    
    # Refunds Table (for backtracking refunded transactions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS refunds (
            refund_id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            refund_date DATETIME NOT NULL,
            refund_amount DECIMAL(10, 2) NOT NULL,
            reason TEXT,
            status TEXT DEFAULT 'processed',
            FOREIGN KEY (order_id) REFERENCES orders(order_id)
        )
    ''')
    
    conn.commit()
    print("✓ Tables created successfully!")
    return conn, cursor


def insert_sample_data(conn, cursor):
    """Insert sample data into the database"""
    
    # Insert Categories
    categories = [
        ('Electronics', 'Electronic devices and accessories'),
        ('Clothing', 'Apparel and fashion items'),
        ('Books', 'Physical and digital books'),
        ('Home & Kitchen', 'Home appliances and kitchen items'),
        ('Sports', 'Sports equipment and accessories'),
        ('Beauty', 'Beauty and personal care products')
    ]
    cursor.executemany('INSERT INTO categories (category_name, description) VALUES (?, ?)', categories)
    
    # Insert Products
    products = [
        ('iPhone 15 Pro', 1, 999.99, 50, 'Latest Apple smartphone'),
        ('Samsung Galaxy S24', 1, 899.99, 45, 'Premium Android phone'),
        ('MacBook Air M3', 1, 1299.99, 30, 'Apple laptop with M3 chip'),
        ('AirPods Pro 2', 1, 249.99, 100, 'Wireless earbuds'),
        ('Nike Air Max', 2, 129.99, 80, 'Running shoes'),
        ('Levi\'s 501 Jeans', 2, 79.99, 60, 'Classic denim jeans'),
        ('Adidas Hoodie', 2, 59.99, 70, 'Cotton blend hoodie'),
        ('Python Programming', 3, 49.99, 200, 'Learn Python programming'),
        ('Data Science Handbook', 3, 39.99, 150, 'Comprehensive DS guide'),
        ('SQL for Beginners', 3, 29.99, 180, 'SQL fundamentals book'),
        ('Instant Pot', 4, 89.99, 40, 'Multi-use pressure cooker'),
        ('Kitchen Aid Mixer', 4, 299.99, 25, 'Stand mixer'),
        ('Yoga Mat', 5, 24.99, 100, 'Non-slip yoga mat'),
        ('Dumbbells Set', 5, 149.99, 35, '5-50 lbs adjustable'),
        ('Moisturizing Cream', 6, 34.99, 90, 'Daily face moisturizer'),
        ('Perfume Set', 6, 79.99, 50, 'Designer fragrance collection')
    ]
    cursor.executemany('''
        INSERT INTO products (product_name, category_id, price, stock_quantity, description) 
        VALUES (?, ?, ?, ?, ?)
    ''', products)
    
    # Insert Customers
    customers = [
        ('John', 'Smith', 'john.smith@email.com', '555-0101', '123 Main St', 'New York', 'USA', '2023-01-15'),
        ('Emily', 'Johnson', 'emily.j@email.com', '555-0102', '456 Oak Ave', 'Los Angeles', 'USA', '2023-02-20'),
        ('Michael', 'Williams', 'mwilliams@email.com', '555-0103', '789 Pine Rd', 'Chicago', 'USA', '2023-03-10'),
        ('Sarah', 'Brown', 'sarah.b@email.com', '555-0104', '321 Elm St', 'Houston', 'USA', '2023-04-05'),
        ('David', 'Jones', 'djones@email.com', '555-0105', '654 Maple Dr', 'Phoenix', 'USA', '2023-05-12'),
        ('Jessica', 'Davis', 'jdavis@email.com', '555-0106', '987 Cedar Ln', 'Philadelphia', 'USA', '2023-06-18'),
        ('Robert', 'Miller', 'rmiller@email.com', '555-0107', '147 Birch Way', 'San Antonio', 'USA', '2023-07-22'),
        ('Amanda', 'Wilson', 'awilson@email.com', '555-0108', '258 Spruce Ct', 'San Diego', 'USA', '2023-08-30'),
        ('Daniel', 'Moore', 'dmoore@email.com', '555-0109', '369 Walnut Blvd', 'Dallas', 'USA', '2023-09-14'),
        ('Laura', 'Taylor', 'ltaylor@email.com', '555-0110', '741 Cherry St', 'San Jose', 'USA', '2023-10-25'),
        ('James', 'Anderson', 'janderson@email.com', '555-0111', '852 Ash Ave', 'Austin', 'USA', '2023-11-08'),
        ('Michelle', 'Thomas', 'mthomas@email.com', '555-0112', '963 Willow Rd', 'Jacksonville', 'USA', '2023-12-01')
    ]
    cursor.executemany('''
        INSERT INTO customers (first_name, last_name, email, phone, address, city, country, registration_date) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', customers)
    
    # Insert Orders with various statuses
    orders = [
        (1, '2024-01-05 10:30:00', 'completed', '123 Main St, New York', 1249.98),
        (2, '2024-01-07 14:15:00', 'completed', '456 Oak Ave, Los Angeles', 899.99),
        (3, '2024-01-10 09:45:00', 'completed', '789 Pine Rd, Chicago', 179.98),
        (1, '2024-01-12 16:20:00', 'completed', '123 Main St, New York', 249.99),
        (4, '2024-01-15 11:00:00', 'shipped', '321 Elm St, Houston', 1549.98),
        (5, '2024-01-18 13:30:00', 'completed', '654 Maple Dr, Phoenix', 89.98),
        (6, '2024-01-20 15:45:00', 'refunded', '987 Cedar Ln, Philadelphia', 999.99),
        (2, '2024-01-22 10:00:00', 'completed', '456 Oak Ave, Los Angeles', 389.97),
        (7, '2024-01-25 12:15:00', 'cancelled', '147 Birch Way, San Antonio', 449.98),
        (8, '2024-01-28 14:30:00', 'completed', '258 Spruce Ct, San Diego', 1299.99),
        (3, '2024-02-01 09:00:00', 'completed', '789 Pine Rd, Chicago', 79.99),
        (9, '2024-02-03 11:45:00', 'shipped', '369 Walnut Blvd, Dallas', 549.97),
        (10, '2024-02-05 16:00:00', 'completed', '741 Cherry St, San Jose', 174.97),
        (4, '2024-02-08 10:30:00', 'completed', '321 Elm St, Houston', 129.99),
        (11, '2024-02-10 14:00:00', 'refunded', '852 Ash Ave, Austin', 249.99),
        (5, '2024-02-12 12:30:00', 'completed', '654 Maple Dr, Phoenix', 299.99),
        (12, '2024-02-15 15:15:00', 'completed', '963 Willow Rd, Jacksonville', 89.99),
        (1, '2024-02-18 09:45:00', 'pending', '123 Main St, New York', 149.99),
        (6, '2024-02-20 11:00:00', 'completed', '987 Cedar Ln, Philadelphia', 79.99),
        (8, '2024-02-22 13:30:00', 'shipped', '258 Spruce Ct, San Diego', 899.99)
    ]
    cursor.executemany('''
        INSERT INTO orders (customer_id, order_date, status, shipping_address, total_amount) 
        VALUES (?, ?, ?, ?, ?)
    ''', orders)
    
    # Insert Order Items
    order_items = [
        (1, 1, 1, 999.99, 999.99),   # Order 1: iPhone
        (1, 4, 1, 249.99, 249.99),   # Order 1: AirPods
        (2, 2, 1, 899.99, 899.99),   # Order 2: Samsung Galaxy
        (3, 5, 1, 129.99, 129.99),   # Order 3: Nike shoes
        (3, 8, 1, 49.99, 49.99),     # Order 3: Python book
        (4, 4, 1, 249.99, 249.99),   # Order 4: AirPods
        (5, 3, 1, 1299.99, 1299.99), # Order 5: MacBook
        (5, 4, 1, 249.99, 249.99),   # Order 5: AirPods
        (6, 11, 1, 89.99, 89.99),    # Order 6: Instant Pot
        (7, 1, 1, 999.99, 999.99),   # Order 7: iPhone (refunded)
        (8, 12, 1, 299.99, 299.99),  # Order 8: KitchenAid
        (8, 11, 1, 89.99, 89.99),    # Order 8: Instant Pot
        (9, 14, 1, 149.99, 149.99),  # Order 9: Dumbbells (cancelled)
        (9, 12, 1, 299.99, 299.99),  # Order 9: KitchenAid (cancelled)
        (10, 3, 1, 1299.99, 1299.99),# Order 10: MacBook
        (11, 6, 1, 79.99, 79.99),    # Order 11: Jeans
        (12, 8, 2, 49.99, 99.98),    # Order 12: 2 Python books
        (12, 9, 1, 39.99, 39.99),    # Order 12: DS handbook
        (12, 10, 2, 29.99, 59.98),   # Order 12: 2 SQL books
        (12, 14, 1, 149.99, 149.99), # Order 12: Dumbbells
        (12, 11, 1, 89.99, 89.99),   # Order 12: Instant Pot (multiple items)
        (13, 15, 2, 34.99, 69.98),   # Order 13: 2 Moisturizers
        (13, 16, 1, 79.99, 79.99),   # Order 13: Perfume set
        (13, 13, 1, 24.99, 24.99),   # Order 13: Yoga mat
        (14, 5, 1, 129.99, 129.99),  # Order 14: Nike shoes
        (15, 4, 1, 249.99, 249.99),  # Order 15: AirPods (refunded)
        (16, 12, 1, 299.99, 299.99), # Order 16: KitchenAid
        (17, 11, 1, 89.99, 89.99),   # Order 17: Instant Pot
        (18, 14, 1, 149.99, 149.99), # Order 18: Dumbbells
        (19, 6, 1, 79.99, 79.99),    # Order 19: Jeans
        (20, 2, 1, 899.99, 899.99)   # Order 20: Samsung Galaxy
    ]
    cursor.executemany('''
        INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal) 
        VALUES (?, ?, ?, ?, ?)
    ''', order_items)
    
    # Insert Payments
    payments = [
        (1, '2024-01-05 10:35:00', 1249.98, 'credit_card', 'completed'),
        (2, '2024-01-07 14:20:00', 899.99, 'debit_card', 'completed'),
        (3, '2024-01-10 09:50:00', 179.98, 'paypal', 'completed'),
        (4, '2024-01-12 16:25:00', 249.99, 'credit_card', 'completed'),
        (5, '2024-01-15 11:05:00', 1549.98, 'credit_card', 'completed'),
        (6, '2024-01-18 13:35:00', 89.98, 'debit_card', 'completed'),
        (7, '2024-01-20 15:50:00', 999.99, 'credit_card', 'refunded'),
        (8, '2024-01-22 10:05:00', 389.97, 'paypal', 'completed'),
        (10, '2024-01-28 14:35:00', 1299.99, 'credit_card', 'completed'),
        (11, '2024-02-01 09:05:00', 79.99, 'debit_card', 'completed'),
        (12, '2024-02-03 11:50:00', 549.97, 'credit_card', 'completed'),
        (13, '2024-02-05 16:05:00', 174.97, 'paypal', 'completed'),
        (14, '2024-02-08 10:35:00', 129.99, 'debit_card', 'completed'),
        (15, '2024-02-10 14:05:00', 249.99, 'credit_card', 'refunded'),
        (16, '2024-02-12 12:35:00', 299.99, 'paypal', 'completed'),
        (17, '2024-02-15 15:20:00', 89.99, 'debit_card', 'completed'),
        (19, '2024-02-20 11:05:00', 79.99, 'credit_card', 'completed'),
        (20, '2024-02-22 13:35:00', 899.99, 'credit_card', 'completed')
    ]
    cursor.executemany('''
        INSERT INTO payments (order_id, payment_date, amount, payment_method, status) 
        VALUES (?, ?, ?, ?, ?)
    ''', payments)
    
    # Insert Refunds
    refunds = [
        (7, '2024-01-25 10:00:00', 999.99, 'Defective product', 'processed'),
        (15, '2024-02-15 09:00:00', 249.99, 'Customer changed mind', 'processed')
    ]
    cursor.executemany('''
        INSERT INTO refunds (order_id, refund_date, refund_amount, reason, status) 
        VALUES (?, ?, ?, ?, ?)
    ''', refunds)
    
    conn.commit()
    print("✓ Sample data inserted successfully!")


def display_database_summary(cursor):
    """Display summary of all tables"""
    print("\n" + "="*60)
    print("DATABASE SUMMARY")
    print("="*60)
    
    tables = ['customers', 'categories', 'products', 'orders', 'order_items', 'payments', 'refunds']
    
    for table in tables:
        cursor.execute(f'SELECT COUNT(*) FROM {table}')
        count = cursor.fetchone()[0]
        print(f"  {table.capitalize():15} : {count} records")
    
    print("="*60)


if __name__ == "__main__":
    print("\n🛒 E-COMMERCE DATABASE SETUP")
    print("-" * 40)
    
    conn, cursor = create_database()
    insert_sample_data(conn, cursor)
    display_database_summary(cursor)
    
    conn.close()
    print("\n✓ Database 'ecommerce.db' created successfully!")
    print("  You can now use this database for practice.\n")
