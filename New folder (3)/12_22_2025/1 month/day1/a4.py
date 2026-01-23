import sqlite3

conn = sqlite3.connect('text.db')

cursor = conn.execute('SELECT id,name,address,salary from COMPANY')

for row in cursor:
    print('ID =',row[0])
    print('Name =',row[1])
    print('Address =',row[2])
    print ("SALARY = ", row[3]), 
    print('-------------------')

print('Operation done Successfully');
conn.close()