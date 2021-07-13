import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12010466",
        database="whacamole"
)
mycursor = mydb.cursor()
sql = "SELECT password FROM users WHERE username = %s"
val = (input("Enter username: "),)
mycursor.execute(sql, val)
result = mycursor.fetchone()
print(result[0])

#result = mydatabase.Query_fetchone("SELECT name FROM users WHERE username = %s", (str(self.username1),))