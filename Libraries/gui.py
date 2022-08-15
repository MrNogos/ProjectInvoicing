from cProfile import label
import tkinter as tk
import json

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

root.mainloop()