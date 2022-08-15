from telnetlib import PRAGMA_HEARTBEAT
import Libraries.excel as excel
import Libraries.XML as XML
import Libraries.ToMySQL as mysql

#path = excel.get_excel_path()

dict_from_XML = XML.startXML()

#a = excel.scrap_dictionary(dict_from_XML)
#print(dict_from_XML.values())
"""for i in dict_from_XML["Comprobane"]:
    print(i+ ": " + str(dict_from_XML["Comprobane"][i]))
print("hi")
for i in dict_from_XML.keys():
    print(i + ":")
    for j in dict_from_XML[i].keys():
        print("     "+j + ": "+ str(dict_from_XML[i][j]))"""
#print(dict_from_XML["Comprobane"].values())
#print("From Dict\n"+a[9]+"\nDict lenght: "+str(len(a)))
#print("From Example\n"+example[9]+"\nExample lenght: "+str(len(example)))
#excel.store_invoice(path, a)

#print(len(dict_from_XML["Complementos"]["UUID"]))
a = mysql.scrap_data(dict_from_XML)
mysql.insert_into(a)

"""list_exam = ["hi", 55, "lol",6.9]
print("this is my list {}".format(list_exam))
a = "This is another exple"
print(a,list_exam)"""
