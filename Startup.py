from tkinter import *
import sqlite3
import DataAPI
import SetupAPI
import GuestLogin
import User_CredentialCheck

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

SetupAPI.CreateAllTables(conn) 

DataAPI.LogoutAll(conn)


def Start_Window():
    start_window = Tk()  
    #start_window.geometry("300x300")
    start_window.title("START")

    def Employee_Window():
        start_window.destroy()
        User_CredentialCheck.Check_Window()

    def Guest_Window():
        start_window.destroy()
        GuestLogin.LoginScreen()

    def Exit():
        start_window.destroy()

    employeeButton = Button(start_window, text = "Employee", command = Employee_Window)
    guestButton = Button(start_window, text = "Guest", command = Guest_Window)
    info = Label(start_window, text = "Please select Employee or Guest to go to login")
    exitButton = Button(start_window, text = "Exit", command = Exit)

    info.grid(row = 0, column = 0)
    employeeButton.grid(row = 1, column = 0)
    guestButton.grid(row = 2, column = 0)
    exitButton.grid(row = 3, column = 0)

    start_window.mainloop()

Start_Window()



