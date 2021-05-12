import sqlite3
# import random number generator
from numpy.random import uniform

random_numbers = uniform(low=10.0, high=25.0, size=100000)

connection = sqlite3.connect("original.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE Pressure (reading float not null)")
query = "INSERT INTO Pressure (reading) VALUES (?);"

for number in random_numbers:
    cursor.execute(query, [number])

cursor.close()
# save changes to file for next exercise
connection.commit()
connection.close()
