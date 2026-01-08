# Easy SQL Tutorial - Real Estate Database 🏠

## Setup Instructions

First, create your database and tables:

```sql
-- Create tables
CREATE TABLE properties (
    property_id INTEGER PRIMARY KEY,
    address TEXT,
    city TEXT,
    bedrooms INTEGER,
    bathrooms REAL,
    price REAL,
    status TEXT
);

CREATE TABLE agents (
    agent_id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT
);

-- Insert sample data
INSERT INTO properties VALUES
(1, '123 Oak St', 'Austin', 3, 2.0, 450000, 'Available'),
(2, '456 Maple Ave', 'Austin', 2, 2.0, 320000, 'Sold'),
(3, '789 Pine Rd', 'Houston', 4, 3.0, 550000, 'Available'),
(4, '321 Elm St', 'Dallas', 3, 2.5, 380000, 'Pending'),
(5, '654 Cedar Ln', 'Austin', 5, 4.0, 750000, 'Available'),
(6, '987 Birch Ct', 'Houston', 2, 1.0, 210000, 'Sold'),
(7, '147 Willow Way', 'Dallas', 4, 3.5, 620000, 'Available'),
(8, '258 Spruce Dr', 'Austin', 1, 1.0, 180000, 'Available');

INSERT INTO agents VALUES
(1, 'Sarah Johnson', '555-0101'),
(2, 'Michael Chen', '555-0102'),
(3, 'Emily Rodriguez', '555-0103');
```

---

## Problem 1: Show All Properties ⭐

**Task:** Display all information from the properties table.

**Hint:** Use `SELECT *` to get all columns.

<details>
<summary>Click to see solution</summary>

```sql
SELECT * FROM properties;
```

**What you'll see:** All 8 properties with all their details.

</details>

---

## Problem 2: Show Only Addresses ⭐

**Task:** Display only the addresses of all properties.

**Hint:** Instead of `*`, write the column name you want.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address FROM properties;
```

**Result:** Just a list of addresses.

</details>

---

## Problem 3: Show Address and Price ⭐

**Task:** Display the address and price of all properties.

**Hint:** Separate column names with commas.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, price FROM properties;
```

</details>

---

## Problem 4: Find Available Properties ⭐

**Task:** Show all properties where status is 'Available'.

**Hint:** Use `WHERE status = 'Available'`

<details>
<summary>Click to see solution</summary>

```sql
SELECT * FROM properties
WHERE status = 'Available';
```

**Result:** You should see 5 available properties.

</details>

---

## Problem 5: Find Properties in Austin ⭐

**Task:** Show address and price for properties in Austin only.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, price FROM properties
WHERE city = 'Austin';
```

**Result:** 4 properties in Austin.

</details>

---

## Problem 6: Find Affordable Properties ⭐⭐

**Task:** Show properties with price less than $400,000.

**Hint:** Use `WHERE price < 400000`

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, city, price FROM properties
WHERE price < 400000;
```

</details>

---

## Problem 7: Find 3-Bedroom Homes ⭐⭐

**Task:** Show all properties that have exactly 3 bedrooms.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, bedrooms, price FROM properties
WHERE bedrooms = 3;
```

</details>

---

## Problem 8: Sort by Price (Cheapest First) ⭐⭐

**Task:** Show all properties sorted from cheapest to most expensive.

**Hint:** Use `ORDER BY price`

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, price FROM properties
ORDER BY price;
```

**Note:** Default sorting is ascending (low to high).

</details>

---

## Problem 9: Sort by Price (Most Expensive First) ⭐⭐

**Task:** Show all properties sorted from most expensive to cheapest.

**Hint:** Add `DESC` after the column name.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, price FROM properties
ORDER BY price DESC;
```

</details>

---

## Problem 10: Multiple Conditions (AND) ⭐⭐

**Task:** Find available properties in Austin.

**Hint:** Use `WHERE city = 'Austin' AND status = 'Available'`

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, price FROM properties
WHERE city = 'Austin' AND status = 'Available';
```

**Result:** 3 available properties in Austin.

</details>

---

## Problem 11: Multiple Conditions (OR) ⭐⭐

**Task:** Find properties in either Austin OR Houston.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, city, price FROM properties
WHERE city = 'Austin' OR city = 'Houston';
```

</details>

---

## Problem 12: Count Properties ⭐⭐

**Task:** How many total properties are in the database?

**Hint:** Use `COUNT(*)`

<details>
<summary>Click to see solution</summary>

```sql
SELECT COUNT(*) FROM properties;
```

**Result:** 8

</details>

---

## Problem 13: Count Available Properties ⭐⭐

**Task:** How many properties are available?

<details>
<summary>Click to see solution</summary>

```sql
SELECT COUNT(*) FROM properties
WHERE status = 'Available';
```

**Result:** 5

</details>

---

## Problem 14: Find Average Price ⭐⭐⭐

**Task:** What is the average price of all properties?

**Hint:** Use `AVG(price)`

<details>
<summary>Click to see solution</summary>

```sql
SELECT AVG(price) FROM properties;
```

**Result:** Around 432,500

</details>

---

## Problem 15: Find Highest and Lowest Price ⭐⭐⭐

**Task:** Show the most expensive and cheapest property prices.

**Hint:** Use `MAX(price)` and `MIN(price)`

<details>
<summary>Click to see solution</summary>

```sql
SELECT 
    MAX(price) AS highest_price,
    MIN(price) AS lowest_price
