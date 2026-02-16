# CREATE A WINDOW WHICH SHOULD HAVE BUTTON SAYING CLACULATOR, WHEN YOU CLICK ON THE BUTTON IT SHOULD HAVE A TOP WINDOU AND IT SHOULD HAVE 4 BUTTON IN IT (ADDITION,SUB,MULTIPLICATION,SUB)
from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("500x500")
l=Label(window,text="this is the main window")
l.pack()
def addition():
    messagebox.showwarning("alert")
def subtraction():
    messagebox.showwarning("alert")
def multiplication():
    messagebox.showwarning("alert")
def division():
    messagebox.showwarning("alert")

def topwindow():
    top=Toplevel()
    top.geometry("300x300")
    l1=Label(top,text="this is the new window")
    l1.pack()
    b2=Button(top,text="addition",command=addition)
    b2.pack()
    b3=Button(top,text="subtraction",command=subtraction)
    b3.pack()
    b4=Button(top,text="multiplication",command=multiplication)
    b4.pack()
    b5=Button(top,text="division",command=division)
    b5.pack()
    top.mainloop()
b=Button(window,text="calculator",command=topwindow)
b.pack()
window.mainloop()