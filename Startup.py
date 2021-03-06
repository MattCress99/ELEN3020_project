from tkinter import *
import tkinter as tk
from tkinter.font import Font
import sqlite3
import User_CredentialCheck, GuestLogin, Customer_UI

def Start_Window(conn):
    start_window = Tk()
    text = tk.Text(start_window)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    # start_window.geometry("300x300")
    start_window.title("START")
    start_window["bg"] = 'cadet blue'



    
    def Employee_Window():
        start_window.destroy()
        User_CredentialCheck.Check_Window(conn)

    def Guest_Window():
        start_window.destroy()
        GuestLogin.LoginScreen(conn)

    def Customer_Window():
        start_window.destroy()
        Customer_UI.ShowSampleTypes(conn)

    def Exit():
        start_window.destroy()

    employeeButton = Button(start_window, text="Employee", font = myFont, command=Employee_Window, height=1, width=8)#, bg="mint cream")
    guestButton = Button(start_window, text="Guest", font = myFont, command=Guest_Window, height=1, width=8)#, bg="mint cream")
    info = Label(start_window, text="Please select Employee or Guest to go to login", font = myFont, bg = 'cadet blue')
    customerButton = Button(start_window, text = "Customer", font = myFont, command = Customer_Window, height = 1, width = 8)#, bg="mint cream")
    exitButton = Button(start_window, text="Exit", font = myFont, command=Exit, height=1, width=8)#, bg="mint cream")

    info.grid(row=0, column=0)
    employeeButton.grid(row=1, column=0)
    guestButton.grid(row=2, column=0)
    customerButton.grid(row=3, column = 0)
    exitButton.grid(row=4, column=0)

    start_window.mainloop()

