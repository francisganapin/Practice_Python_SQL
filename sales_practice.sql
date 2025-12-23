-- ==========================================
-- STEP 1: SETUP SALES DATABASE
-- Run these commands to create tables and add data.
-- ==========================================

-- 1. Create Tables
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    region TEXT
);

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price REAL
);

CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    sale_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- 2. Insert Sample Data

-- Customers
INSERT INTO customers (name, region) VALUES 
('Alice Johnson', 'North'),
('Bob Smith', 'South'),
('Charlie Brown', 'East'),
('Diana Prince', 'West'),
('Evan Wright', 'North');

-- Products
INSERT INTO products (name, category, price) VALUES 
('Laptop', 'Electronics', 1200.00),
('Wireless Mouse', 'Electronics', 25.50),
('Office Chair', 'Furniture', 150.00),
('Wooden Desk', 'Furniture', 300.00),
('Coffee Mug', 'Accessories', 12.99);

-- Sales
INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES 
(1, 1, 1, '2023-01-15'), -- Alice bought Laptop
(1, 2, 2, '2023-01-15'), -- Alice bought 2 Mice
(2, 3, 1, '2023-02-10'), -- Bob bought Chair
(3, 5, 4, '2023-02-20'), -- Charlie bought 4 Mugs
(4, 1, 1, '2023-03-05'), -- Diana bought Laptop
(5, 2, 1, '2023-03-10'), -- Evan bought Mouse
(2, 4, 1, '2023-04-01'), -- Bob bought Desk
(3, 2, 1, '2023-04-15'), -- Charlie bought Mouse
(1, 5, 2, '2023-05-01'), -- Alice bought 2 Mugs
(4, 3, 2, '2023-05-20'); -- Diana bought 2 Chairs

-- ==========================================
-- STEP 2: PRACTICE PROBLEMS
-- ==========================================

-- PROBLEM 1:
-- List all products that cost more than $100.
-- Expected Output: Laptop, Office Chair, Wooden Desk
-- Hint: Use WHERE price > ...

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 2:
-- Find the total number of customers in the 'North' region.
-- Expected Output: 2
-- Hint: Use COUNT(*) and WHERE

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 3:
-- List all sales showing the sale_date and quantity, sorted by sale_date (newest first).
-- Expected Output: Sales from May, then April, etc.
-- Hint: Use ORDER BY ... DESC

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 4:
-- Calculate the total revenue from all sales.
-- Note: Revenue = price * quantity. You'll need to join sales and products.
-- Expected Output: Total sum of all sales values.
-- Hint: Use SUM(products.price * sales.quantity) and JOIN

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 5:
-- Find the total quantity of each product sold.
-- Expected Output: Laptop: 2, Mouse: 4, etc.
-- Hint: Use GROUP BY product_id (or product name) and SUM(quantity)

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 6:
-- List the names of customers who have bought a 'Laptop'.
-- Expected Output: Alice Johnson, Diana Prince
-- Hint: Join customers, sales, and products. Filter by product name.

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 7:
-- Find the total amount spent by each customer.
-- Expected Output: Alice: $1276.98, etc.
-- Hint: Join customers, sales, products. Group by customer. SUM(price * quantity).

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 8:
-- Find the average price of products in the 'Electronics' category.
-- Expected Output: ~612.75
-- Hint: Use AVG() and WHERE category = ...

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 9:
-- Find the region that has generated the most revenue.
-- Expected Output: The region name with highest total sales.
-- Hint: Group by region, SUM revenue, ORDER BY sum DESC LIMIT 1.

-- Write your solution below:
-- SELECT ...


-- ==========================================
-- PROBLEM 10:
-- List products that have NEVER been sold.
-- (Note: In our sample data, all products have been sold, but write the query assuming one might not be).
-- Hint: Use LEFT JOIN and check where sales.id IS NULL.

-- Write your solution below:
-- SELECT ...
