from tkinter import *
window=Tk()
window.geometry("400x400")
l=Label(window,text="this is root window")
def topwindow():
    top=Toplevel()
    top.geometry("200x200")
    top.title("top window")
    l1=Label(top,text="this is top level window")
    l1.pack()
    top.mainloop()

b=Button(window,text="click here to enter a new window",command=topwindow)
l.pack()
b.pack()
window.mainloop()