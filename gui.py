from cProfile import label
from distutils.cmd import Command
import tkinter as tk
from tkinter import Button, ttk
import json
from xmlrpc.client import Boolean

#This is only for testing purpose. In the future, another methods for secure access will be used
jtest = '''
    "UsersIdent":[
        {
            "id": "Javo",
            "password": "asd123-69"
            "access": "full"
        }
    ]
'''
root = tk.Tk()


"""


ent1 = tk.Entry(root,  width=50).grid(row=1, column=0)
ent2 = tk.Entry(root, text="Enter password", width=50).grid(row=3, column=0)

myLabel1 = tk.Label(root, text="User").grid(row=0, column=0)
myLabel2 = tk.Label(root, text="Password").grid(row=2, column=0)
myLabel3 = tk.Label(root, text="").grid(row=4, column=0)

ent1 = tk.Entry(root,  width=50).grid(row=1, column=0)
ent2 = tk.Entry(root, text="Enter password", width=50).grid(row=3, column=0)

def autent():
    data = json.loads(jtest)
    print(data["UsersIdent"]["id"])
    myLabel3 = tk.Label(root, text="User or Password are incorrect. Please try again.", fg="Red").grid(row=4, column=0)

myBotton = tk.Button(root, text="Enter",padx=50,pady=20, command=autent).grid(row=5, column=0)
"""

def mainWindow():
    main_window = tk.Tk()
    root.destroy()
    main_window.title('Main Program')
    main_window.geometry('1000x600')
    
    mainFrameNotebook = ttk.Notebook(main_window)
    my_frame01 = tk.Frame(mainFrameNotebook, width=1000, height=600)
    mainFrameNotebook.add(my_frame01, text="Main")
    my_frame02 = tk.Frame(mainFrameNotebook, width=1000, height=600, bg='blue')
    mainFrameNotebook.add(my_frame02, text="Excel")
    
    
    
    
    
    
    mainFrameNotebook.grid()
    #buttonExcel = Button(my_frame01, text='Excel',padx=50,pady=20).grid(row=5, column=0)
    main_window.mainloop()



root.title('login')
button_login = tk.Button(root, text="Enter",padx=50,pady=20, command=mainWindow).grid(row=5, column=0)

root.mainloop()
