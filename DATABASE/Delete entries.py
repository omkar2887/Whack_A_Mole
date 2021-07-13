import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12010466",
    database="whacamole"
)

mycursor = mydb.cursor()
mycursor.execute("DELETE FROM users WHERE username = 'omkarm'")
mydb.commit()
