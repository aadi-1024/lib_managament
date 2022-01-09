import tkinter as tk
from tkinter import ttk #To provide better integrated widgets
from tkinter import messagebox
import mysql.connector
#IGNORE ALL PRINT FUNCTIONS THEY ARE FOR DEBUGGING PURPOSES ONLY

class Window:
    #TODO: fix button commands to accept functions with args
    #DONE, I think
    def __init__(self, con, database, table): #initialiser
        self.cursor = con.cursor() #SQL stuff
        self.con = con
        self.database = database
        self.table = table

        #Front end stuff -->
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
        self.label1 = ttk.Label(self.root, text="Lookup Entry:")
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
        #DB stats -->
        self.stat_label = ttk.Label(self.root, text="Show Status:")
        self.stat_but = tk.Button(self.root, text="Show", command=self.stats)
        self.stat_label.place(x=55, y=380)
        self.stat_but.place(x=70, y=405)
        self.setup_db()

    def setup_db(self):
        print(f"DBG: Setup DB called with args: {self.table}")
        try:
            self.cursor.execute(f"USE {self.database}")
        except:
            print("DBG: Required DB does not exist")
            messagebox.showerror("Fatal", "Required Database does not exist")
            self.root.quit()

        self.cursor.execute("SHOW TABLES")
        if self.table in self.cursor.fetchone():
            print(f"DBG: Found table {self.table}")
        else:
            messagebox.showerror("Fatal", f"Couldnt find table {self.table}")
            self.root.quit()

    def query(self): #default only temporary till TODO:8 is done
        #DONE more or less
        print("DBG: query called")
        #Supposed to read input from self.lookupEntry and
        #query the database

        temp = self.lookupEntry.get()
        print(f"DBG: Value returned from self.lookupEntry: {temp}")

        #TODO: Integrate query with DB and return result using
        #tk.messagebox
        #DONE
        self.cursor.execute(f"SELECT * FROM {self.table} WHERE name = \"{self.lookupEntry.get()}\"")
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

    def stats(self):
        print(f"DBG: stats called with args table: {self.table}")
        try:
            self.cursor.execute(f"SELECT * FROM {self.table}")
            temp = self.cursor.fetchall()
            #Counting available books
            available_books = 0
            for i in temp:
                if i[3] == 1:
                    available_books += 1

            messagebox.showinfo("Status", f"No. of books: {len(temp)}\nBooks Available: {available_books}")
        except:
            print("DBG: Error while trying to communicate with server")
            messagebox.showerror("Error", "Couldnt communicate with the server")
            return 0