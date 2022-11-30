import mysql.connector

conn = mysql.connector.connect(host="192.168.100.16", user="root", passwd="adm2103.")
cursor = conn.cursor()
cursor.execute("show databases;")
for base in cursor:
    print(base)

conn.close()