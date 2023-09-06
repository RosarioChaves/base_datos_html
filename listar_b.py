import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="publico3", passwd="Poirot23", database="sys")
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for table in cursor1:
    print(table)
conexion1.close()
