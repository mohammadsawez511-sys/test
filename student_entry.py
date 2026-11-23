from tkinter import *
import csv
from tkinter import ttk
from tkinter import messagebox


r = Tk()
r.title("STUDENT DATA")

def display():
    Dict = {"NAME": un.get(),"gender": gender.get(),"roll no": roll_var.get(),"class": cls_var.get(),"bio": bio_var.get(),"che": che_var.get(),"phy": phy_var.get() }

    with open("student_entry.csv", "a", newline="") as f:
        csvWriter = csv.DictWriter(f, fieldnames=Dict.keys())
        csvWriter.writerow(Dict)

    messagebox.showinfo("Success", "Data saved successfully!")

un = StringVar()
gender = StringVar()
roll_var = IntVar()
cls_var = StringVar()
bio_var = StringVar()
che_var = StringVar()
phy_var = StringVar()

L = Label(r, text="STUDENT ENTRY",font=("Arial", 20, "bold"),padx=10, pady=10, fg="green")
L.grid(columnspan=2)

L1 = Label(r,text="enter name :",font=("Arial", 20, "bold"),padx=10, pady=10)
L1.grid(row=1,column=0)

username = Entry(r,font=("Arial", 20, "bold"),textvariable=un)
username.grid(row=1,column=1)

m = Radiobutton(r,text="male",font=("Arial", 20, "bold"),value="male",variable=gender)
m.grid(row=2,column=0)
f = Radiobutton(r,text="female",font=("Arial", 20, "bold"),value="female",variable=gender)
f.grid(row=2,column=1)

L2= Label(r,text="select roll_no :",font=("Arial", 20, "bold"), padx=10, pady=10)
L2.grid(row=3,column=0)
roll = Spinbox(r,from_=1,to= 100,textvariable=roll_var)
roll.grid(row=3,column=1)

L3 = Label(r,text="enter your class :",font=("Arial", 20, "bold"))
L3.grid(row=4,column=0)
c = Entry(r,font=("Arial", 20, "bold"),textvariable=cls_var)
c.grid(row=4,column=1)

L4= Label(r, text="ENTER MARKS IN SUBJECTS",font=("Arial", 20, "bold"),padx=10, pady=10, fg="red")
L4.grid(columnspan=2)

L5 = Label(r,text="BIOLOGY :",font=("Arial", 20, "bold"))
L5.grid(row=6,column=0)
mark1 = Entry(r,font=("Arial", 20, "bold"),textvariable=bio_var)
mark1.grid(row=6,column=1)

L6 = Label(r,text="CHEMESTRY :",font=("Arial", 20, "bold"))
L6.grid(row=7,column=0)
mark2 = Entry(r,font=("Arial", 20, "bold"),textvariable=che_var)
mark2.grid(row=7,column=1)

L7= Label(r,text="PHYSICS :",font=("Arial", 20, "bold"))
L7.grid(row=8,column=0)
mark3 = Entry(r,font=("Arial", 20, "bold"),textvariable=phy_var)
mark3.grid(row=8,column=1)


button = Button(r,text="SUBMIT",font=("Arial", 10, "bold"),padx=35,pady=15,fg="green",bg="white",command=display)
button.grid(columnspan=2)
r.mainloop()
