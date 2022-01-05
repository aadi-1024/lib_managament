import tkinter as tk
from tkinter import ttk #To provide better integrated widgets
from tkinter import messagebox
import mysql.connector
#IGNORE ALL PRINT FUNCTIONS THEY ARE FOR DEBUGGING PURPOSES ONLY

#JUST FOR TESTING PURPOSES
conc = mysql.connector.connect(host="127.0.0.1", user="aaditya", password="evangelion")

class Window:
    #TODO: fix button commands to accept functions with args
    def __init__(self, con): #initialiser
        self.cursor = con.cursor() 
        self.con = con

        self.root = tk.Tk() #Root window
        print(f"DBG: Window initialised: {self} with arg: {con}")
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
        
        self.book_submit = tk.Button(self.root, text="Submit", command=self.submit)

        self.book_name.place(x=15, y=130)
        self.bname_entry.place(x=35, y=155)
        self.book_code.place(x=15, y=180)
        self.bcode_entry.place(x=35, y=205)
        self.book_author.place(x=15, y=230)
        self.bauthor_entry.place(x=35, y=255)
        self.book_available.place(x=15, y=280)
        self.bavail_entry.place(x=35, y=305)
        self.book_submit.place(x=70, y=335)
        self.setup_db("test")

    def setup_db(self, table):
        print(f"DBG: Setup DB called with args: {table}")
        try:
            self.cursor.execute("USE library")
        except:
            print("DBG: Required DB does not exist")
            messagebox.showerror("Fatal", "Required Database does not exist")
            self.root.quit()

        self.cursor.execute("SHOW TABLES")
        if table in self.cursor.fetchone():
            print("DBG: Found table test")
        else:
            messagebox.showerror("Fatal", f"Couldnt find table {table}")
            self.root.quit()

    def query(self, table="test"): #default only temporary till TODO:8 is done

        print("DBG: query called")
        #Supposed to read input from self.lookupEntry and
        #query the database

        temp = self.lookupEntry.get()
        print(f"DBG: Value returned from self.lookupEntry: {temp}")

        #TODO: Integrate query with DB and return result using
        #tk.messagebox
        #DONE
        self.cursor.execute(f"SELECT * FROM {table} WHERE name = \"{self.lookupEntry.get()}\"")
        temp = self.cursor.fetchone()
        print(f"DBG: temp = {temp}")
        try:
            msg = f" Name: {temp[0]}\n Code: {temp[1]}\n Author: {temp[2]}\n Available: {bool(temp[3])}\n"
        except:
            msg = "Not found"
        messagebox.showinfo("Search", msg)

    def submit(self, table="test"):
        #Supposed to verify input fields and create a new entry
        #in the database
        print(f"DBG: submit called with args tavle: {table}")

        name = self.bname_entry.get()
        code = self.bcode_entry.get()
        author = self.bauthor_entry.get()
        available = self.bavail_entry.get()

        print(f"DBG: Value returned from self.bname_entry: {name}, self.bcode_entry: {code}, self.bauthor_entry: {author}, self.bavail_entry: {available}")

        #TODO: Make it verify and submit the entries
        #DONE
        try:
            int(code)
        except:
            print("DBG: Invalid values entered in self.bcode_entry")
            messagebox.showwarning("Incorrect Values", "Please enter correct values in the code box")
            return 0
        try:
            bool(available)
        except:
            print("DBG: Invalid values entered in self.bavail_entry")
            messagebox.showwarning("Incorrect Values", "Please enter correct values in the available box(0/1)")
            return 0
        if name.isspace() or author.isspace():
            print("DBG: Boxes cannot be empty")
            messagebox.showwarning("Incorrect Values", "Please enter correct values in the boxes")
            return 0
        else:
            try:
                s = f"INSERT INTO {table} VALUES (\"{name}\", {code}, \"{author}\", {available})" 
                self.cursor.execute(s)
                self.con.commit()
                messagebox.showinfo("Successful", "Row Successfully added into the table")
            except:
                print("DBG: Couldn't add row to DB")
                messagebox.showerror("Error", "Couldn't insert row into the database")
                return 0
w = Window(conc) #TESTING ONLY