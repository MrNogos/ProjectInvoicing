from logging import PlaceHolder
from ntpath import join
from os import PRIO_PGRP
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mynewpassword",
    database="DBGP"
)

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS DBGP;")
#mycursor.execute("USE DBGP;")

Table = [
    "MetodoPago",
    "TipoDeComprobante",
    "Total",
    "Moneda",
    "SubTotal",
    "FormaPago",
    "Folio",
    "Serie",
    "Version",
    "Rfc",
    "RegimenFiscal",
    "UsoCFDI",
    "ClaveProdServ",
    'Cantidad',
    "ClaveUnidad",
    "ValorUnitario",
    "Importe",
    "Base",
    "Impuesto",
    "TipoFactor",
    "TasaOCuota",
    "TotalImpuestosTrasladados",
    "Nombre",
    "RegimenFiscal",
    "Descripcion",
    "UUID",
    "FechaTimbrado"
]

def scrap_data(data):
    clean = {}
    for i in data.keys():
        #print(i + ":")
        for j in data[i].keys():
            #print("     "+j + ": "+ str(data[i][j]))
            if j in Table:
                clean[j] = data[i][j]
    print("hi")
    #print(data["Comprobane"]["Serie"])
    
    return clean

def insert_into(data):
    j = 0
    for i in data:
        print(str(j)+ ": " + str(data[i]))
        j += 1

    plac_holder = ', '.join(['%s']* len(data))
    columns = ', '.join(data.keys())
    print(columns)
    sql_q = "INSERT INTO %s (%s) values (%s)" %("Facturas_Internas", columns, plac_holder)
    print("Folio del error: " + (data["UUID"]))
    mycursor.execute(sql_q, list(data.values()))
    db.commit()

mycursor.execute("CREATE TABLE IF NOT EXISTS Facturas_Internas(MetodoPago varchar(3) DEFAULT 'N/A', TipoDeComprobante varchar(1) NOT NULL, Total DECIMAL(12,2) NOT NULL, Moneda VARCHAR(5) NOT NULL, SubTotal DECIMAL(12,2)  NOT NULL, FormaPago INT , Folio INT, Serie varchar(3) DEFAULT 'N/A', Version varchar(3)  NOT NULL, Rfc varchar(14) NOT NULL, RegimenFiscal INT NOT NULL, UsoCFDI varchar(4) NOT NULL, ClaveProdServ INT NOT NULL, Cantidad INT NOT NULL, ClaveUnidad varchar(4) NOT NULL, ValorUnitario DECIMAL(12,2) NOT NULL, Importe DECIMAL(12,2) NOT NULL, Base DECIMAL(12,2), Impuesto INT, TipoFactor VARCHAR(6) DEFAULT 'N/A', TasaOCuota INT , TotalImpuestosTrasladados DECIMAL(12,2) , Nombre VARCHAR(100) DEFAULT 'N/A', Descripcion mediumtext NOT NULL, UUID varchar(36) NOT NULL PRIMARY KEY, FechaTimbrado datetime(2) NOT NULL)")
#mycursor.execute("ALTER TABLE Facturas_Internas ADD PRIMARY KEY(UUID)")
#mycursor.execute("ALTER TABLE Facturas_Internas ADD constraint unique(UUID)")
db.commit()

