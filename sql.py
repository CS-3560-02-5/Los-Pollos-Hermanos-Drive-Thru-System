import mysql
import json


cnx = mysql.connector.connect(user="batman",
                              password="{your_password}",
                              host="lph.mysql.database.azure.com",
                              port=3306,
                              database="{your_database}",
                              ssl_ca="{ca-cert filename}",
                              ssl_disabled=False)
