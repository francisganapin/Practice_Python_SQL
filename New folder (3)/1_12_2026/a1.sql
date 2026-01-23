-- INNER JOIN (only matching rows)
SELECT p.address, a.first_name, a.last_name
FROM properties p
INNER JOIN agents a ON p.agent_id = a.agent_id;

--## Problem 1: Agent Sales Performance

--Find the total sales amount for each agent (as seller) along with the number of properties they sold. 
--Include the agent's full name and their 
--office name. Only show agents who have made at least 2 sales. Order by total sales descending.

SELECT
      a.agent_id,
	  a.first_name,
	  a.last_name,
	  count(p.status = 'Sold') as sold_property,
	  sum(sale_price) as total_sales
FROM agents a
JOIN properties p
    ON a.agent_id = p.agent_id
JOIN transactions t
	ON t.property_id = p.property_id
WHERE p.status = 'Sold'
GROUP BY a.agent_id
Order BY total_sales DESC;

==--Find the total sales amount for each agent (as seller) along with the number of properties they sold. 
--Include the agent's full name and their 
--office name. Only show agents who have made at least 2 sales. Order by total sales descending.

SELECT
      a.agent_id,
	  a.first_name,
	  a.last_name,
	  count(p.status = 'Sold') as sold_property,
	  sum(sale_price) as total_sales,
	  count(*) as count_2
FROM agents a
JOIN properties p
    ON a.agent_id = p.agent_id
JOIN transactions t
	ON t.property_id = p.property_id
WHERE p.status = 'Sold'
GROUP BY a.agent_id
HAVING COUNT(*) = 2
Order BY total_sales DESC;


## Problem 2: Price Difference Analysis

--For each sold property, calculate the difference between the list price and sale price. 
--Show the property address, city, list price, sale price, the difference (list - sale), 
--and the percentage difference. Order by percentage difference descending.

SELECT 
    p.address,
	p.city,
	p.list_price,
	t.sale_price,
	(p.list_price - t.sale_price) as diff
from properties p 
join transactions t
     on t.property_id = p.property_id
WHERE p.status = 'Sold';


--## Office Performance Ranking

--Rank each office by their total transaction value 
--(sum of all sale prices where either buyer or seller agent belongs to that office). 
--Show office name, city, 
--total transaction value, and the rank. Use window functions for ranking.



SELECT 
    o.office_name,
    o.city,
    SUM(t.sale_price) AS total_transaction_value,
    RANK() OVER (ORDER BY SUM(t.sale_price) DESC) AS office_rank
FROM offices o
LEFT JOIN agents a ON o.office_id = a.office_id
LEFT JOIN transactions t ON a.agent_id = t.buyer_agent_id 
                         OR a.agent_id = t.seller_agent_id
GROUP BY o.office_id, o.office_name, o.city
ORDER BY office_rank;


## Problem 4: Average Days on Market by Property Type

--Calculate the average days on market for each property type. 
--Only include property types that have at least 2 sold properties. 
--Show the property type name and average days, rounded to 1 decimal place. Order by average days ascending.
--**Skills:** JOIN, GROUP BY, HAVING, AVG, ROUND, COUNT


SELECT 
	 pt.type_name,
	 round(avg(days_on_market),1) as average_days
FROM properties p 
JOIN transactions t
	on t.property_id = p.property_id
JOIN property_types pt
	on pt.type_id = p.type_id
GROUP BY type_name
ORDER BY average_days DESC;


--##  Properties Above City Average

--Find all properties where the list price is above the average list price for their respective city. 
--Show the property address, city, list price, and how much above the city average it is.

SELECT property_id,address,city,list_price
FROM properties
WHERE list_price > (
    SELECT AVG(list_price)
    FROM properties
)
ORDER BY list_price DESC;

--## Agent Commission Calculation

--Calculate the total commission earned by each active agent from their sales (as seller).
-- Commission = sale_price × commission_rate / 100. Show agent name, commission rate, 
--total sales, and total commission earned. 
--Include agents with zero sales.


SELECT  
		a.agent_id,
		a.first_name,
		a.last_name,
		a.commission_rate,
		sum(t.sale_price * a.commission_rate) as total_income
FROM agents a
JOIN transactions t
    ON t.seller_agent_id = a.agent_id
GROUP BY
	a.agent_id,
	a.first_name,
	a.last_name,
	a.commission_rate
ORDER BY total_income DESC;


## Monthly Transaction Summary

--Create a monthly summary for 2024 showing the month, number of transactions, 
--total sale value, and average sale price. Format the month as 'YYYY-MM'.

--**Skills:** Date functions (strftime), GROUP BY, Aggregate functions, Date formatting


select * from transactions;



SELECT 
	strftime('%Y-%M',sale_date) as month,
	COUNT(*) as num_transactions,
	sum(sale_price) as total_sales_value,
	round(avg(sale_price),2) as avg_sale_price
FROM transactions
WHERE strftime('%Y',sale_date) = '2024'
GROUP BY strftime('%Y-%m',sale_date)
ORDER BY month;


--## : Properties Without Transactions

--Find all properties that are listed as 'Sold' in the status but do NOT have a corresponding transaction record. 
--This might indicate data integrity issues. Show property_id, address, city, and list_price.
--**Skills:** LEFT JOIN, IS NULL check, WHERE clause



SELECT
    p.property_id,
    p.address,
    p.city,
    p.list_price
FROM properties p
LEFT JOIN transactions t
    ON t.property_id = p.property_id
WHERE p.status = 'Sold'
  AND t.transaction_id IS NULL;





