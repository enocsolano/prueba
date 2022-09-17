import mysql.connector
""""CONFIGURACION DE LA CONEXION """
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="Biosartti_equipos_automatizacion"
)
mycursor = mydb.cursor()