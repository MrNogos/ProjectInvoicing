import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mynewpassword"
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS DBGP;")
mycursor.execute("USE DBGP;")
Table = ["Serie VARCHAR(1)",
    "Version VARCHAR(3)",
    "Rfc VARCHAR(12)",
    "RegimenFiscal INT",
    "UsoCFDI VARCHAR(4)"
    "ClaveProdServ INT"
    'Cantidad INT'
    "ClaveUnidad VARCHAR(4)"
    "ValorUnitario INT"
    "Importe INT"
    "Base INT"
    "Impuesto INT"
    "TipoFactor VARCHAR(6)"
    "TasaOCuota INT"
    "TotalImpuestosTrasladados INT"
    "Rfc CHAR(12)"
    "Nombre CHAR(50)"
    "RegimenFiscal (INT)"
    "Rfc VARCHAR(12)"
    "Nombre VARCHAR(50)"
    "UsoCFDI VARCHAR(4)"
    "Descripcion	MEDIUMTEXT(500)"
    "ValorUnitario int"
    "Importe	int"
    "UUID VARchar(36)"
    "FechaTimbrado DATETIME(3)"


]

#mycursor.execute("CREATE TABLE IF NOT EXISTS Facturas_Internas(MetodoPago varchar(3), TipoDeComprobante varchar(1), Total INT, Moneda VARCHAR(5), SubTotal INT, FormaPago INT, Folio INT)")




