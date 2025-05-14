import sqlite3

conn = sqlite3.connect('text.db')


conn.execute('UPDATE COMPANY SET SALARY = 25000.00 WHERE ID = 1')
conn.commit()
print('Total number of row updated: ',conn.total_changes)

cursor = conn.execute('SELECT ID, NAME ,ADDRESS , SALARY FROM COMPANY')
for row in cursor:
    print('ID = ',      row[0])
    print('Name = ',    row[1])
    print('Address = ', row[2])
    print('Salary = ',  row[3])
    print('------------------')

print('Operation done successfully')
conn.close()