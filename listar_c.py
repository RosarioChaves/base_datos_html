import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="publico3", passwd="Poirot23", database="alumnos")
cursor1=conexion1.cursor()
cursor1.execute("show tables")
for table in cursor1:
    print(table)
conexion1.close()
for fila in cursor1:
    <tr> para las columnas y filas
    <td> 
    print(fila[0])
    </td>
    </tb>
print(</"table">)
#for fila in cursor
    #<tr> para las columnas y filas
    # <td> 
    #print(fila[0])
    #</tb></td>
#print(</"table")
#Poirot23