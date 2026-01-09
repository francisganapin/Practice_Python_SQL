# Real Estate SQL Practice Questions 🏠

## Database Schema Overview

```
Agents (agent_id, first_name, last_name, email, phone, hire_date, commission_rate)
Clients (client_id, first_name, last_name, email, phone, client_type)
Properties (property_id, address, city, state, zip_code, price, bedrooms, bathrooms, sqft, year_built, property_type, status, listing_date, agent_id)
Transactions (transaction_id, property_id, agent_id, buyer_id, seller_id, sale_price, sale_date, commission)
Showings (showing_id, property_id, agent_id, client_id, showing_date, feedback, rating)
```

---

# 🟢 EASY QUESTIONS (1-15)

## Question 1: Select All Properties
**Display all columns from the Properties table.**

<details>
<summary>💡 Hint</summary>
Use SELECT * to get all columns
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties;
```
</details>

---

## Question 2: Agent Names
**List only the first and last names of all agents.**

<details>
<summary>💡 Hint</summary>
Specify column names after SELECT
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT first_name, last_name FROM Agents;
```
</details>

---

## Question 3: Expensive Properties
**Find all properties with a price greater than $500,000.**

<details>
<summary>💡 Hint</summary>
Use WHERE with a comparison operator
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties WHERE price > 500000;
```
</details>

---

## Question 4: Available Properties
**List all properties that are currently available for sale.**

<details>
<summary>💡 Hint</summary>
Filter by status = 'available'
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties WHERE status = 'available';
```
</details>

---

## Question 5: Count Clients
**How many clients are in the database?**

<details>
<summary>💡 Hint</summary>
Use the COUNT() function
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT COUNT(*) AS total_clients FROM Clients;
```
</details>

---

## Question 6: Sort by Price
**List all properties sorted by price from highest to lowest.**

<details>
<summary>💡 Hint</summary>
Use ORDER BY with DESC
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties ORDER BY price DESC;
```
</details>

---

## Question 7: Houses Only
**Find all properties that are houses (not condos, townhouses, or apartments).**

<details>
<summary>💡 Hint</summary>
Filter by property_type
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties WHERE property_type = 'house';
```
</details>

---

## Question 8: Top 5 Most Expensive
**Show the 5 most expensive properties.**

<details>
<summary>💡 Hint</summary>
Use ORDER BY and LIMIT
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties ORDER BY price DESC LIMIT 5;
```
</details>

---

## Question 9: Buyer Clients
**List all clients who are buyers.**

<details>
<summary>💡 Hint</summary>
Filter by client_type
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Clients WHERE client_type = 'buyer';
```
</details>

---

## Question 10: Properties in California
**Find all properties located in California (CA).**

<details>
<summary>💡 Hint</summary>
Filter by state column
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties WHERE state = 'CA';
```
</details>

---

## Question 11: Average Property Price
**Calculate the average price of all properties.**

<details>
<summary>💡 Hint</summary>
Use the AVG() function
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT AVG(price) AS average_price FROM Properties;
```
</details>

---

## Question 12: Properties with 3+ Bedrooms
**Find properties with 3 or more bedrooms.**

<details>
<summary>💡 Hint</summary>
Use >= comparison
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties WHERE bedrooms >= 3;
```
</details>

---

## Question 13: Recent Showings
**List all showings from 2025.**

<details>
<summary>💡 Hint</summary>
Use LIKE with a pattern or BETWEEN
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Showings WHERE showing_date LIKE '2025%';
```
</details>

---

## Question 14: Total Sales
**Find the total of all sale prices from transactions.**

<details>
<summary>💡 Hint</summary>
Use SUM() function
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT SUM(sale_price) AS total_sales FROM Transactions;
```
</details>

---

## Question 15: Unique Cities
**List all unique cities where properties are located.**

<details>
<summary>💡 Hint</summary>
Use DISTINCT keyword
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT DISTINCT city FROM Properties;
```
</details>

---

# 🟡 MEDIUM QUESTIONS (16-30)

## Question 16: Properties with Agent Info
**Show property address, city, price, and the agent's full name for each property.**

<details>
<summary>💡 Hint</summary>
JOIN Properties with Agents table
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    p.address, 
    p.city, 
    p.price,
    a.first_name || ' ' || a.last_name AS agent_name
FROM Properties p
JOIN Agents a ON p.agent_id = a.agent_id;
```
</details>

---

## Question 17: Count by Property Type
**Count how many properties exist for each property type.**

<details>
<summary>💡 Hint</summary>
Use GROUP BY with COUNT()
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    property_type, 
    COUNT(*) AS count
FROM Properties
GROUP BY property_type;
```
</details>

---

## Question 18: Average Price by City
**Calculate the average property price for each city.**

<details>
<summary>💡 Hint</summary>
Use GROUP BY with AVG()
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    city, 
    ROUND(AVG(price), 2) AS avg_price
FROM Properties
GROUP BY city
ORDER BY avg_price DESC;
```
</details>

---

## Question 19: Agent Sales Summary
**Show each agent's name and their total sales (sum of sale_price from transactions).**

<details>
<summary>💡 Hint</summary>
JOIN Agents with Transactions and use SUM()
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    a.first_name || ' ' || a.last_name AS agent_name,
    SUM(t.sale_price) AS total_sales
