# from tkinter import messagebox
import tkinter as tk
import gui
import mysql.connector
#again ignore the print statements they are solely for debugging

def get_creds():
    root = tk.Tk()
    root.geometry("230x170")
    root.resizable = False
    root.title("Enter Creds")

    uname = tk.Label(root, text="Username:")
    passw = tk.Label(root, text="Password:")
    uname_enter = tk.Entry(root)
    passw_enter = tk.Entry(root)
    submit = tk.Button(root, text="Submit")

    uname.place(x=15, y=25)
    uname_enter.place(x=35, y=50)
    passw.place(x=15, y=75)
    passw_enter.place(x=35, y=100)
    submit.place(x=70, y=130)
    root.mainloop()
get_creds()
"DISCARDED APPROACHING ANOTHER WAY"
# try:
#     #TODO: make authentication safer by removing preset password
#     connector = mysql.connector(host="127.0.0.1", user="aaditya", password="evangelion")
# except:
#     print(f"DBG: Fatal, connection to database failed. Check whether mysqld is running and username and password is correct")
#     messagebox.showerror("Fatal Error", message="Couldnt connect to MySQL server. Terminating")
"DISCARDED CODE ^"
#w1 = gui.Window() #calling main window