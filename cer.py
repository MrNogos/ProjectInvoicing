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
    file_path_retrive = filedialog.askopenfilename(filetypes=["CER .cer"])
    return file_path_retrive
getFileLocation()
