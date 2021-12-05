# import the library
from tkinter import *
from types import lambdaType

root = Tk()
root.title("Simple Calculator")
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def buttonClick(value):
    e.delete(0,END)
    e.insert(0,value)

# create the lable widget
button1 = Button(root, text="1",padx=40,pady=20,command=lambda: buttonClick(1),bg="#fff444").grid(row=3,column=0)
button2 = Button(root, text="2",padx=40,pady=20,command=lambda: buttonClick(2),bg="#fff444").grid(row=3,column=1)
button3 = Button(root, text="3",padx=40,pady=20,command=lambda: buttonClick(3),bg="#fff444").grid(row=3,column=2)

button4 = Button(root, text="4",padx=40,pady=20,command=lambda: buttonClick(4),bg="#fff444").grid(row=2,column=0)
button5 = Button(root, text="5",padx=40,pady=20,command=lambda: buttonClick(5),bg="#fff444").grid(row=2,column=1)
button6 = Button(root, text="6",padx=40,pady=20,command=lambda: buttonClick(6),bg="#fff444").grid(row=2,column=2)

button7 = Button(root, text="7",padx=40,pady=20,command=lambda: buttonClick(7),bg="#fff444").grid(row=1,column=0)
button8 = Button(root, text="8",padx=40,pady=20,command=lambda: buttonClick(8),bg="#fff444").grid(row=1,column=1)
button9 = Button(root, text="9",padx=40,pady=20,command=lambda: buttonClick(9),bg="#fff444").grid(row=1,column=2)

button0 = Button(root, text="0",padx=40,pady=20,command=lambda: buttonClick(0),bg="#fff444").grid(row=4,column=0)
buttonClear = Button(root, text="Clear",padx=79,pady=20,command=lambda: buttonClick(""),bg="#fff444").grid(row=4,columnspan=2,column=1)

buttonPlus = Button(root, text="+",padx=39,pady=20,command=lambda: buttonClick("+"),bg="#fff444").grid(row=5,column=0)
buttonEqual = Button(root, text="=",padx=91,pady=20,command=lambda: buttonClick("="),bg="#fff444").grid(row=5,columnspan=2,column=1)



# back it or shoving it on the screen
root.mainloop()
