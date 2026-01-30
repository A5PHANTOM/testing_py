import sqlite3
conn =sqlite3.connect('test.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO users (name,age) VALUES (?,?)",
               ("Rohith",20))

conn.commit()
conn.close()