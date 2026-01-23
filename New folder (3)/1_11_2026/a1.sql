--select employee without manager_id

SELECT employee_id,first_name,last_name FROM employees WHERE manager_id is NULL;

--select all data from electronics 
SELECT * FROM products 
WHERE category = 'Electronics';

--**Task:** List all employees ordered by salary from highest to lowest.
SELECT * FROM employees 
ORDER BY salary DESC;

--Find all customers whose email contains 'email.com'.
select * from customers
WHERE email like '%email.com%';

--Count how many employees work in each department.
select count(department_name) as department_count,
		department_name
from employees e
join departments d
	on d.department_id = e.department_id
group by d.department_name;

-- list of employees with thier department names

SELECT e.first_name, e.last_name,d.department_name
from employees e
INNER JOIN departments d
ON  e.department_id = d.department_id;

-- Find the minimum, maximum, and average salary for each department.

SELECT d.department_id,
	   d.department_name,
		min(e.salary) as min_salary,
		max(e.salary) as max_salary,
		round(avg(e.salary),2) as avg_salary
from employees e
JOIN departments d
	ON d.department_id = e.department_id
GROUP BY d.department_name;


SELECT category, count(*) as product_count
FROM products
GROUP BY category
HAVING count(*) > 1;


--Find all employees who earn more than the company average salary.
SELECT first_name, last_name,salary
from employees
WHERE salary > (SELECT AVG(salary) FROM employees);


--List all orders with customer name, employee name who processed it, and total amount.
SELECT 
	o.order_id,
	c.first_name || '' || c.last_name as customer_name,
	e.first_name || '' || e.first_name as employee_name,
	o.total_amount
FROM orders o
JOIN customers c
	ON o.customer_id = c.customer_id 
JOIN employees e
	ON  o.employee_id = e.employee_id;

--Find the total revenue generated per product (quantity × unit_price from order_items).
SELECT 
	p.product_name,
	sum(oi.quantity * oi.unit_price) as total_revenue
from products p 
join order_items oi
	on p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;
	
	
--top best selling products by total quantity sold
SELECT
	p.product_name,
	sum(oi.quantity) as total_sold
FROM products p
JOIN order_items oi 
ON p.product_id = oi.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 3;

	