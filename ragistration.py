
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

r = Tk()
r.title("REGISTRATION FORM")
r.geometry("750x850")
r.configure(bg="#EEF2F6")
'''
with open("student_ragistration.txt","w")as f:
    f.write()
'''
def display_data():

    if un.get() == "" or em.get() == "" or nm.get() == "" or p1.get() == "" or p2.get() == "" :
        messagebox.showerror("ERROR", "Please fill all the information!")

    elif not nm.get().isdigit() or len(nm.get()) != 10  :
        messagebox.showerror("ERROR", "Invalid phone number!")

    elif p1.get() != p2.get():
        messagebox.showerror("ERROR", "Verify password does not match!")
    

    #elif gender.get()=="male":
       # messagebox.showinfo("gender","male is selected")

    #elif gender.get()=="male":
       # messagebox.showinfo("gender","female is selected")
    # else:
    #     print("STUDENT REGISTRATION SUCCESSFULLY")
    #     print("Username:", un.get())
    #     print("gender :",gender.get())
    #     print("Email:", em.get())
    #     print("Number:", nm.get())
    #     print("Password:", p1.get())
    #     print("Verify Password:", p2.get())

    skills = ""
    if python_var.get()==1:
        skills+="python"
    if javascrpit_var.get()==1:
        skills+=","+"javascrpit"
    if SQL_var.get()==1:
        skills+=","+"SQL"
    if Excel_var.get()==1:
        skills+=","+"Excel"    


    s = ""
    s+=un.get()+"\t"+em.get()+"\t"+str(nm.get())+"\t"+p1.get()+"\t"+gender.get()+"\t"+skills+"\t"+edu_var.get()+"\t"+str(age_var.get())+"\n"    
    try:
        with open("student_ragistration.txt","a")as f:
            f.write(s)
            f.close()                  
        messagebox.showinfo("hello","ragister succesfully")
    except Exception as e:
          messagebox.showerror("Error", str(e))



un = StringVar()
em = StringVar()
nm = StringVar()
p1 = StringVar()
p2 = StringVar()
gender = StringVar()
python_var = IntVar(value=0)
SQL_var = IntVar(value=0)
javascrpit_var = IntVar(value=0)
Excel_var = IntVar(value=0)
edu_var = StringVar(value="none")
age_var = IntVar(value=18)


L = Label(r, text="REGISTRATION FORM !",font=("Arial", 25, "bold"),padx=10, pady=10, fg="green")
L.grid(columnspan=2)
#justify="left",anchor="w",width=25
L1 = Label(r, text="Enter Name:",font=("Arial", 20, "bold"), padx=10, pady=10)
L1.grid(row=1, column=0)
username = Entry(r, font=("Arial", 20, "bold"), textvariable=un)
username.grid(row=1, column=1)

L01 = Label(r,text="selct gender :",font=("Arial", 20, "bold"))
L01.grid(row=2,column=0)

m = Radiobutton(r,text="male",font=("Arial", 20, "bold"),value="male",variable=gender)
m.grid(row=3,column=1)
f = Radiobutton(r,text="female",font=("Arial", 20, "bold"),value="female",variable=gender)
f.grid(row=3,column=0)

L02 = Label(r,text="select Skill !",font=("Arial", 20, "bold"))
L02.grid(row=4,column=0)

p = Checkbutton(r,text="python",font=("Arial", 20, "bold"),variable=python_var)
p.grid(row=5,column=0)

j = Checkbutton(r,text="javascript",font=("Arial", 20, "bold"),variable=javascrpit_var)
j.grid(row=5,column=1)

s = Checkbutton(r,text="SQL",font=("Arial", 20, "bold"),variable=SQL_var)
s.grid(row=6,column=0)

e= Checkbutton(r,text="Excel",font=("Arial", 20, "bold"),variable=Excel_var)
e.grid(row=6,column=1)

L2 = Label(r, text="Enter Email:",font=("Arial", 20, "bold"), padx=10, pady=10)
L2.grid(row=7, column=0)
Email = Entry(r, font=("Arial", 20, "bold"), textvariable=em)
Email.grid(row=7, column=1)

L3 = Label(r, text="Enter Phone Number:",font=("Arial", 20, "bold"), padx=10, pady=10)
L3.grid(row=8, column=0)
number = Entry(r, font=("Arial", 20, "bold"), textvariable=nm)
number.grid(row=8, column=1)

L4 = Label(r, text="Enter Password:",font=("Arial", 20, "bold"), padx=10, pady=10)
L4.grid(row=9, column=0)
password = Entry(r, font=("Arial", 20, "bold"),show="*", textvariable=p1)
password.grid(row=9, column=1)

L5 = Label(r, text="Verify Password:",font=("Arial", 20, "bold"), padx=10, pady=10)
L5.grid(row=10, column=0)
password2 = Entry(r, font=("Arial", 20, "bold"),show="*", textvariable=p2)
password2.grid(row=10, column=1)

#COMBOBOX
L6 = Label(r,text="select education",font=("Arial", 20, "bold"), padx=10, pady=10)
L6.grid(row=11,column=0)
Education = ttk.Combobox(r,values=["HSC","SSC","diploma","BE","BCS"],textvariable=edu_var)
Education.grid(row=11,column=1)                                


# spinbox
L7 = Label(r,text="select age",font=("Arial", 20, "bold"), padx=10, pady=10)
L7.grid(row=12,column=0)
age = Spinbox(r,from_=18,to= 30, textvariable=age_var)
age.grid(row=12,column=1)

Button1 = Button(r, text="SUBMIT",font=("Arial", 15, "bold"),padx=10, pady=10, fg="green",bg="white", command=display_data)
Button1.grid(row=13, column=0)

Button2 = Button(r, text="EXIT",font=("Arial", 15, "bold"),padx=10, pady=10, fg="red",bg="white", command=r.destroy)
Button2.grid(row=13, column=1)



r.mainloop()