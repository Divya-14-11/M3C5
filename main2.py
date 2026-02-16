from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window=Tk()
window.geometry("200x200")
def displaymessage():
    messagebox.showwarning("alert","stock virus found")
b=Button(window,text="scan for virus",command=displaymessage)
b.pack()
window.mainloop()