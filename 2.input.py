# import the library
from tkinter import *


# create the root widget
root = Tk()
# create the lable widget
myLable = Label(root, text="What is your name!") # (the window, the text)
field = Entry(root, width=50,borderwidth=5) # (the window, the text)
field.insert(0,"name is:")
myLable.pack()
def showName():
    myLable2 = Label(root, text="My "+field.get()) # (the window, the text)
    myLable2.pack()

myButton2 = Button(root, text="Click here!",command=showName,fg="blue",bg="#fff444") # (the window, the text,the status,size)
field.pack()

# back it or shoving it on the screen
myButton2.pack()
root.mainloop()

