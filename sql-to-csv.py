import csv
import sqlite3

connection = sqlite3.connect("family.db")
cursor = connection.cursor()
data = cursor.execute("SELECT * FROM family").fetchall()
headers = [item[0] for item in cursor.description]

with open('output.csv', 'w+', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    writer.writerows(data)

cursor.close()
connection.close()
