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
SELECT * FROM foods WHERE calories > 150;

-- Multiple conditions
SELECT * FROM foods WHERE calories > 100 AND protein_g > 10;
SELECT * FROM foods WHERE category = 'Fruits' OR category = 'Vegetables';

-- NULL check
SELECT * FROM foods WHERE fiber_g IS NULL;
SELECT * FROM foods WHERE fiber_g IS NOT NULL;

-- IN operator
SELECT * FROM users WHERE goal IN ('Weight Loss', 'Muscle Gain');

-- BETWEEN (inclusive)
SELECT * FROM foods WHERE calories BETWEEN 100 AND 200;

-- LIKE patterns
SELECT * FROM foods WHERE food_name LIKE '%Chicken%';  -- contains
SELECT * FROM foods WHERE food_name LIKE 'G%';         -- starts with
```

---

## 🔹 Sorting & Limiting

```sql
-- Order by ascending (default)
SELECT * FROM foods ORDER BY calories;

-- Order descending
SELECT * FROM foods ORDER BY protein_g DESC;

-- Multiple columns
SELECT * FROM foods ORDER BY category, calories DESC;

-- Limit results
SELECT * FROM foods ORDER BY protein_g DESC LIMIT 5;
```

---

## 🔹 Aggregate Functions

```sql
-- Count rows
SELECT COUNT(*) FROM users;
SELECT COUNT(DISTINCT category) FROM foods;

-- Sum values
SELECT SUM(calories) FROM foods;

-- Average
SELECT AVG(protein_g) FROM foods;
SELECT ROUND(AVG(calories), 2) FROM foods;

-- Min / Max
SELECT MIN(calories), MAX(calories) FROM foods;
```

---

## 🔹 GROUP BY & HAVING

```sql
-- Group by column
SELECT category, COUNT(*) 
FROM foods 
GROUP BY category;

-- Multiple aggregations
SELECT 
    category,
    COUNT(*) as count,
    AVG(calories) as avg_cal,
    SUM(protein_g) as total_protein
FROM foods 
GROUP BY category;

-- HAVING (filter groups)
SELECT category, AVG(calories) as avg_cal
FROM foods
GROUP BY category
HAVING AVG(calories) > 100;
```

---

## 🔹 JOINs

```sql
-- INNER JOIN (matching rows only)
SELECT u.username, m.meal_type, m.meal_date
FROM users u
INNER JOIN meals m ON u.user_id = m.user_id;

-- LEFT JOIN (all from left table)
SELECT u.username, m.meal_id
FROM users u
LEFT JOIN meals m ON u.user_id = m.user_id;

-- Multiple JOINs
SELECT 
    u.username,
    m.meal_type,
    f.food_name
FROM users u
JOIN meals m ON u.user_id = m.user_id
JOIN meal_items mi ON m.meal_id = mi.meal_id
JOIN foods f ON mi.food_id = f.food_id;
```

---

## 🔹 Subqueries

```sql
-- Subquery in WHERE
SELECT * FROM foods
WHERE calories > (SELECT AVG(calories) FROM foods);

-- Subquery with IN
SELECT * FROM users
WHERE user_id IN (
    SELECT user_id FROM meals WHERE meal_date = '2024-10-01'
);

-- EXISTS
SELECT * FROM users u
WHERE EXISTS (
    SELECT 1 FROM meals m WHERE m.user_id = u.user_id
);
```

---

## 🔹 CASE Statements

```sql
SELECT 
    food_name,
    calories,
    CASE 
        WHEN calories < 100 THEN 'Low Calorie'
        WHEN calories <= 200 THEN 'Moderate'
        ELSE 'High Calorie'
    END as calorie_level
FROM foods;
```

---

## 🔹 String Functions

```sql
-- Concatenate (SQLite)
SELECT first_name || ' ' || last_name FROM users;

-- Upper / Lower
SELECT UPPER(food_name) FROM foods;

-- Length
SELECT food_name, LENGTH(food_name) FROM foods;
```

---

## 🔹 Math with Columns

```sql
-- Multiply columns
SELECT food_name, calories * 2 as double_serving FROM foods;

-- Calculate totals with quantity
SELECT SUM(f.calories * mi.quantity) as total_cal
FROM meal_items mi
JOIN foods f ON mi.food_id = f.food_id;
```

---

## Quick Reference

| Clause | Purpose |
|--------|---------|
| `SELECT` | Choose columns |
| `FROM` | Specify table |
| `JOIN` | Combine tables |
| `WHERE` | Filter rows |
| `GROUP BY` | Group rows |
| `HAVING` | Filter groups |
| `ORDER BY` | Sort results |
| `LIMIT` | Limit rows |

### Execution Order
```
1. FROM & JOINs
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT
```
