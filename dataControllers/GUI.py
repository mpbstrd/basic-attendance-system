from tkinter import *
from tkinter import messagebox
from tkinter import Label
from datetime import datetime
import time
import sys
from webbrowser import get

from numpy import inner

from teacher import Teacher
from department import Department
from attendance import Attendace

# BASIC COMPONENTS
gui = Tk()
gui.geometry("500x500")
gui.title('LOG IN')
gui.resizable(0,0)
now = datetime.now()
today = now.strftime("%d/%m/%Y %I:%M:%S %p")
gui['bg']="#FFD580"

# MAKES TIME
def get_time():
    timeVar = time.strftime('%I:%M:%S %p')
    label.config(text=timeVar)
    label.after(1000, get_time)
label = Label(gui, font=("Fivo Sans",20),background="#FFD580",foreground="black")
label.pack()
get_time()

# REGISTERS FOR TIME IN
def timein():

    # GUI THINGS
    Frame(gui,width=400,height=400,bg="white").place(x=50,y=50)
    l1=Label(gui,text="ENTER TEACHER ID",bg='White')
    l=('Montserrat',20)
    l1.config(font=l)
    l1.place(x=120,y=150)

    e1 = Entry(gui,width=20,border=2)
    e1.config(font=1)
    e1.place(x=160,y=230)

    # BACK END THINGS
    inn = e1.get()
    t = Teacher()
    temp = t.idExists(inn)

    def cmd():
        messagebox.showinfo("inn")

        if temp == True:
            a = Attendace()
            if a.timein(inn) == True:
                messagebox.showinfo("LOGIN SUCCUESSFULLY!", today)
            else:
                messagebox.showinfo("LOGIN FAILED!!", str(e1.get())+" Unable to time in. Please try again")
        else:
            messagebox.showinfo("LOGIN FAILED!!", "Unable to identify user. Please try again")


    Button(gui,width=20,height=2,fg="white",bg="orange",border=0,command=cmd,text='SUBMIT').place(x=180,y=280)

def timeout():
    Frame(gui,width=400,height=400,bg="white").place(x=50,y=50)
    l1=Label(gui,text="ENTER TEACHER ID",bg='White')
    l=('Montserrat',20)
    l1.config(font=l)
    l1.place(x=120,y=150)

    e1 = Entry(gui,width=20,border=2)
    e1.config(font=1)
    e1.place(x=160,y=230)
    
    # BACK END THINGS
    inn = e1.get()
    t = Teacher()
    temp = t.idExists(str(inn))

    def cmd():
        if temp == True:
            a = Attendace()
            if a.timeout(inn) == True:
                messagebox.showinfo("LOGIN SUCCUESSFULLY!", today)
                gui.mainloop()
            else:
                messagebox.showinfo("LOGIN FAILED!!", "PLEASE TRY AGAIN")
        else:
            messagebox.showinfo("LOGIN FAILED!!", "PLEASE TRY AGAIN")


    Button(gui,width=20,height=2,fg="white",bg="orange",activebackground="#FFD580",border=0,command=cmd,text='SUBMIT').place(x=180,y=280)

Button(gui,width=27,height=25,fg="black",bg="white",command=timein,border=3,text='TIME IN').place(x=50,y=51)
Button(gui,width=25,height=25,fg="black",bg="white",command=timeout,border=3,text='TIME OUT').place(x=250,y=51)

gui.mainloop()