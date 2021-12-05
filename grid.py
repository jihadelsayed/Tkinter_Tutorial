# import the library
from tkinter import *


# create the root widget
root = Tk()
# create the lable widget
myLable = Label(root, text="hello world") # (the window, the text)
def showName():
    myLable2 = Label(root, text="My name is Jihad") # (the window, the text)
    myLable2.grid(row=1,column=0)

myButton = Button(root, text="Click here!",state=DISABLED,padx=50,pady=50,command=showName) # (the window, the text,the status,size)
myButton2 = Button(root, text="Click here!",command=showName,fg="blue",bg="#fff444") # (the window, the text,the status,size)

# back it or shoving it on the screen
myLable.grid(row=0,column=0)
myButton.grid(row=2,column=2)
myButton2.grid(row=3,column=3)

root.mainloop()

