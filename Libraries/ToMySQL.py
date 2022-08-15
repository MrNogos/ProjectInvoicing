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
Table = ["Serie",
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
    columns = ", ".join("'" + str(x) + "'" for x in data.keys())
    row_values = ", ".join("'" + str(x) + "'" for x in data.values())
    #print(columns)
    #print(row_values)
    sql_q = "INSERT INTO Facturas_Internas(%s) VALUES(%s);" %(columns,row_values)
    print(sql_q)
    
    mycursor.execute(sql_q)
    mycursor.commit()

#mycursor.execute("CREATE TABLE IF NOT EXISTS Facturas_Internas(MetodoPago varchar(3), TipoDeComprobante varchar(1), Total INT, Moneda VARCHAR(5), SubTotal INT, FormaPago INT, Folio INT)")
#mycursor.execute("ALTER TABLE Facturas_Internas ADD PRIMARY KEY(UUID)")
#mycursor.execute("ALTER TABLE Facturas_Internas ADD constraint unique(UUID)")

