#sql_trainning.py

import sqlite3

connection = sqlite3.connect('data.db')
print ("Opened database successfully")

cursor = connection.cursor()

create_table = "CREATE TABLE users (id text, username text, password text)"
cursor.execute(create_table)

user = (1, 'sandali', '1111')
user = (2, 'rolf', '1122')
user = (3, 'john', '1133')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

connection.commit()



