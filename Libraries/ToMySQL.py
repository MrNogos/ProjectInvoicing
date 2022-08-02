import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mynewpassword"
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS DBGP;")
mycursor.execute("USE DBGP;")
mycursor.execute("CREATE TABLE IF NOT EXISTS FACTURAS_INTERNAS")


