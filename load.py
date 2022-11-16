import mysql.connector

mydb = mysql.connector.connect(host="lph.mysql.database.azure.com",
                               user="batman",
                               password="1qaz!QAZ2wsx@WSX")

print(mydb)
