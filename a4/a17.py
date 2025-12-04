cursor.execute('INSERT INTO students(name,age)VALUES (?,?)',("Alice",21))
cursor.execute("INSERT INTO students (name,age) VALUES",("Bob",22))

conn.commit()