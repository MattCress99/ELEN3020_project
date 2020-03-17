import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

##########---------->    START: WINDOW FOR ADDING BOXES <----------##########
def AddBox_Window():
    def CreateBox():
        try:
            _boxID = boxID.get()
            _fridgeID = fridgeID.get()
            _boxX = int(boxX.get())
            _boxY = int(boxY.get())
            _boxZ = int(boxZ.get())
            print(DataAPI.AddBox(conn, _boxID, _fridgeID, _boxX, _boxY, _boxZ))
        except:
            print("ERROR: Invalid data entered")
        
    def console_PrintBox():
        print("Box ID: %s\nFridge ID: %s\nBox X: %s\nBox Y: %s\nBox Z: %s" % 
                    (boxID.get(), fridgeID.get(), boxX.get(), boxY.get(), boxZ.get()))

    def Open_MainBox_Window():
        window_AddBox.destroy()
        MainBox_Window()
      
    window_AddBox = tk.Tk()
    #window_AddBox.geometry("300x300")
    window_AddBox.title("ADD BOX")

    tk.Label(window_AddBox, text = "Box ID").grid(row = 0)
    boxID = tk.Entry(window_AddBox)
    boxID.grid(row = 0, column = 1)

    tk.Label(window_AddBox, text = "Fridge ID").grid(row = 1)
    fridgeID = tk.Entry(window_AddBox)
    fridgeID.grid(row = 1, column = 1)

    tk.Label(window_AddBox, text = "Box X").grid(row = 2)
    boxX = tk.Entry(window_AddBox)
    boxX.grid(row = 2, column = 1)

    tk.Label(window_AddBox, text = "Box Y").grid(row = 3)
    boxY = tk.Entry(window_AddBox)
    boxY.grid(row = 3, column = 1)

    tk.Label(window_AddBox, text = "Box Z").grid(row = 4)
    boxZ = tk.Entry(window_AddBox)
    boxZ.grid(row = 4, column = 1)

    tk.Button(window_AddBox, text = 'Print Box to Console', 
                        command = console_PrintBox).grid(row = 7, column=1)
    tk.Button(window_AddBox, text = 'Add Box', command = CreateBox).grid(row = 8, column=1)

    tk.Button(window_AddBox, text = 'Back to Box Menu', 
                        command = Open_MainBox_Window).grid(row = 10, column=1)

    window_AddBox.mainloop()
##########---------->    END: WINDOW FOR ADDING BOXES <----------##########

##########---------->    START: WINDOW FOR MOVING BOXES <----------##########
def MoveBox_Window():
    def MoveBox():
        try:
            _boxID = boxID.get()
            _fridgeID = fridgeID.get()
            print(DataAPI.MoveBox(conn, _boxID, _fridgeID))
        except:
            print("ERROR: Invalid data entered")

    def Open_MainBox_Window():
        window_MoveBox.destroy()
        MainBox_Window()

    window_MoveBox = tk.Tk()
    #window_MoveBox.geometry("300x300")
    window_MoveBox.title("MOVE BOX")

    tk.Label(window_MoveBox, text = "Move box with BoxID:").grid(row = 0)
    boxID = tk.Entry(window_MoveBox)
    boxID.grid(row = 0, column = 1)

    tk.Label(window_MoveBox, text = "To fridge with FridgeID:").grid(row = 1)
    fridgeID = tk.Entry(window_MoveBox)
    fridgeID.grid(row = 1, column = 1)

    tk.Button(window_MoveBox, text = 'Move Box', command = MoveBox).grid(row = 5, column=1)
    tk.Button(window_MoveBox, text = 'Back to Box Menu', 
                        command = Open_MainBox_Window).grid(row = 10, column=1)

    window_MoveBox.mainloop()
##########---------->    END: WINDOW FOR MOVING BOXES <----------##########

##########---------->    START: WINDOW FOR DELETING BOXES <----------##########
def DeleteBox_Window():
    def DeleteBox():
        try:
            _boxID = boxID.get()
            _fridgeID = fridgeID.get()
            print("HAVEN'T MADE DELETE FUNCTION YET")
        except:
            print("ERROR: Invalid data entered")

    def Open_MainBox_Window():
        window_DeleteBox.destroy()
        MainBox_Window()

    window_DeleteBox = tk.Tk()
    #window_DeleteBox.geometry("300x300")
    window_DeleteBox.title("DELETE BOX")

    tk.Label(window_DeleteBox, text = "Delete box with BoxID: ").grid(row = 0)
    boxID = tk.Entry(window_DeleteBox)
    boxID.grid(row = 0, column = 1)

    tk.Label(window_DeleteBox, text = "From fridge with FridgeID: ").grid(row = 1)
    fridgeID = tk.Entry(window_DeleteBox)
    fridgeID.grid(row = 1, column = 1)

    tk.Button(window_DeleteBox, text = 'Delete Box', command = DeleteBox).grid(row = 5, column=1)
    tk.Button(window_DeleteBox, text = 'Back to Box Menu', 
                        command = Open_MainBox_Window).grid(row = 10, column=1)

    window_DeleteBox.mainloop()
##########---------->    END: WINDOW FOR DELETING BOXES <----------##########

##########---------->    START: MAIN WINDOW FOR BOXES <----------##########
def MainBox_Window():
    window_MainBox = tk.Tk()
    window_MainBox.geometry("300x300")
    window_MainBox.title("BOX MENU")

    def Open_AddBox_Window():
        window_MainBox.destroy()
        AddBox_Window()

    def Open_MoveBox_Window():
        window_MainBox.destroy()
        MoveBox_Window()

    def Open_DeleteBox_Window():
        window_MainBox.destroy()
        DeleteBox_Window()

    tk.Button(window_MainBox, text = 'Add Box', 
                        command = Open_AddBox_Window).grid(row = 0, column=0)
    tk.Button(window_MainBox, text = 'Move Box', 
                        command = Open_MoveBox_Window).grid(row = 1, column=0)
    tk.Button(window_MainBox, text = 'Delete Box', 
                        command = Open_DeleteBox_Window).grid(row = 2, column=0)

    window_MainBox.mainloop()
##########---------->    END: MAIN WINDOW FOR BOXES <----------##########




SetupAPI.CreateAllTables(conn)   
MainBox_Window()
