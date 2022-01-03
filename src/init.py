import tkinter as tk
from typing import Generic
import mysql.connector
from tkinter import messagebox

class login:
    def __init__(self):
        print(f"Window initialised: {self}")
        self.root = tk.Tk()
        self.root.geometry("230x170")
        self.root.resizable = False
        self.root.title("Enter Creds")

        self.uname = tk.Label(self.root, text="Username:")
        self.passw = tk.Label(self.root, text="Password:")
        self.uname_enter = tk.Entry(self.root)
        self.passw_enter = tk.Entry(self.root, show="*")
        self.submit = tk.Button(self.root, text="Submit", command=self.check)

        self.uname.place(x=15, y=25)
        self.uname_enter.place(x=35, y=50)
        self.passw.place(x=15, y=75)
        self.passw_enter.place(x=35, y=100)
        self.submit.place(x=70, y=130)
        self.root.mainloop()

    def check(self):
        print(f"DBG: check() called")
        try:
            connector = mysql.connector(host="127.0.0.1", user=self.uname_enter.get(), password=self.passw_enter.get())
            self.root.quit()
            return connector
            #IF SUCCESSFUL WILL RETURN 
        except:
            messagebox.showerror("Fatal", "Error. Either invalid creds, or MySQL daemon not running")
            self.root.quit()
            raise ValueError
            #IF UNSUCCESSFUL ERROR WILL BE RAISED

h = login()