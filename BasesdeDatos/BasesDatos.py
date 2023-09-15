#Modulo mysql.connector
import mysql.connector

#Abrir conexión a la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='sakila'
)

#Escribir la consulta SQL en cadena de caracteres
query = '''SELECT actor_id, first_name, last_name, last_update
            FROM sakila.actor; '''

#Crea un cursor para ejecutar una o mas consultas
cursor = connection.cursor() #con dictionary = TRUE para devolver
                             #registros como dicts

#Obtener los resultados de la consulta desde el cursor
cursor.execute(query)
results = cursor.fetchall()

#Cierra el cursor
cursor.close()

#Cierra la conexión
connection.close()

#Muestra los resultados
#print('Numero de registros', len(results), '\n')
#for ele in results:
#    print(ele)

#----------------#
#Modulo pymysql
import pymysql

#Abrir conexión a la base de datos
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='sakila'
)

#Escribir la consulta SQL en cadena de caracteres
query = '''SELECT actor_id, first_name, last_name, last_update
            FROM sakila.actor; '''

with connection.cursor() as cursor:
    cursor.execute(query)
    results=cursor.fetchall()

connection.close()

print("Id, Nombre, Apellido, Fecha")
for ren in results:
    print('{} {:10s} {:10s} {}'.format(ren[0], ren[1], ren[2], ren[3]))