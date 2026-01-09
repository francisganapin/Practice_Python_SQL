# SQL Cheatsheet 📋

Quick reference guide with real estate database examples.

---

## 📌 Basic SELECT

```sql
-- Select all columns
SELECT * FROM Properties;

-- Select specific columns
SELECT address, city, price FROM Properties;

-- With alias
SELECT address AS property_address, price AS listing_price FROM Properties;
```

---

## 📌 WHERE Clause (Filtering)

```sql
-- Equals
SELECT * FROM Properties WHERE status = 'available';

-- Not equals
SELECT * FROM Properties WHERE property_type != 'apartment';

-- Greater/Less than
SELECT * FROM Properties WHERE price > 500000;
SELECT * FROM Properties WHERE bedrooms <= 3;

-- BETWEEN
SELECT * FROM Properties WHERE price BETWEEN 300000 AND 600000;

-- IN (multiple values)
SELECT * FROM Properties WHERE city IN ('Miami', 'Orlando', 'Tampa');

-- LIKE (pattern matching)
SELECT * FROM Properties WHERE address LIKE '%Oak%';    -- contains 'Oak'
SELECT * FROM Properties WHERE city LIKE 'San%';        -- starts with 'San'

-- NULL check
SELECT * FROM Properties WHERE agent_id IS NULL;
SELECT * FROM Properties WHERE agent_id IS NOT NULL;

-- AND / OR
SELECT * FROM Properties 
WHERE price > 400000 AND bedrooms >= 3;

SELECT * FROM Properties 
WHERE city = 'Miami' OR city = 'Orlando';
```

---

## 📌 ORDER BY (Sorting)

```sql
-- Ascending (default)
SELECT * FROM Properties ORDER BY price;

-- Descending
SELECT * FROM Properties ORDER BY price DESC;

-- Multiple columns
SELECT * FROM Properties ORDER BY city ASC, price DESC;
```

---

## 📌 LIMIT

```sql
-- Top 10 results
SELECT * FROM Properties ORDER BY price DESC LIMIT 10;

-- Skip first 5, get next 10
SELECT * FROM Properties LIMIT 10 OFFSET 5;
```

---

## 📌 Aggregate Functions

| Function | Description | Example |
|----------|-------------|---------|
| `COUNT()` | Count rows | `SELECT COUNT(*) FROM Properties;` |
| `SUM()` | Sum values | `SELECT SUM(sale_price) FROM Transactions;` |
| `AVG()` | Average | `SELECT AVG(price) FROM Properties;` |
| `MIN()` | Minimum | `SELECT MIN(price) FROM Properties;` |
| `MAX()` | Maximum | `SELECT MAX(price) FROM Properties;` |

```sql
-- Examples
SELECT 
    COUNT(*) AS total_properties,
    AVG(price) AS avg_price,
    MIN(price) AS cheapest,
    MAX(price) AS most_expensive
FROM Properties;
```

---

## 📌 GROUP BY

```sql
-- Count properties by city
SELECT city, COUNT(*) AS property_count
FROM Properties
GROUP BY city;

-- Average price by property type
SELECT property_type, AVG(price) AS avg_price
FROM Properties
GROUP BY property_type;

-- Total sales by agent
SELECT agent_id, SUM(sale_price) AS total_sales
FROM Transactions
GROUP BY agent_id;
```

---

## 📌 HAVING (Filter After GROUP BY)

```sql
-- Cities with more than 5 properties
SELECT city, COUNT(*) AS count
FROM Properties
GROUP BY city
HAVING COUNT(*) > 5;

-- Agents with total sales > $1 million
SELECT agent_id, SUM(sale_price) AS total_sales
FROM Transactions
GROUP BY agent_id
HAVING SUM(sale_price) > 1000000;
```

---

## 📌 JOINs

### INNER JOIN
Returns only matching rows from both tables

```sql
SELECT p.address, a.first_name, a.last_name
FROM Properties p
INNER JOIN Agents a ON p.agent_id = a.agent_id;
```

### LEFT JOIN
Returns all rows from left table + matching from right

