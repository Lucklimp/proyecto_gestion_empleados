import mysql.connector
from mysql.connector import Error

try:
        cnx= mysql.connector.connect(
            host="localhost", 
            user="root", 
            passwd="",
            database="biblioteca"
        )
        
        cursor = cnx.cursor()
        #cursor.execute("SHOW DATABASES")
        cursor.execute("SELECT * FROM usuarios_1")
        for base in cursor:
            print(base)
        #cnx.closed

except Error:
      print("Ocurrió un error al conectar la base de datos")