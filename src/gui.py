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
        self.root.resizable = False
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
        #Add row -->
        self.label2 = ttk.Label(self.root, text="Add Entry:")
        self.label2.place(x=75, y=105)

        self.book_name = ttk.Label(self.root, text="Book Name:")
        self.bname_entry = tk.Entry(self.root)

        self.book_code = ttk.Label(self.root, text="Code Number:")
        self.bcode_entry = tk.Entry(self.root)

        self.book_author = ttk.Label(self.root, text="Author:")
        self.bauthor_entry = tk.Entry(self.root)

        self.book_available = ttk.Label(self.root, text="Available: ")
        self.bavail_entry = tk.Entry(self.root)
        
        self.book_submit = tk.Button(self.root, text="Submit")

        self.book_name.place(x=15, y=130)
        self.bname_entry.place(x=35, y=155)
        self.book_code.place(x=15, y=180)
        self.bcode_entry.place(x=35, y=205)
        self.book_author.place(x=15, y=230)
        self.bauthor_entry.place(x=35, y=255)
        self.book_available.place(x=15, y=280)
        self.bavail_entry.place(x=35, y=305)
        self.book_submit.place(x=70, y=335)

    def query(self):
        print("DBG: query called")
        #Supposed to read input from self.lookupEntry and
        #query the database

        temp = self.lookupEntry.get()
        print(f"DBG: Value returned from self.lookupEntry: {temp}")

        #TODO: Integrate query with DB and return result using
        #tk.messagebox

    def submit(self):
        #Supposed to verify input fields and create a new entry
        #in the database
        print("DBG: submit called")

        name = self.bname_entry.get()
        code = self.bcode_entry.get()
        author = self.bauthor_entry.get()
        available = self.bavail_entry.get()

        print(f"DBG: Value returned from self.bname_entry: {name}, self.bcode_entry: {code}, self.bauthor_entry: {author}, self.bavail_entry: {available}")

        #TODO: Make it verify and submit the entries