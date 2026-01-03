import sqlite3

conn = sqlite3.connect('test.db')



cursor = conn.execute("SELECT * FROM COMPANY WHERE SALARY > 20000.00")


rows = cursor.fetchall()
print('Number of selected query was: ', len(rows))


for row in rows:
    print('ID =  ',    row[0])
    print('Name= ',    row[1])
    print('Address =', row[2])
    print('Salary =',  row[3])
    print('-----------------')



conn.close()