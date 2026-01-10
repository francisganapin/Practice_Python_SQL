# SQL Practice Problems 🎯

## Database Schema Overview

| Table | Description |
|-------|-------------|
| `employees` | Employee info with salary, department, and manager |
| `departments` | Department names, locations, and budgets |
| `products` | Product catalog with prices and stock |
| `suppliers` | Supplier contact information |
| `customers` | Customer details and registration dates |
| `orders` | Order header with status and totals |
| `order_items` | Individual items within each order |

---

## 🟢 EASY (Problems 1-5)

### Problem 1: Basic SELECT
**Task:** Retrieve all columns from the `employees` table.

<details>
<summary>💡 Hint</summary>
Use SELECT * to get all columns
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM employees;
```
</details>

---

### Problem 2: Filtering with WHERE
**Task:** Find all products in the 'Electronics' category.

<details>
<summary>💡 Hint</summary>
Use WHERE to filter by category column
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM products
WHERE category = 'Electronics';
```
</details>

---

### Problem 3: Sorting Results
**Task:** List all employees ordered by salary from highest to lowest.

<details>
<summary>💡 Hint</summary>
Use ORDER BY with DESC for descending order
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT first_name, last_name, salary
FROM employees
ORDER BY salary DESC;
```
</details>

---

### Problem 4: Using LIKE Pattern
**Task:** Find all customers whose email contains 'email.com'.

<details>
<summary>💡 Hint</summary>
Use LIKE with % wildcards
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM customers
WHERE email LIKE '%email.com%';
```
</details>

---

### Problem 5: COUNT and Basic Aggregation
**Task:** Count how many employees work in each department.

<details>
<summary>💡 Hint</summary>
Use COUNT() with GROUP BY
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT department_id, COUNT(*) as employee_count
FROM employees
GROUP BY department_id;
```
</details>

---

## 🟡 MEDIUM (Problems 6-10)

### Problem 6: INNER JOIN
**Task:** List all employees with their department names.

<details>
<summary>💡 Hint</summary>
Join employees with departments on department_id
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```
</details>

---

### Problem 7: Multiple Aggregations
**Task:** Find the minimum, maximum, and average salary for each department.

<details>
<summary>💡 Hint</summary>
Use MIN(), MAX(), AVG() with GROUP BY
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    d.department_name,
    MIN(e.salary) as min_salary,
    MAX(e.salary) as max_salary,
    ROUND(AVG(e.salary), 2) as avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY d.department_name;
```
</details>

---

### Problem 8: HAVING Clause
**Task:** Find categories with more than 3 products.

<details>
<summary>💡 Hint</summary>
Use GROUP BY with HAVING to filter groups
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT category, COUNT(*) as product_count
FROM products
GROUP BY category
HAVING COUNT(*) > 3;
```
</details>

---

### Problem 9: Subquery in WHERE
**Task:** Find all employees who earn more than the company average salary.

<details>
<summary>💡 Hint</summary>
Use a subquery to calculate the average, then compare
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
</details>

---

### Problem 10: LEFT JOIN
**Task:** List all departments and count of employees (including departments with no employees).

<details>
<summary>💡 Hint</summary>
Use LEFT JOIN to include all departments
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    d.department_name,
    COUNT(e.employee_id) as employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
```
</details>

---

## 🔴 CHALLENGING (Problems 11-15)

### Problem 11: Multiple JOINs
**Task:** List all orders with customer name, employee name who processed it, and total amount.

<details>
<summary>💡 Hint</summary>
Join orders with both customers and employees tables
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    o.order_id,
    c.first_name || ' ' || c.last_name as customer_name,
    e.first_name || ' ' || e.last_name as employee_name,
    o.order_date,
    o.total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN employees e ON o.employee_id = e.employee_id
ORDER BY o.order_date;
```
</details>

---

### Problem 12: Complex Aggregation with JOINs
**Task:** Find the total revenue generated per product (quantity × unit_price from order_items).

<details>
<summary>💡 Hint</summary>
Join products with order_items, then aggregate with SUM
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    p.product_name,
    SUM(oi.quantity * oi.unit_price) as total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;
```
</details>

---

### Problem 13: Correlated Subquery
**Task:** Find employees who earn more than the average salary in their own department.

<details>
<summary>💡 Hint</summary>
Use a correlated subquery that references the outer query's department
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT e1.first_name, e1.last_name, e1.salary, e1.department_id
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```
</details>

---

### Problem 14: CASE Statement
**Task:** Categorize products by stock level: 'Low' (< 50), 'Medium' (50-100), 'High' (> 100).

<details>
<summary>💡 Hint</summary>
Use CASE WHEN for conditional logic
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    product_name,
    stock_quantity,
    CASE 
        WHEN stock_quantity < 50 THEN 'Low'
        WHEN stock_quantity <= 100 THEN 'Medium'
        ELSE 'High'
    END as stock_level
FROM products
ORDER BY stock_quantity;
```
</details>

---

### Problem 15: Complex Report Query
**Task:** Create a sales report showing each employee's name, department, total orders processed, and total sales amount. Only include employees who have processed at least 1 order.

<details>
<summary>💡 Hint</summary>
Join employees, departments, and orders. Use GROUP BY and aggregations.
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    e.first_name || ' ' || e.last_name as employee_name,
    d.department_name,
    COUNT(o.order_id) as orders_processed,
    SUM(o.total_amount) as total_sales
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name, d.department_name
HAVING COUNT(o.order_id) >= 1
ORDER BY total_sales DESC;
```
</details>

---

## 🚀 Bonus Challenge

**Task:** Find the top 3 best-selling products by total quantity sold.

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    p.product_name,
    SUM(oi.quantity) as total_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 3;
```
</details>

---

## How to Practice

1. Run `python setup_database.py` to create the database
2. Open SQLite with: `sqlite3 practice.db`
3. Try each problem before looking at the solution!
4. Use `.schema` to see table structures
5. Use `.tables` to list all tables
