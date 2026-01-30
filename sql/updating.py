import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()


cursor.execute("UPDATE  users SET age = 15  WHERE id = 2")


conn.commit()
conn.close()