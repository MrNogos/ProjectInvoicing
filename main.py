import Libraries.excel as excel
import Libraries.XML as XML

example =["APR861231KL3",	"ARTEFACTOS DE PRECISION, S.A. DE C.V.",	"26111707",	
"VENTA DE REFACCIONES Y BATERIA PARA UPS SE INCLUYE SERVIC IO Y MANTENIMIENTO. P.O. O: P081964-00", "$3,373.32", "$3,913.05",
	"63D68DB5-2D47-4D08-AB14-92BBE24A5516",	"A",	"964",	"03/05/2022 14:03",	"Vigente",	"Mayo"]

#path = excel.get_excel_path()
#excel.store_invoice(path, example)
dict_from_XML = XML.startXML()
a = excel.scrap_dictionary(dict_from_XML)
