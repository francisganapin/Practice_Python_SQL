"""
SQL Practice Database Setup
Run this script to create and populate the practice database.
"""

import sqlite3
import os

def create_database():
    """Create the SQL practice database with sample data."""
    
    # Create database file
    db_path = os.path.join(os.path.dirname(__file__), 'practice.db')
    
    # Remove existing database if exists
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # ==========================================
    # CREATE TABLES
    # ==========================================
    
    # Employees table
    cursor.execute('''
        CREATE TABLE employees (
            employee_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            department_id INTEGER,
            hire_date DATE,
            salary DECIMAL(10, 2),
            manager_id INTEGER,
            FOREIGN KEY (department_id) REFERENCES departments(department_id),
            FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
        )
    ''')
    
    # Departments table
    cursor.execute('''
        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY,
            department_name TEXT NOT NULL,
            location TEXT,
            budget DECIMAL(12, 2)
        )
    ''')
    
    # Products table
    cursor.execute('''
        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT,
            price DECIMAL(10, 2),
            stock_quantity INTEGER,
            supplier_id INTEGER,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        )
    ''')
    
    # Suppliers table
    cursor.execute('''
        CREATE TABLE suppliers (
            supplier_id INTEGER PRIMARY KEY,
            supplier_name TEXT NOT NULL,
            contact_email TEXT,
            country TEXT
        )
    ''')
    
    # Orders table
    cursor.execute('''
        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            employee_id INTEGER,
            order_date DATE,
            total_amount DECIMAL(10, 2),
            status TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
        )
    ''')
    
    # Customers table
    cursor.execute('''
        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            city TEXT,
            country TEXT,
            registration_date DATE
        )
    ''')
    
    # Order_Items table
    cursor.execute('''
        CREATE TABLE order_items (
            item_id INTEGER PRIMARY KEY,
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            unit_price DECIMAL(10, 2),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
    ''')
    
    # ==========================================
    # INSERT SAMPLE DATA
    # ==========================================
    
    # Departments
    departments = [
        (1, 'Sales', 'New York', 500000),
        (2, 'Engineering', 'San Francisco', 800000),
        (3, 'Marketing', 'Chicago', 350000),
        (4, 'Human Resources', 'New York', 200000),
        (5, 'Finance', 'Boston', 400000)
    ]
    cursor.executemany('INSERT INTO departments VALUES (?, ?, ?, ?)', departments)
    
    # Employees
    employees = [
        (1, 'John', 'Smith', 'john.smith@company.com', 1, '2020-01-15', 75000, None),
        (2, 'Sarah', 'Johnson', 'sarah.johnson@company.com', 2, '2019-03-20', 95000, None),
        (3, 'Michael', 'Brown', 'michael.brown@company.com', 1, '2021-06-01', 55000, 1),
        (4, 'Emily', 'Davis', 'emily.davis@company.com', 2, '2020-09-10', 85000, 2),
        (5, 'David', 'Wilson', 'david.wilson@company.com', 3, '2018-11-25', 65000, None),
        (6, 'Jessica', 'Martinez', 'jessica.martinez@company.com', 2, '2022-02-14', 72000, 2),
        (7, 'Robert', 'Anderson', 'robert.anderson@company.com', 4, '2017-07-08', 60000, None),
        (8, 'Lisa', 'Taylor', 'lisa.taylor@company.com', 5, '2019-12-03', 78000, None),
        (9, 'James', 'Thomas', 'james.thomas@company.com', 1, '2023-01-10', 52000, 1),
        (10, 'Amanda', 'Garcia', 'amanda.garcia@company.com', 3, '2021-04-22', 58000, 5),
        (11, 'Chris', 'Lee', 'chris.lee@company.com', 2, '2020-08-15', 90000, 2),
        (12, 'Nicole', 'White', 'nicole.white@company.com', 5, '2022-05-30', 68000, 8)
    ]
    cursor.executemany('INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?)', employees)
    
    # Suppliers
    suppliers = [
        (1, 'Tech Supplies Inc', 'contact@techsupplies.com', 'USA'),
        (2, 'Global Electronics', 'sales@globalelec.com', 'China'),
        (3, 'Office Pro', 'info@officepro.com', 'Canada'),
        (4, 'Quality Goods Ltd', 'support@qualitygoods.com', 'UK'),
        (5, 'Fast Imports', 'order@fastimports.com', 'Germany')
    ]
    cursor.executemany('INSERT INTO suppliers VALUES (?, ?, ?, ?)', suppliers)
    
    # Products
    products = [
        (1, 'Laptop Pro 15', 'Electronics', 1299.99, 45, 1),
        (2, 'Wireless Mouse', 'Electronics', 29.99, 200, 2),
        (3, 'Office Chair', 'Furniture', 249.99, 75, 3),
        (4, 'Standing Desk', 'Furniture', 599.99, 30, 3),
        (5, 'Monitor 27"', 'Electronics', 399.99, 60, 1),
        (6, 'Keyboard Mechanical', 'Electronics', 89.99, 150, 2),
        (7, 'Webcam HD', 'Electronics', 79.99, 100, 4),
        (8, 'Desk Lamp', 'Furniture', 45.99, 120, 4),
        (9, 'USB Hub', 'Electronics', 24.99, 180, 2),
        (10, 'Notebook Pack', 'Office Supplies', 12.99, 500, 5)
    ]
    cursor.executemany('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)', products)
    
    # Customers
    customers = [
        (1, 'Alice', 'Cooper', 'alice.cooper@email.com', 'New York', 'USA', '2022-01-10'),
        (2, 'Bob', 'Martin', 'bob.martin@email.com', 'Los Angeles', 'USA', '2022-03-15'),
        (3, 'Carol', 'Williams', 'carol.w@email.com', 'Toronto', 'Canada', '2021-11-20'),
        (4, 'Daniel', 'Clark', 'daniel.c@email.com', 'London', 'UK', '2022-06-05'),
        (5, 'Eva', 'Schmidt', 'eva.schmidt@email.com', 'Berlin', 'Germany', '2023-02-28'),
        (6, 'Frank', 'Miller', 'frank.m@email.com', 'Chicago', 'USA', '2021-08-12'),
        (7, 'Grace', 'Lee', 'grace.lee@email.com', 'Vancouver', 'Canada', '2022-09-01'),
        (8, 'Henry', 'Wang', 'henry.wang@email.com', 'Shanghai', 'China', '2023-04-18')
    ]
    cursor.executemany('INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)', customers)
    
    # Orders
    orders = [
        (1, 1, 3, '2023-10-01', 1549.97, 'Completed'),
        (2, 2, 3, '2023-10-05', 329.98, 'Completed'),
        (3, 3, 9, '2023-10-10', 849.98, 'Shipped'),
        (4, 4, 3, '2023-10-12', 1299.99, 'Completed'),
        (5, 5, 9, '2023-10-15', 169.97, 'Processing'),
        (6, 1, 3, '2023-10-18', 599.99, 'Completed'),
        (7, 6, 9, '2023-10-20', 454.97, 'Shipped'),
        (8, 7, 3, '2023-10-22', 1799.97, 'Completed'),
        (9, 2, 9, '2023-10-25', 89.99, 'Completed'),
        (10, 8, 3, '2023-10-28', 2099.96, 'Processing'),
        (11, 3, 9, '2023-11-01', 279.98, 'Completed'),
        (12, 4, 3, '2023-11-05', 649.98, 'Shipped')
    ]
    cursor.executemany('INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?)', orders)
    
    # Order Items
    order_items = [
        (1, 1, 1, 1, 1299.99),
        (2, 1, 3, 1, 249.99),
        (3, 2, 2, 2, 29.99),
        (4, 2, 6, 3, 89.99),
        (5, 3, 5, 1, 399.99),
        (6, 3, 4, 1, 599.99),
        (7, 4, 1, 1, 1299.99),
        (8, 5, 2, 3, 29.99),
        (9, 5, 6, 1, 89.99),
        (10, 6, 4, 1, 599.99),
        (11, 7, 3, 1, 249.99),
        (12, 7, 7, 2, 79.99),
        (13, 7, 8, 1, 45.99),
        (14, 8, 1, 1, 1299.99),
        (15, 8, 5, 1, 399.99),
        (16, 8, 9, 4, 24.99),
        (17, 9, 6, 1, 89.99),
        (18, 10, 1, 1, 1299.99),
        (19, 10, 5, 2, 399.99),
        (20, 11, 3, 1, 249.99),
        (21, 11, 2, 1, 29.99),
        (22, 12, 4, 1, 599.99),
        (23, 12, 9, 2, 24.99)
    ]
    cursor.executemany('INSERT INTO order_items VALUES (?, ?, ?, ?, ?)', order_items)
    
    conn.commit()
    conn.close()
    
    print(f"✅ Database created successfully at: {db_path}")
    print("\n📊 Tables created:")
    print("   - employees (12 records)")
    print("   - departments (5 records)")
    print("   - products (10 records)")
    print("   - suppliers (5 records)")
    print("   - customers (8 records)")
    print("   - orders (12 records)")
    print("   - order_items (23 records)")
    print("\n🎯 You're ready to practice SQL!")

if __name__ == "__main__":
    create_database()
