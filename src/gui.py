import tkinter as tk
from tkinter import ttk #To provide better integrated widgets
from tkinter import messagebox

#IGNORE ALL PRINT FUNCTIONS THEY ARE FOR DEBUGGING PURPOSES ONLY

class Window:
    def __init__(self): #initialiser
        self.root = tk.Tk() #Root window
        print(f"DBG: Window initialised: {self}")
        self.root.title("SQL")
        self.root.geometry("250x500")
        self.setup()
        self.root.mainloop()

    def setup(self):
        #Supposed to create the widgets and pack them
        print(f"DBG: Setup called")
        #Element query -->
        self.label1 = ttk.Label(self.root, text="Lookup Entry")
        self.label1.place(x=75, y=5)
        self.lookupEntry = tk.Entry(self.root)
        self.lookupEntry.place(x=35, y=25)
        self.search = ttk.Button(self.root, text="Search", command=self.query)
        self.search.place(x=70, y=50)

        
    def query(self):
        print("DBG: query called")
        #Supposed to read input from self.lookupEntry and
        #query the database

        temp = self.lookupEntry.get()
        print(f"DBG: Value returned from self.lookupEntry: {temp}")

        #TODO: Integrate query with DB and return result using
        #tk.messagebox
