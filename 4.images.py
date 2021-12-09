# import the library
from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.iconbitmap('icon.ico')
button_quit = Button(root, text="Exit Program", command=root.quit)
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def buttonClick(value):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(value))




# back it or shoving it on the screen
root.mainloop()

