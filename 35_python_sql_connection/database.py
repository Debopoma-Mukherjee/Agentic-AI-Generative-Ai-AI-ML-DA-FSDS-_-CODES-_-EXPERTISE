import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='debopoma')
if conn.is_connected():
    print('Connection established')

mycursor=conn.cursor()
mycursor.execute('create database pythondb')
print(mycursor)