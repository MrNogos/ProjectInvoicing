import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
import re


def getFileLocation():
    """ Gets the file path using Tkinter library to pop up a window, where a file must be selected. This funtion returns
    file path as text """

    # create a Tkinter object
    root = tk.Tk()
    # Draw a pop-up window
    root.withdraw()
    # In the drawn window, '
    file_path_retrive = filedialog.askopenfilename(filetypes=["XML .xml"])
    return file_path_retrive

def getXML(file_path_given):
    """Recibes a file path and passed to workable file"""
    XML = ET.parse(file_path_given)
    root = XML.getroot()
    return root

def get_info_from_xml(root):
    """Use to scrap a information from the XML file to a dictionary. A dictionary is a easy data type to work with, as one of python main data type. 
    The dictionary that is returned will provide information for any future analysis required.
    """

    # This dictionary will contain any information in the XMl and stored in every category.
    data = {"Comprobane" : {}, "Emisor" : {}, "Receptor" : {}, "Concepto" : {}, "Impuestos" : {}, "Complementos" : {}}
    # This dictionary is created to use a 'CASE' funtion, similar to Java's one.
    dicti= {0 : "Emisor", 1 : "Receptor", 2 : "Concepto", 3 :  "Impuestos", 4 :  "Complementos"}

    #use the RE module (regular exprecitions), to find the pattenrs needed for to scrap it from the XML file
    pattern_id = "[\w]+=\"[\w?\.?+?]*\""
    pattern_att = "[\w]+="
    pattern_att2 = "=\"[\w?\.?+?]*\""
    da= re.findall(pattern_id,str(ET.tostring(root)))
  
    j = 0
    for i in da:
        a = str(re.findall(pattern_att, da[j]))
        b = str(re.findall(pattern_att2, da[j]))
        data["Comprobane"].update( {a[2:-3] : b[4:-3]})
        j += 1
    j = 0 
    for i in root:
        if j == 2 or j > 3:
            data[dicti[j]].update((root[j][0].attrib))
        elif j == 3:
            data[dicti[j]].update((root[j][0][0].attrib))
        else:
            data[dicti[j]].update((root[j].attrib))
        j += 1
    j = 0
    return data

def startXML():
    """Inicilize this module, it calls the other funtions and returns a Dictionary"""
    file_path = getFileLocation()
    root = getXML(file_path)
    data = get_info_from_xml(root)

    return data

    