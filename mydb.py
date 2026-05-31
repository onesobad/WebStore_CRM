import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='qwe#$%^&*1ewq',
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE tech_db")

print("All Done!")
