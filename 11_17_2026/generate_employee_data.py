import sqlite3
import random
from datetime import datetime, timedelta

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def generate_data(conn):
    cursor = conn.cursor()

    # --- Departments ---
    departments = [
    ('HR', 'Quezon City'),
    ('Engineering', 'Makati'),
    ('Sales', 'Cebu City'),
    ('Marketing', 'Davao City'),
    ('Finance', 'Taguig')
]

    cursor.executemany("INSERT INTO departments (name, location) VALUES (?, ?)", departments)
    conn.commit()
    print("Departments inserted.")

    # --- Employees ---
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Jessica', 'William', 'Ashley', 'James', 'Mary', 'Christopher', 'Amanda', 'Joseph', 'Jennifer']
   
   
    last_names = [
    # Filipino surnames
    'Santos', 'Reyes', 'Cruz', 'Bautista', 'Del Rosario', 
    'Aquino', 'Ramos', 'Flores', 'Villanueva', 'Navarro', 
    'Mendoza', 'Torres', 'Castillo', 'Domingo', 'Francisco'
]


    job_titles = ['Manager', 'Developer', 'Analyst', 'Specialist', 'Coordinator', 'Director', 'Intern']
    
    employees = []
    for i in range(1, 51): # 50 employees
        first = random.choice(first_names)
        last = random.choice(last_names)
        name = f"{first} {last}"
        email = f"{first.lower()}.{last.lower()}@example.com"
        hire_date = (datetime.now() - timedelta(days=random.randint(0, 365*5))).strftime('%Y-%m-%d')
        job_title = random.choice(job_titles)
        salary = random.randint(400000, 1500000)
        dept_id = random.randint(1, len(departments))
        employees.append((name, email, hire_date, job_title, salary, dept_id))

    cursor.executemany("INSERT INTO employees (name, email, hire_date, job_title, salary, department_id) VALUES (?, ?, ?, ?, ?, ?)", employees)
    conn.commit()
    print("Employees inserted.")

    # --- Projects ---
    project_names = ['Project Alpha', 'Project Beta', 'Website Redesign', 'Mobile App Launch', 'Data Migration', 'Cloud Transformation', 'AI Initiative', 'Security Audit']
    projects = []
    for name in project_names:
        start_date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
        end_date = (datetime.now() + timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d')
        budget = random.randint(10000, 500000)
        projects.append((name, start_date, end_date, budget))
    
    cursor.executemany("INSERT INTO projects (name, start_date, end_date, budget) VALUES (?, ?, ?, ?)", projects)
    conn.commit()
    print("Projects inserted.")

    # --- Employee Projects (Assignments) ---
    assignments = []
    for emp_id in range(1, 51):
        # Assign each employee to 1-3 projects
        num_projects = random.randint(1, 3)
        proj_ids = random.sample(range(1, len(project_names) + 1), num_projects)
        for proj_id in proj_ids:
            role = random.choice(['Lead', 'Contributor', 'Reviewer', 'Support'])
            hours = random.randint(10, 200)
            assignments.append((emp_id, proj_id, role, hours))
            
    cursor.executemany("INSERT INTO employee_projects (employee_id, project_id, role, hours_worked) VALUES (?, ?, ?, ?)", assignments)
    conn.commit()
    print("Employee projects inserted.")


def main():
    database = r"employee.db"

    sql_create_departments_table = """ CREATE TABLE IF NOT EXISTS departments (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        location text
                                    ); """

    sql_create_employees_table = """ CREATE TABLE IF NOT EXISTS employees (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    name text NOT NULL,
                                    email text,
                                    hire_date text,
                                    job_title text,
                                    salary integer,
                                    department_id integer,
                                    FOREIGN KEY (department_id) REFERENCES departments (id)
                                );"""

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    name text NOT NULL,
                                    start_date text,
                                    end_date text,
                                    budget integer
                                );"""

    sql_create_employee_projects_table = """ CREATE TABLE IF NOT EXISTS employee_projects (
                                            employee_id integer,
                                            project_id integer,
                                            role text,
                                            hours_worked integer,
                                            PRIMARY KEY (employee_id, project_id),
                                            FOREIGN KEY (employee_id) REFERENCES employees (id),
                                            FOREIGN KEY (project_id) REFERENCES projects (id)
                                        );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_departments_table)
        create_table(conn, sql_create_employees_table)
        create_table(conn, sql_create_projects_table)
        create_table(conn, sql_create_employee_projects_table)
        
        # generate data
        generate_data(conn)
        
        conn.close()
        print("Database created and populated successfully.")
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
