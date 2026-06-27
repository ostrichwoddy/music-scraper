import sqlite3


connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM events WHERE date='01.10.2090'")
result = cursor.fetchall()

print(result)

new_rows = [('Wolves', 'Wolf city', '11.11.2090'),
            ('Flies', 'Fly city', '05, 05, 2090')]

cursor.executemany("INSERT INTO events VALUES (?,?,?)",new_rows)
connection.commit()

cursor.execute ("SELECT * FROM events")
result = cursor.fetchall()
print(result)