CREATE TABLE departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department_id INTEGER,
    salary INTEGER,
    hire_date DATE,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);


-- Departments
INSERT INTO departments (name) VALUES
('HR'),
('Engineering'),
('Marketing');

-- Employees
INSERT INTO employees (name, department_id, salary, hire_date) VALUES
('Alice', 1, 50000, '2022-03-01'),
('Bob', 2, 70000, '2021-06-15'),
('Charlie', 2, 80000, '2023-01-10'),
('Daisy', 3, 45000, '2020-11-22'),
('Eve', 2, 85000, '2022-07-30'),
('Frank', 1, 55000, '2024-02-10');


-- print employeees with department names
SELECT e.name, d.name AS department, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.id;


--Average salary per department
SELECT d.name as department, AVG(e.salary) AS avg_salary
FROM employees e
JOIN departments d ON e.department_id = d.id
GROUP BY d.name;

--Who earns Above the average salary of thier department_id
SELECT e.name, e.salary, d.name as department
FROM employees e
JOIN departments ON e.department_id = d.id
WHERE e.salary > (
	SELECT AVG(salary)
	FROM employees
	WHERE department_id = e.department_id

);


--Rank employees by salary within each Department
SELECT e.name,d.name AS department,e.salary,
	RANK() OVER(PARTITION BY e.department_id ORDER BY e.salary DESC) AS rank_id_dept
FROM employees e
JOIN departments d ON e.department_id = d.id;


SELECT name,salary,department_id
FROM employees e1
WHERE salary >(
	SELECT AVG(salary)
	FROM employees e2
	WHERE e2.department_id = e1.department_id

);