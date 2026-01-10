# SQL Cheat Sheet 📋

## 🔹 Basic Queries

```sql
-- Select all columns
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Select with alias
SELECT column1 AS alias_name FROM table_name;

-- Select distinct values
SELECT DISTINCT column FROM table_name;
```

---

## 🔹 Filtering (WHERE)

```sql
-- Basic comparison
SELECT * FROM employees WHERE salary > 50000;

-- Multiple conditions
SELECT * FROM products WHERE price > 100 AND category = 'Electronics';
SELECT * FROM products WHERE price < 50 OR stock_quantity > 100;

-- NULL check
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;

-- IN operator
SELECT * FROM employees WHERE department_id IN (1, 2, 3);

-- BETWEEN (inclusive)
SELECT * FROM products WHERE price BETWEEN 50 AND 200;

-- LIKE patterns
SELECT * FROM customers WHERE email LIKE '%@gmail.com';  -- ends with
SELECT * FROM customers WHERE first_name LIKE 'J%';      -- starts with
SELECT * FROM products WHERE product_name LIKE '%Pro%';  -- contains
```

---

## 🔹 Sorting & Limiting

```sql
-- Order by (default ASC)
SELECT * FROM employees ORDER BY salary;

-- Order descending
SELECT * FROM employees ORDER BY salary DESC;

-- Multiple columns
SELECT * FROM employees ORDER BY department_id, salary DESC;

-- Limit results
SELECT * FROM products ORDER BY price DESC LIMIT 5;

-- Offset (skip rows)
SELECT * FROM products LIMIT 10 OFFSET 5;
```

---

## 🔹 Aggregate Functions

```sql
-- Count rows
SELECT COUNT(*) FROM employees;
SELECT COUNT(DISTINCT department_id) FROM employees;

-- Sum values
SELECT SUM(salary) FROM employees;

-- Average
SELECT AVG(price) FROM products;
SELECT ROUND(AVG(salary), 2) FROM employees;

-- Min / Max
SELECT MIN(price), MAX(price) FROM products;
```

---

## 🔹 GROUP BY & HAVING

```sql
-- Group by column
SELECT department_id, COUNT(*) 
FROM employees 
GROUP BY department_id;

-- Multiple aggregations
SELECT 
    category,
    COUNT(*) as count,
    AVG(price) as avg_price,
    SUM(stock_quantity) as total_stock
FROM products 
GROUP BY category;

-- HAVING (filter groups)
SELECT category, COUNT(*) as count
FROM products
GROUP BY category
HAVING COUNT(*) > 2;
```

---

## 🔹 JOINs

```sql
-- INNER JOIN (matching rows only)
SELECT e.first_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;

-- LEFT JOIN (all from left table)
SELECT d.department_name, e.first_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id;

-- RIGHT JOIN (all from right table)
SELECT e.first_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id;

-- Multiple JOINs
SELECT 
    o.order_id,
    c.first_name as customer,
    e.first_name as employee
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN employees e ON o.employee_id = e.employee_id;
```

---

## 🔹 Subqueries

```sql
-- Subquery in WHERE
SELECT * FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Subquery in FROM
SELECT avg_dept.department_id, avg_dept.avg_salary
FROM (
    SELECT department_id, AVG(salary) as avg_salary
    FROM employees
    GROUP BY department_id
) as avg_dept;

-- Correlated subquery
SELECT e1.first_name, e1.salary
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);

-- EXISTS
SELECT * FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);
```

---

## 🔹 CASE Statements

```sql
-- Simple CASE
SELECT 
    product_name,
    CASE category
        WHEN 'Electronics' THEN 'Tech'
        WHEN 'Furniture' THEN 'Office'
        ELSE 'Other'
    END as category_type
FROM products;

-- Searched CASE
SELECT 
    product_name,
    stock_quantity,
    CASE 
        WHEN stock_quantity < 50 THEN 'Low'
        WHEN stock_quantity <= 100 THEN 'Medium'
        ELSE 'High'
    END as stock_level
FROM products;
```

---

## 🔹 String Functions

```sql
-- Concatenate (SQLite uses ||)
SELECT first_name || ' ' || last_name as full_name FROM employees;

-- Upper / Lower
SELECT UPPER(first_name), LOWER(email) FROM employees;

-- Length
SELECT product_name, LENGTH(product_name) FROM products;

-- Substring
SELECT SUBSTR(email, 1, 5) FROM customers;

-- Trim
SELECT TRIM('  hello  ');
```

---

## 🔹 Date Functions (SQLite)

```sql
-- Current date
SELECT DATE('now');

-- Extract parts
SELECT 
    order_date,
    strftime('%Y', order_date) as year,
    strftime('%m', order_date) as month,
    strftime('%d', order_date) as day
FROM orders;

-- Date arithmetic
SELECT DATE('now', '-7 days');
SELECT DATE('now', '+1 month');
```

---

## 🔹 Data Modification

```sql
-- INSERT
INSERT INTO table_name (col1, col2) VALUES (val1, val2);
INSERT INTO table_name VALUES (val1, val2, val3);

-- UPDATE
UPDATE employees SET salary = 80000 WHERE employee_id = 1;
UPDATE products SET stock_quantity = stock_quantity - 10 WHERE product_id = 5;

-- DELETE
DELETE FROM orders WHERE status = 'Cancelled';
DELETE FROM customers WHERE customer_id = 10;
```

---

## 🔹 Table Operations

```sql
-- CREATE TABLE
CREATE TABLE new_table (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    value DECIMAL(10,2),
    created_at DATE DEFAULT CURRENT_DATE
);

-- ALTER TABLE
ALTER TABLE table_name ADD COLUMN new_column TEXT;
ALTER TABLE table_name RENAME TO new_name;

-- DROP TABLE
DROP TABLE IF EXISTS table_name;
```

---

## 🔹 Quick Reference

| Clause | Purpose |
|--------|---------|
| `SELECT` | Choose columns |
| `FROM` | Specify table |
| `WHERE` | Filter rows |
| `GROUP BY` | Group rows |
| `HAVING` | Filter groups |
| `ORDER BY` | Sort results |
| `LIMIT` | Limit rows returned |

### Execution Order
1. FROM & JOINs
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT

---

## 🔹 SQLite Tips

```sql
-- Show all tables
.tables

-- Show table schema
.schema table_name

-- Format output
.mode column
.headers on

-- Exit
.quit
```