```sql
SELECT p.address, a.first_name
FROM Properties p
LEFT JOIN Agents a ON p.agent_id = a.agent_id;
```

### Multiple Joins
```sql
SELECT 
    t.transaction_id,
    p.address,
    a.first_name AS agent,
    b.first_name AS buyer
FROM Transactions t
JOIN Properties p ON t.property_id = p.property_id
JOIN Agents a ON t.agent_id = a.agent_id
JOIN Clients b ON t.buyer_id = b.client_id;
```

---

## 📌 Subqueries

```sql
-- Properties above average price
SELECT * FROM Properties
WHERE price > (SELECT AVG(price) FROM Properties);

-- Agents with no transactions
SELECT * FROM Agents
WHERE agent_id NOT IN (SELECT agent_id FROM Transactions);

-- Properties with highest price in each city
SELECT * FROM Properties p1
WHERE price = (
    SELECT MAX(price) FROM Properties p2 
    WHERE p1.city = p2.city
);
```

---

## 📌 CASE WHEN

```sql
SELECT 
    address,
    price,
    CASE 
        WHEN price < 300000 THEN 'Budget'
        WHEN price < 700000 THEN 'Mid-Range'
        ELSE 'Luxury'
    END AS category
FROM Properties;
```

---

## 📌 String Functions

```sql
-- Concatenate
SELECT first_name || ' ' || last_name AS full_name FROM Agents;

-- Upper/Lower case
SELECT UPPER(city), LOWER(email) FROM Properties, Clients;

-- Length
SELECT address, LENGTH(address) AS address_length FROM Properties;
```

---

## 📌 Date Functions (SQLite)

```sql
-- Current date
SELECT DATE('now');

-- Extract year/month
SELECT strftime('%Y', sale_date) AS year FROM Transactions;
SELECT strftime('%m', sale_date) AS month FROM Transactions;

-- Date formatting
SELECT strftime('%Y-%m', listing_date) AS year_month FROM Properties;
```

---

## 📌 COALESCE & NULLIF

```sql
-- Replace NULL with default
SELECT COALESCE(phone, 'No Phone') FROM Clients;

-- Return NULL if values equal
SELECT NULLIF(status, 'pending') FROM Properties;
```

---

## 📌 DISTINCT

```sql
-- Unique values
SELECT DISTINCT city FROM Properties;
SELECT DISTINCT property_type, status FROM Properties;
```

---

## 📌 ROUND

```sql
SELECT ROUND(AVG(price), 2) AS avg_price FROM Properties;
SELECT ROUND(price / sqft, 2) AS price_per_sqft FROM Properties;
```

---

## 📌 Common Query Patterns

### Top N by Category
```sql
-- Top 3 most expensive properties per city
SELECT * FROM Properties p1
WHERE (
    SELECT COUNT(*) FROM Properties p2
    WHERE p2.city = p1.city AND p2.price > p1.price
) < 3
ORDER BY city, price DESC;
```

### Running Total
```sql
SELECT 
    sale_date,
    sale_price,
    SUM(sale_price) OVER (ORDER BY sale_date) AS running_total
FROM Transactions;
```

### Ranking
```sql
SELECT 
    address,
    price,
    RANK() OVER (ORDER BY price DESC) AS price_rank
FROM Properties;
```

---

## 📌 Quick Reference Table

| Task | Syntax |
|------|--------|
| All rows | `SELECT * FROM table;` |
| Filter | `WHERE condition` |
| Sort | `ORDER BY column DESC` |
| Limit | `LIMIT n` |
| Count | `COUNT(*)` |
| Sum | `SUM(column)` |
| Average | `AVG(column)` |
| Group | `GROUP BY column` |
| Filter groups | `HAVING condition` |
| Join tables | `JOIN table ON condition` |
| Find NULL | `IS NULL` / `IS NOT NULL` |
| Pattern match | `LIKE '%pattern%'` |
| In list | `IN ('a', 'b', 'c')` |
| Unique | `DISTINCT column` |

---

**Happy querying! 🚀**
