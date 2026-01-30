import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for i in rows :
    print(i)
conn.commit()
conn.close()

