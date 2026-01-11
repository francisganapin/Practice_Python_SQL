# SQL Practice - Real Estate Database

## Quick Cheatsheet

### SELECT & WHERE
```sql
SELECT * FROM agents;                           -- all columns
SELECT first_name, last_name FROM agents;       -- specific columns
SELECT * FROM properties WHERE list_price > 500000;
SELECT * FROM properties WHERE city = 'Phoenix' OR city = 'Denver';
SELECT * FROM properties WHERE city IN ('Los Angeles', 'San Diego');
```

### Aggregate Functions
```sql
COUNT(*)           -- count rows
SUM(sale_price)    -- total
AVG(list_price)    -- average
MIN(list_price)    -- minimum
MAX(list_price)    -- maximum
ROUND(AVG(x), 2)   -- round to 2 decimals
```

### GROUP BY & HAVING
```sql
SELECT city, COUNT(*) FROM properties GROUP BY city;
SELECT city, COUNT(*) FROM properties GROUP BY city HAVING COUNT(*) > 2;
```

### JOINs
```sql
-- INNER JOIN (only matches)
SELECT p.address, a.first_name
FROM properties p
JOIN agents a ON p.agent_id = a.agent_id;

-- LEFT JOIN (all from left + matches from right)
SELECT a.first_name, t.sale_price
FROM agents a
LEFT JOIN transactions t ON a.agent_id = t.agent_id;
```

### Date Functions (SQLite)
```sql
strftime('%Y-%m', sale_date)    -- Format as '2024-03'
strftime('%Y', sale_date)       -- Extract year
```

### Window Functions
```sql
RANK() OVER (ORDER BY sale_price DESC)              -- rank all
RANK() OVER (PARTITION BY city ORDER BY price DESC) -- rank per city
```

### Useful Extras
```sql
first_name || ' ' || last_name AS full_name   -- concatenate strings
COALESCE(value, 0)                            -- replace NULL with 0
ORDER BY list_price DESC                      -- sort descending
LIMIT 5                                       -- top 5 results
```

---

## 5 Practice Problems

### Problem 1: Agent Sales Summary
Find total sales and number of transactions per agent. Show agent name, total sales, and transaction count. Only include agents with at least 1 sale.

**Hint:** JOIN agents → transactions, GROUP BY agent, use SUM and COUNT

---

### Problem 2: City Price Analysis
Find the average list price for each city. Show city, average price (rounded to 2 decimals), and property count. Order by average price descending.

**Hint:** GROUP BY city, use AVG and ROUND

---

### Problem 3: Top Agent Per Office
Find the agent with highest total sales in each office. Show office name, agent name, and their total sales.

**Hint:** Use window function with PARTITION BY office_id

---

### Problem 4: Monthly Sales Report
Group transactions by month. Show month (as 'YYYY-MM'), transaction count, and total sales. Order by month.

**Hint:** Use strftime('%Y-%m', sale_date), GROUP BY

---

### Problem 5: Price Difference
For sold properties, show address, list price, sale price, and the difference (list - sale). Order by difference descending.

**Hint:** JOIN properties → transactions, calculate difference

---

## How to Practice

```python
import sqlite3

conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

query = """
    YOUR SQL HERE
"""

cursor.execute(query)
for row in cursor.fetchall():
    print(row)

conn.close()
```

Good luck! 🏠
