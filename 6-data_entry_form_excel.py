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
window.title("Data Entry Form")

frame = tk.Frame(window)
frame.pack()

#saving user info
user_info_frame = tk.LabelFrame(frame, text="user information") #label içindeki frame
user_info_frame.grid(row=0, column=0, pady=20, padx=10)

first_name_label = tk.Label(user_info_frame, text="First Name") #şimdi user_info_frame içersinde label oluşturduk çevreçeve içinde çerçeve
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row= 0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="age")
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tk.Label(user_info_frame, text="Nationality")
nationality_commbobox = ttk.Combobox(user_info_frame, values=["africa", "asia", "middle east","europe", "america"])
nationality_label.grid(row=2, column=1)
nationality_commbobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10 , pady=5)

#saving courses info

courses_frame = tk.LabelFrame(frame)
courses_frame.grid(row=1,column=0, sticky="news", padx=20, pady=10)

registered_label = tk.Label(courses_frame, text="Registration Status", )

reg_status_var = tk.StringVar(value="Not registered") #inside default val
registered_check = tk.Checkbutton(courses_frame, text="currently registered",
                                  variable= reg_status_var, onvalue= "Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_frame, text="# completed courses")
numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemester_label = tk.Label(courses_frame, text="# Semesters")
numsemester_spinbox = tk.Spinbox(courses_frame, from_=0, to= "infinity")
numsemester_label.grid(row=0, column=3 )
numsemester_spinbox.grid(row=1, column=3)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# Accept terms

terms_frame = tk.LabelFrame(frame, text=" terms and conductions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not accepted")
terms_check = tk.Checkbutton(terms_frame, text= " I accept the term and conductions",
                             variable=accept_var, onvalue="accepted", offvalue="not accepted")
terms_check.grid(row=0, column=0)

button = tk.Button(frame, text="Enter Data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()