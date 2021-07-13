import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12010466"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE whacamole")
