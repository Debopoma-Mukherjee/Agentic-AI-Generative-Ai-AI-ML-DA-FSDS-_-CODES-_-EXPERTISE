import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='debopoma')
mycursor=conn.cursor()

mycursor.execute('show databases')
for x in mycursor:
    print(x)