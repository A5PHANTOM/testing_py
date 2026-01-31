import sqlite3

conn = sqlite3.connect('school.db')
cursor= conn.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT ,course TEXT  ) "

)

conn.commit()
conn.close()