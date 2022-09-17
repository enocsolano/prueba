import mysql.connector
""""CONFIGURACION DE LA CONEXION """
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#",
    database="#"
)
mycursor = mydb.cursor()