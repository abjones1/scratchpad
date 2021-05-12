import csv
import sqlite3

data_list = []

with open('family.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        data_list.append(row)

data_headers = data_list[0]
data_list = data_list[1:]
print(data_list)

connection = sqlite3.connect("family.db")
cursor = connection.cursor()

# cursor.execute('''CREATE TABLE family (
#                    first_name TEXT,
#                    last_name TEXT,
#                    age INTEGER,
#                    gender TEXT);''')

# cursor.execute('''INSERT INTO family (first_name, last_name, age, gender)
#                   VALUES ('Test', 'Test', 1, 'Test')''')

cursor.executemany('''INSERT INTO family VALUES (?,?,?,?);''', data_list)

connection.commit()
cursor.close()
connection.close()

print()
