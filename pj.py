import tkinter as tk
from tkinter import messagebox
import os


STUDENT_FILE = "students_records.txt"
TEACHER_FILE = "teachers_records.txt"

def add_student():
    name = entry_name.get()
    roll = entry_roll.get()
    grade = entry_grade.get()

    if name and roll and grade:
        with open(STUDENT_FILE,"a") as file:
            file.write(f"{roll},{name},{grade}\n")
        messagebox.showinfo("Success", "Student record added successfuly")
        entry_name.delete(0, tk.END)
        entry_roll.delete(0, tk.END)
        entry_grade.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all the fields.")

def view_students():
    if not os.path.exist(STUDENT_FILE)
        messagebox.showwarning("File Error", "No student records found")
        return
    

    window = tk.toplevel(root)
    window.title("View All Students")


    with open(STUDENT_FILE, "r")as file:
        records = file.readlines()

    records.sort(key=lambda x: x.split( ',')[0])
    for i, record in enumerate(records):
        roll, name, grade = record.strip().split(',')
        tk.Label(window, text = f"{i+1}.ROll: {roll}, Name: {name}, Grade: {grade}").pack()

def search_students():
    search_roll = entry_search.get()

    if not search_roll:
        messagebox.showwarning("Input Error", "Please enter a Roll No. ")
        return
    
    found = False
    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_File, "r")as file:
            records = file.readlines()

        for record in records:
            roll, name, grade = record.strip().split(',')
            if roll == search_roll:
                message.showinfo("Found", f"Roll: {roll}\nName: {name}\nGrade: {grade}")
                found =True
                break


    if not found:
        messagebox.showwarning("Not Found", "No student found that Roll No. ")

    
def delete_student():
    del_roll = entry_delete.get()

    if not del_roll:
        messagebox.showwarning("Input Error", "Please enter a Roll No")
        return

    if os.path.exists(STUDENT_FILE):
        with open(STUDENT_FILE, "r") as file:
            records = file.readlines()

        with open(STUDENT_FILE, "w")as file:
            deleted = False
            for record in records:
                roll,name,grade = record.strip().split(',')
                if roll ! =del_roll:
                    file.write(record)

                else:
                    deleted = True


            if deleted:
                messaagebox.showinfo("Success", "")        



            

                                                                                                                                                                                                                                                                                    