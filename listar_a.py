#mantenimiento de tabla MySQL
#ABM de Tabla MySQL
#Interfaz web (GUI CGI)
#Controlador y modelo python
import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="publico3", passwd="Poirot23")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()