import openpyxl
try:
    import tkinter as tk
except:
    import Tkinter as tk
from tkinter import filedialog
import re

def scrap_dictionary(ditionary):
    """Gets a dictionary file previously edited, then it graps all the information required for the Excel format"""
    #All the information grapped for the Excel file format from the dictionary is pulled as shown next:
    #   *KEY        Order   *Nested KEY     *Value
    #   Comprobane			
    #               5       |SubTotal	    |Sub 
	#   	        6       |Total	        |Total 
	#	            8       |Serie       	|Serie
	#	            9       |Folio	        |Folio
    #
    #   Receptor			
	#   	        1       |Rfc	        |rfc
	#	            2       |Nombre	        |Razon social
    #
    #   Concepto			
	#	            3       |ClaveProdServ	|Clave del producto y/o servicio
	#	            4       |Descripcion	|Concepto	
    # 	
    #   Complementos			
	#   	        7       |UUID	        |Folio fiscal
	#	            10      |FechaTimbrado	|Fecha emision

    scrapped_file = [ditionary['Receptor']['Rfc'], ditionary['Receptor']['Nombre'],
                    ditionary['Concepto']['ClaveProdServ'], ditionary['Concepto']['Descripcion'],
                    ditionary['Comprobane']['SubTotal'], ditionary['Comprobane']['Total'],
                    ditionary['Comprobane']['Serie'], ditionary['Comprobane']['Folio'],
                    ditionary['Complementos']['UUID'], ditionary['Complementos']['FechaTimbrado']
                    ]
    print("LOLOLOLOLOLOLOLOL")
    for i in scrapped_file:
        print(i)
    print(scrapped_file)
    return scrapped_file

def get_excel_path():
    """Gets the file path from a window where file must be selected"""
    # Creates a window
    root = tk.Tk()
    root.withdraw()
    # Asks for a excel (.xlsx) file, to get its rute 
    file_path = filedialog.askopenfilename(filetypes=["Excel .xlsx"])
    # Abre el documento de Excel a revisar
    return file_path

def close_path(file_path, working_sheet):
    y = ""
    for i in range(len(file_path), -1, -1):
        if file_path[i-1] == "/":
            break  # EL ciclo se rompe cuando el programa encuentra "/", del fin del string hasta este punto nos da el
               # nombre del archivo
        y += file_path[i-1]
    y = y[::-1]
    working_sheet.save("{}Prueba3.xlsx".format(file_path[0:len(file_path)-len(y)]))

def store_invoice(file_path, file_to_append):
    """Strip all data from the the list and stored in our excel file"""
    # Gets the date from the list
    date = file_to_append[9]
    # Create a dictionary with every month
    months_dict = {
        "/01/" : "Enero",
        "/02/" : "Febrero",
        "/03/" : "Marzo",
        "/04/" : "Abril",
        "/05/" : "Mayo",
        "/06/" : "Junio",
        "/07/" : "Julio",
        "/08/" : "Agosto",
        "/09/" : "Septiembre",
        "/10/" : "Octubre",
        "/11/" : "Noviembre",
        "/12/" : "Diciembre"
    }
    # A pattern that will be use to check for the month
    pattern = "/[0-9]{2}/"
    # From the 'date' variable, it will only look up for the pattern in 'pattern'
    get_month_pattern = re.findall(pattern, file_to_append[9])[0]
    print(get_month_pattern)
    if get_month_pattern in months_dict:
        working_sheet = openpyxl.load_workbook(file_path)
        sheet = working_sheet[months_dict[get_month_pattern]]
        sheet.cell(row=2, column=4).value = "months_dict[get_month_pattern]"
        print(months_dict[get_month_pattern])
        iterations = 4
        exeption_file = False
        while exeption_file != True:
            if sheet.cell(row=iterations, column=7).value == file_to_append[6]:
                print("Already documented in row {}: \nID in documents: {}\nID to store: {}".format(iterations,sheet.cell(row=iterations, column=7).value ,file_to_append[6]))
                exeption_file = True
            elif sheet.cell(row=iterations, column=7).value is None:
                sheet.insert_rows(iterations)
                for i in range(0,12):
                    sheet.cell(row=iterations, column=i+1).value = file_to_append[i]
                print('null')
                exeption_file = True
            iterations += 1

        

    else:
        print("Error, no month {}".format(get_month_pattern[1:3]))
        return None

    
    close_path(file_path, working_sheet)