FROM Agents a
LEFT JOIN Transactions t ON a.agent_id = t.agent_id
GROUP BY a.agent_id
ORDER BY total_sales DESC;
```
</details>

---

## Question 20: Cities with High Average Price
**Find cities where the average property price is above $400,000.**

<details>
<summary>💡 Hint</summary>
Use HAVING after GROUP BY
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    city, 
    AVG(price) AS avg_price
FROM Properties
GROUP BY city
HAVING AVG(price) > 400000;
```
</details>

---

## Question 21: Transaction Details
**Show transaction details including property address, buyer name, seller name, and sale price.**

<details>
<summary>💡 Hint</summary>
Multiple JOINs - Clients table twice (for buyer and seller)
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    p.address,
    b.first_name || ' ' || b.last_name AS buyer_name,
    s.first_name || ' ' || s.last_name AS seller_name,
    t.sale_price,
    t.sale_date
FROM Transactions t
JOIN Properties p ON t.property_id = p.property_id
JOIN Clients b ON t.buyer_id = b.client_id
JOIN Clients s ON t.seller_id = s.client_id;
```
</details>

---

## Question 22: Properties Above Average
**Find all properties priced above the average price.**

<details>
<summary>💡 Hint</summary>
Use a subquery to calculate average
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT * FROM Properties
WHERE price > (SELECT AVG(price) FROM Properties);
```
</details>

---

## Question 23: Agent Showing Count
**Count how many showings each agent has conducted.**

<details>
<summary>💡 Hint</summary>
JOIN and GROUP BY
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    a.first_name || ' ' || a.last_name AS agent_name,
    COUNT(s.showing_id) AS showing_count
FROM Agents a
LEFT JOIN Showings s ON a.agent_id = s.agent_id
GROUP BY a.agent_id
ORDER BY showing_count DESC;
```
</details>

---

## Question 24: Price Categories
**Categorize properties as 'Budget' (< $300k), 'Mid-Range' ($300k-$700k), or 'Luxury' (> $700k).**

<details>
<summary>💡 Hint</summary>
Use CASE WHEN statement
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    address,
    city,
    price,
    CASE 
        WHEN price < 300000 THEN 'Budget'
        WHEN price BETWEEN 300000 AND 700000 THEN 'Mid-Range'
        ELSE 'Luxury'
    END AS price_category
FROM Properties;
```
</details>

---

## Question 25: Average Showing Rating by Property
**Calculate the average rating for each property from showings.**

<details>
<summary>💡 Hint</summary>
JOIN Properties with Showings and use GROUP BY
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    p.property_id,
    p.address,
    ROUND(AVG(s.rating), 2) AS avg_rating,
    COUNT(s.showing_id) AS showing_count
FROM Properties p
JOIN Showings s ON p.property_id = s.property_id
GROUP BY p.property_id
ORDER BY avg_rating DESC;
```
</details>

---

## Question 26: Top Earning Agents
**Find agents who earned more than $10,000 in commissions.**

<details>
<summary>💡 Hint</summary>
SUM commissions and use HAVING
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    a.first_name || ' ' || a.last_name AS agent_name,
    SUM(t.commission) AS total_commission
FROM Agents a
JOIN Transactions t ON a.agent_id = t.agent_id
GROUP BY a.agent_id
HAVING SUM(t.commission) > 10000
ORDER BY total_commission DESC;
```
</details>

---

## Question 27: Properties Without Showings
**Find properties that have never had a showing.**

<details>
<summary>💡 Hint</summary>
Use LEFT JOIN and check for NULL
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT p.* 
FROM Properties p
LEFT JOIN Showings s ON p.property_id = s.property_id
WHERE s.showing_id IS NULL;
```
</details>

---

## Question 28: Monthly Sales Summary
**Show total sales and count of transactions for each month.**

<details>
<summary>💡 Hint</summary>
Use strftime() to extract month from date
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    strftime('%Y-%m', sale_date) AS month,
    COUNT(*) AS transaction_count,
    SUM(sale_price) AS total_sales
FROM Transactions
GROUP BY strftime('%Y-%m', sale_date)
ORDER BY month;
```
</details>

---

## Question 29: Price per Square Foot
**Calculate price per square foot for each property and find the top 10 best value properties.**

<details>
<summary>💡 Hint</summary>
Divide price by sqft
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    address,
    city,
    price,
    sqft,
    ROUND(price * 1.0 / sqft, 2) AS price_per_sqft
FROM Properties
WHERE sqft > 0
ORDER BY price_per_sqft ASC
LIMIT 10;
```
</details>

---

## Question 30: Complete Property Report
**Create a comprehensive report: property details, agent name, number of showings, average rating, and sale status.**

<details>
<summary>💡 Hint</summary>
Multiple JOINs with subqueries or GROUP BY
</details>

<details>
<summary>✅ Solution</summary>

```sql
SELECT 
    p.address,
    p.city,
    p.price,
    p.status,
    a.first_name || ' ' || a.last_name AS agent_name,
    COALESCE(COUNT(s.showing_id), 0) AS total_showings,
    COALESCE(ROUND(AVG(s.rating), 1), 0) AS avg_rating
FROM Properties p
JOIN Agents a ON p.agent_id = a.agent_id
LEFT JOIN Showings s ON p.property_id = s.property_id
GROUP BY p.property_id
ORDER BY total_showings DESC;
```
</details>

---

## 🎯 Practice Tips

1. **Start simple** - Run each query step by step
2. **Read the error** - SQLite gives helpful error messages
3. **Use aliases** - Makes complex queries easier to read
4. **Test with LIMIT** - Add `LIMIT 5` when testing on large datasets
5. **Check your JOINs** - Make sure you're joining on the right columns

---

**Good luck with your SQL practice! 🚀**
