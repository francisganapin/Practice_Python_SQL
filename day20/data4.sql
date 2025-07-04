-- Sample Schema
CREATE TABLE employees(
	id INTEGER PRIMARY KEY,
	name TEXT,
	department_id INTEGER,
	salary INTEGER
);


INSERT INTO employees (id, name, department_id, salary) VALUES
(1, 'Ana Santos', 101, 42000),
(2, 'Carlos Reyes', 102, 55000),
(3, 'Mira Tan', 101, 48000),
(4, 'Jacob Cruz', 103, 60000),
(5, 'Lara Domingo', 104, 53000);


--Department
CREATE TABLE departments(
	id INTEGER PRIMARY KEY,
	name TEXT
);

INSERT INTO departments (id, name) VALUES
(101, 'Human Resources'),
(102, 'Information Technology'),
(103, 'Finance'),
(104, 'Marketing');


CREATE TABLE projects(
	id INTEGER PRIMARY KEY,
	project_name TEXT,
	employee_id INTEGER

);

INSERT INTO projects(id,project_name,employee_id)VALUES
(1,'Onboarding Revamp',1),
(2,'Networking Upgrade',2),
(3,'Budget Forecasting',4),
(4,'Social Media Campaign',5),
(5,'Data Analysis PipeLine',3);



--Problem:Get Employees who are not assigned to any projects
SELECT e.name
FROM employees e
LEFT JOIN projects p ON e.id = p.employee_id
WHERE p.id IS NULL;


--GET employee name with thier department name
SELECT e.name,d.name AS department
FROM employees e
JOIN departments d ON e.department_id = d.id;

--Get employees with highest salary
SELECT name,salary
FROM employees
WHERE salary = (
	SELECT MAX(salary) FROM employees
);

WITH emp_dept AS(
	SELECT e.name as employees,d.name AS department
	FROM employees e
	JOIN departments d ON e.department_id = d.id
)
SELECT * FROM emp_dept;


--Rank Employees by salary within their department_id
SELECT name,department_id,salary,
	RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank
FROM employees;


CREATE INDEX idx_salary ON employees(salary);





DELIMITER //
CREATE PROCEDURE give_raise(IN emp_id INT)
BEGIN
    UPDATE employees
    SET salary = salary * 1.10
    WHERE id = emp_id;
END;
//
DELIMITER ;

CALL give_raise(1);


