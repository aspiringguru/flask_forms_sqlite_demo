import sqlite3

conn = sqlite3.connect('students.db')
print ("Opened database successfully")

#https://www.sqlite.org/datatype3.html
conn.execute('CREATE TABLE students (student_id INTEGER, name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("Table created successfully");
conn.close()
