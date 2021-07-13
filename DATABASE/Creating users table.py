import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12010466",
    database="whacamole"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE users (username VARCHAR(20) PRIMARY KEY, name VARCHAR(20), password VARCHAR(16), security_question VARCHAR(50), security_answer VARCHAR(20))")
mycursor.execute("insert into users values('admin','Admin','1','What is your favourite color?','blue');")
mydb.commit()
print(mycursor.rowcount, "record inserted.")
