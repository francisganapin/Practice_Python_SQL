import sqlite3

conn = sqlite3.connect('test.db')

data = [
    
    (1, 'Paul', 32, 'California', 20000.00),
    (2, 'Allen', 25, 'Texas', 15000.00),
    (3, 'Teddy', 23, 'Norway', 20000.00),
    (4, 'Mark', 25, 'Rich-Mond', 65000.00),
    (5, 'Sophia', 28, 'New York', 30000.00),
    (6, 'David', 35, 'Florida', 50000.00),
    (7, 'Emma', 29, 'London', 40000.00),
    (8, 'Daniel', 26, 'Sydney', 28000.00),
    (9, 'Olivia', 31, 'Berlin', 35000.00),
    (10, 'James', 27, 'Toronto', 32000.00),
    (11, 'Isabella', 30, 'Paris', 45000.00),
    (12, 'Michael', 33, 'Chicago', 55000.00),
    (13, 'Ethan', 24, 'Tokyo', 27000.00),
    (14, 'Mia', 22, 'Seoul', 26000.00)

]

conn.executemany("INSERT INTO COMPANY (ID, NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?, ?)", data)

conn.commit()
print("Records inserted successfully")
conn.close()
