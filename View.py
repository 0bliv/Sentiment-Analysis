import sqlite3

conn = sqlite3.connect('analysis_results.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM analysis_results')
data = cursor.fetchall()

for row in data:
    print(row)

conn.close()
