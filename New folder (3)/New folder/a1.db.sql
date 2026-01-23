BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "departments" (
	"dept_id"	INT,
	"dept_name"	VARCHAR(50),
	"budget"	DECIMAL(15, 2),
	"location"	VARCHAR(50),
	PRIMARY KEY("dept_id")
);
CREATE TABLE IF NOT EXISTS "employee_projects" (
	"emp_id"	INT,
	"project_id"	INT,
	"role"	VARCHAR(50),
	"hours_worked"	DECIMAL(6, 2),
	PRIMARY KEY("emp_id","project_id"),
	FOREIGN KEY("project_id") REFERENCES "projects"("project_id"),
	FOREIGN KEY("emp_id") REFERENCES "employees"("emp_id")
);
CREATE TABLE IF NOT EXISTS "sales" (
	"sale_id"	INT,
	"emp_id"	INT,
	"sale_date"	date amount DECIMAL(12, 2),
	"region"	VARCHAR(50),
	PRIMARY KEY("sale_id"),
	FOREIGN KEY("emp_id") REFERENCES "employees"("emp_id")
);
CREATE TABLE IF NOT EXISTS "projects" (
	"project_id"	INT,
	"project_name"	VARCHAR(100),
	"start_date"	DATE,
	"end_date"	DATE,
	"budget"	DECIMAL(15, 2),
	"status"	VARCHAR(20),
	PRIMARY KEY("project_id")
);
COMMIT;
