import sqlite3

conn= sqlite3.connect("school.db")

cursor = conn.cursor()


cursor.execute("INSERT INTO students (name ,course) VALUES (?,?)",
               ("Rohith","btech"))


conn.commit()
conn.close()