FROM properties;
```

**Result:** Highest: 750,000, Lowest: 180,000

</details>

---

## Problem 16: Count Properties by City ⭐⭐⭐

**Task:** How many properties are in each city?

**Hint:** Use `GROUP BY city` with `COUNT(*)`

<details>
<summary>Click to see solution</summary>

```sql
SELECT city, COUNT(*) AS property_count
FROM properties
GROUP BY city;
```

**Result:** 
- Austin: 4 properties
- Houston: 2 properties
- Dallas: 2 properties

**What's happening:** `GROUP BY` groups rows with the same city together, then `COUNT(*)` counts each group.

</details>

---

## Problem 17: Average Price by City ⭐⭐⭐

**Task:** What is the average property price in each city?

<details>
<summary>Click to see solution</summary>

```sql
SELECT city, AVG(price) AS avg_price
FROM properties
GROUP BY city
ORDER BY avg_price DESC;
```

**Result:** Shows each city with its average property price, sorted from highest to lowest.

</details>

---

## Problem 18: Find Properties in Price Range ⭐⭐

**Task:** Show properties priced between $300,000 and $500,000.

**Hint:** Use `BETWEEN`

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, price FROM properties
WHERE price BETWEEN 300000 AND 500000;
```

**Note:** `BETWEEN` includes both the start and end values (300,000 and 500,000 are included).

</details>

---

## Problem 19: Find Properties in Multiple Cities ⭐⭐

**Task:** Show properties in Austin, Dallas, or Houston using the `IN` operator.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, city, price FROM properties
WHERE city IN ('Austin', 'Dallas', 'Houston');
```

**Why use IN?** It's cleaner than writing `city = 'Austin' OR city = 'Dallas' OR city = 'Houston'`

</details>

---

## Problem 20: Search for Addresses with "Oak" ⭐⭐⭐

**Task:** Find all properties where the address contains the word "Oak".

**Hint:** Use `LIKE '%Oak%'`

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, city FROM properties
WHERE address LIKE '%Oak%';
```

**What's %?** It's a wildcard that matches any characters.
- `%Oak%` = Oak anywhere in the text
- `Oak%` = Starts with Oak
- `%Oak` = Ends with Oak

</details>

---

## Problem 21: Total Value of All Properties ⭐⭐

**Task:** Calculate the total value of all properties combined.

**Hint:** Use `SUM(price)`

<details>
<summary>Click to see solution</summary>

```sql
SELECT SUM(price) AS total_value
FROM properties;
```

**Result:** $3,460,000 (sum of all property prices)

</details>

---

## Problem 22: Properties with More Than 2 Bedrooms ⭐⭐

**Task:** Show all properties that have more than 2 bedrooms, sorted by number of bedrooms.

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, bedrooms, price FROM properties
WHERE bedrooms > 2
ORDER BY bedrooms DESC;
```

</details>

---

## Problem 23: Expensive Available Properties ⭐⭐⭐

**Task:** Find available properties priced above the average price.

**Hint:** You'll need to use a subquery with `AVG(price)`

<details>
<summary>Click to see solution</summary>

```sql
SELECT address, price FROM properties
WHERE status = 'Available' 
  AND price > (SELECT AVG(price) FROM properties);
```

**What's a subquery?** The `(SELECT AVG(price) FROM properties)` runs first, calculates the average, then the outer query uses that value.

</details>

---

## Problem 24: Count Properties by Status ⭐⭐⭐

**Task:** How many properties are in each status (Available, Sold, Pending)?

<details>
<summary>Click to see solution</summary>

```sql
SELECT status, COUNT(*) AS count
FROM properties
GROUP BY status
ORDER BY count DESC;
```

**Result:**
- Available: 5
- Sold: 2
- Pending: 1

</details>

---

## Problem 25: Most Expensive Property in Each City ⭐⭐⭐⭐

**Task:** Show the highest-priced property in each city.

**Hint:** Use `GROUP BY city` with `MAX(price)`

<details>
<summary>Click to see solution</summary>

```sql
SELECT city, MAX(price) AS highest_price
FROM properties
GROUP BY city
ORDER BY highest_price DESC;
```

**Result:** Shows each city with its most expensive property price.

**Challenge:** Can you also show the address of that property? (This requires a more advanced query!)

</details>

---

## Quick Reference Card 📝

### Basic Commands
```sql
-- Show everything
SELECT * FROM table_name;

-- Show specific columns
SELECT column1, column2 FROM table_name;

-- Filter results
SELECT * FROM table_name WHERE condition;

-- Sort results
SELECT * FROM table_name ORDER BY column_name;
SELECT * FROM table_name ORDER BY column_name DESC;
```

### Common Conditions
```sql
WHERE price = 500000          -- Exactly equal
WHERE price < 500000          -- Less than
WHERE price > 500000          -- Greater than
WHERE price <= 500000         -- Less than or equal
WHERE price >= 500000         -- Greater than or equal
WHERE city = 'Austin'         -- Text comparison
WHERE status != 'Sold'        -- Not equal
```

### Combining Conditions
```sql
WHERE city = 'Austin' AND price < 500000    -- Both must be true
WHERE city = 'Austin' OR city = 'Dallas'    -- Either can be true
```

### Aggregate Functions
```sql
COUNT(*)        -- Count rows
AVG(price)      -- Average value
MAX(price)      -- Highest value
MIN(price)      -- Lowest value
SUM(price)      -- Total sum
```

---

## Practice Tips 💡

1. **Start from Problem 1** and work your way down
2. **Try to solve each problem yourself** before looking at the solution
3. **Type the queries yourself** - don't copy/paste
4. **Experiment!** Try changing the queries to see what happens
5. **If you get an error**, read it carefully - it usually tells you what's wrong

---

## Next Steps 🚀

Once you're comfortable with these 15 problems:
- Try combining multiple conditions
- Practice with different sorting orders
- Create your own questions and solve them
- Move on to JOIN operations (combining tables)

**Good luck! You've got this! 💪**
