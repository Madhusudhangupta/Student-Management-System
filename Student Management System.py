import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Management")

connection = sqlite3.connect('management.db')

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
YEAR = "year"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + YEAR + " INTEGER, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

appLabel = tk.Label(root, text="Student Management System", fg="red", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

class Student:
    studentName = ""
    collegeName = ""
    year = 0
    phoneNumber = 0
    address = ""

    def __init__(self, studentName, collegeName, year, phoneNumber, address):
        self.studentName = studentName
        self.collegeName = collegeName
        self.year = year
        self.phoneNumber = phoneNumber
        self.address = address

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Roboto", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                        font=("Roboto", 12)).grid(row=2, column=0, padx=(10,0))
yearLabel = tk.Label(root, text="Enter your year", width=40, anchor='w',
                        font=("Roboto", 12)).grid(row=3, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Roboto", 12)).grid(row=4, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Roboto", 12)).grid(row=5, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 30)
collegeEntry = tk.Entry(root, width = 30)
yearEntry = tk.Entry(root, width = 30)
phoneEntry = tk.Entry(root, width = 30)
addressEntry = tk.Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
collegeEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
yearEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=4, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=5, column=1, padx=(0,10), pady = 20)

def takeNameInput():
    global nameEntry, collegeEntry, yearEntry, phoneEntry, addressEntry
    # global username, collegeName, year, phone, address
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, YEAR, STUDENT_ADDRESS, STUDENT_PHONE

    username = nameEntry.get()
    nameEntry.delete(0, tk.END)

    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)

    year = int(yearEntry.get())
    yearEntry.delete(0, tk.END)

    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)

    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_COLLEGE + ", " + YEAR + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_PHONE + " ) VALUES ( '"
                       + username + "', '" + collegeName + "', '" + str(year) + "', '" +
                       address + "', " + str(phone) + " ); ")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Saved Data")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                        fg="red", width=40)
    appLabel.config(font=("Roboto", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four", "five")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Year")
    tree.heading("four", text="Address")
    tree.heading("five", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="" + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4], row[5]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()



button = tk.Button(root, text="Save Data", command=lambda :takeNameInput())
button.grid(row=6, column=0, pady=30)

displayButton = tk.Button(root, text="Show result", command=lambda :destroyRootWindow())
displayButton.grid(row=6, column=1)

root.mainloop()