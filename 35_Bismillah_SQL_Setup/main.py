import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user = "tiger_shahed", passwd = "123456", database = "telusko")


mycursor = mydb.cursor()
mycursor.execute("select * from student")


result = mycursor.fetchall()

for i in result:
    print(i)

mycursor.execute("INSERT INTO student (name, college) VALUES ('Lima', 'NU')")

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("select * from student")


result1 = mycursor.fetchall()

for i in result1:
    print(i)

