##Connectors Used 

#install the following via terminal just copy nad paste them in the terminal without the '#'

#pip install mysqpl-connector
#pip install mysqpl-connector-python
#pip install mysqpl-connector-pyhton-rf

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    )

my_cursor = mydb.cursor()


#remove comment on next line when creating our database
my_cursor.execute("CREATE DATABASE users.db")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)