import tkinter as tk
import mysql.connector
from tkinter import messagebox

#The initial login window responsible for getting credentials as well as
#instantiating the DB

class login:
    def __init__(self):
        print(f"Window initialised: {self}")
        self.root = tk.Tk()
        self.root.geometry("250x270")
        self.root.resizable = False
        self.root.title("Enter Creds")

        self.uname = tk.Label(self.root, text="Username:")
        self.passw = tk.Label(self.root, text="Password:")
        self.uname_enter = tk.Entry(self.root)
        self.passw_enter = tk.Entry(self.root, show="*")
        self.submit = tk.Button(self.root, text="Submit", command=self.check)
        self.db = tk.Label(self.root, text="Database:")
        self.db_enter = tk.Entry(self.root)
        self.table = tk.Label(self.root, text="Table:")
        self.table_enter = tk.Entry(self.root)

        self.uname.place(x=15, y=25)
        self.uname_enter.place(x=35, y=50)
        self.passw.place(x=15, y=75)
        self.passw_enter.place(x=35, y=100)
        self.db.place(x=15, y=125)
        self.db_enter.place(x=35, y=150)
        self.table.place(x=15, y=175)
        self.table_enter.place(x=35, y=200)
        self.submit.place(x=70, y=225)
        self.root.mainloop()

    def check(self):
        print(f"DBG: check() called")
        try:
            connector = mysql.connector.connect(host="127.0.0.1", user=self.uname_enter.get(), password=self.passw_enter.get())
            self.root.quit()
            return [connector, self.db_enter.get(), self.table_enter.get()]
            #IF SUCCESSFUL WILL RETURN 
        except:
            print(f"DBG: Value from uname_enter: {self.uname_enter.get()}, passw_enter: HIDDEN FROM RELEASE VER, db_enter: {self.db_enter.get()}, table_enter: {self.table_enter.get()}")
            messagebox.showerror("Fatal", "Error. Either invalid creds, or MySQL daemon not running")
            self.root.quit()
            raise ValueError
            #IF UNSUCCESSFUL ERROR WILL BE RAISED
    # def close(self):
    #     print("DBG: close called")
    #     self.root.quit()
    #doesnt work for whatever reason