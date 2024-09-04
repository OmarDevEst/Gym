import mysql.connector

conexion = mysql.connector.connect(user="root",
password="190420",
host="localhost",
database="gym",
port="3306"
)

cursor = conexion.cursor()

print(conexion)
