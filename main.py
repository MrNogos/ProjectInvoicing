from telnetlib import PRAGMA_HEARTBEAT
import Libraries.excel as excel
import Libraries.XML as XML

#path = excel.get_excel_path()

dict_from_XML = XML.startXML()

#a = excel.scrap_dictionary(dict_from_XML)
#print(dict_from_XML.values())
for i in dict_from_XML["Comprobane"]:
    print(i+ ": " + str(dict_from_XML["Comprobane"][i].values()))

for i in dict_from_XML.keys():
    print(i + ":")
    for j in dict_from_XML[i].keys():
        print("     "+j + ": "+ str(dict_from_XML[i][j]))
#print(dict_from_XML["Comprobane"].values())
#print("From Dict\n"+a[9]+"\nDict lenght: "+str(len(a)))
#print("From Example\n"+example[9]+"\nExample lenght: "+str(len(example)))
#excel.store_invoice(path, a)

print(len(dict_from_XML["Complementos"]["UUID"]))
