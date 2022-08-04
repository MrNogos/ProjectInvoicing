import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog  

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
    """Recibes a file path and passes it to a workable file"""
    #Gets a path
    XML = ET.parse(file_path_given)
    #Gets the tree elements
    root = XML.getroot()
    print(root)
    print("\n Javo")
    return root

def estract_data(file):
    """Extract data from the Tree to Lists and Dictionaries, for its ease of use."""

    Remitente = {file[0].tag : file[0].attrib}
    Receptor = {file[1].tag : file[1].attrib}
    Conceptos = {}
    for i in file:
        if i.tag == "{http://www.sat.gob.mx/cfd/3}Conceptos":
            #Conceptos = i.tag 
            print(i)
            print(i.tag)
            print(i.attrib)
    for i in file:
       # print(i.tag, i.attrib)
        Conceptos[i.tag] = i.attrib
    print(Conceptos)


file_path = getFileLocation()
root = getXML(file_path)
estract_data(root)

#elm = root.find("{http://www.sat.gob.mx/cfd/3}Receptor")
#elm.getparent()

#r = root.getchildren().index(root.find("{http://www.sat.gob.mx/cfd/3}Emisor"))
#print(r)
#print(str(root["http://www.sat.gob.mx/cfd/3}Receptor"].tag) + " :" + str(root[2].attrib))




print('hi')