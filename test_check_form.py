import tkinter as tk
from tkinter import ttk #temalar var
from tkinter import messagebox
import openpyxl
import os

def enter_data():

    accepted = accept_var.get()

    if accepted == "accepted" :
        #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname :
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_commbobox.get()

            #courses info
            numcourses = numcourses_spinbox.get()
            numsemester = numsemester_spinbox.get()
            registration_status = reg_status_var.get()


            print("first name: ", firstname, "\nlast name: ", lastname)
            print("Title: ",title, "\nAge: ",age, "\nNationality: ", nationality)
            print("Courses: ", numcourses, "Semester: ", numsemester)
            print("Registration status: ", registration_status)
            print("-----------------------------")

            filepath = r"C:\Users\Sinan\Desktop\Coding\Python\Tk-gui-projects\data.xlsx"


            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet =workbook.active
                heading = ["First Name", "Last Name", "Title", "Age", "Nationality",
                           "#courses", "# Somesters", "Registration Status"]
                sheet.append(heading)
                workbook.save(filepath)

            workbook = openpyxl.load_workbook(filepath)
            sheet =workbook.active
            sheet.append([firstname, lastname, title, age, nationality, numcourses,
                         numsemester, registration_status])
            workbook.save(filepath)

        else:
            tk.messagebox.showwarning(title="ERROR", message="Firstname and lastname required ")

    else:
        tk.messagebox.showwarning(title="ERROR", message="You have not accepted the terms")

window = tk.Tk()
window.title("Device Test Entry Form")

frame = tk.Frame(window)
frame.pack()

#saving user info
user_info_frame = tk.LabelFrame(frame, text="RFID DEVICE INFO") #label içindeki frame
user_info_frame.grid(row=0, column=0, pady=20, padx=10, sticky="news")

first_name_label = tk.Label(user_info_frame, text="Model Code") #şimdi user_info_frame içersinde label oluşturduk çevreçeve içinde çerçeve
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="MAC ADRESS")
last_name_label.grid(row= 2, column=0)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=3, column=0)

title_label = tk.Label(user_info_frame, text="Personnel Name")
title_combobox = ttk.Combobox(user_info_frame, values=["","Sinan", "Personnel-1", "Personnel-2"])
title_label.grid(row=0, column=1)
title_combobox.grid(row=1, column=1)


for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10 , pady=5)

#saving courses info

courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1,column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(courses_frame, text="Device Status")

reg_status_var = tk.StringVar(value="PASS") #inside default val
registered_check = tk.Checkbutton(courses_frame, text="PASS QC",
                                  variable= reg_status_var, onvalue= "PASS QC", offvalue="PROBLEM!")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_frame, text="# Device problem")
numcourses_spinbox = tk.Entry(courses_frame)
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms



button = tk.Button(frame, text="Enter Data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()