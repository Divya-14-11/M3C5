from tkinter import*
from PIL import Image,ImageTk
window=Tk()
window.geometry("800x800")
upload=Image.open("1.jpg")
image=ImageTk.PhotoImage(upload)
l=Label(window,image=image,height=570,width=300)
l.place(x=50,y=50)
l1=Label(window,text="landscape")
l1.place(x=50,y=670)
window.mainloop()