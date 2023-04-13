# Construct a GUI and create the Python programs (using Pycharm/ Tkinter module in creating widgets) that
# allow you to type in your Given Name, Middle Name, and Last Name inside the three consecutive Entry widgets
# and display the full name inside the last Entry widget by clicking "Show Full Name" button.
# (Note: The output window must be exactly the same as below image)

from tkinter import *

win = Tk()
win.geometry("300x200+10+20")
win.title("Midterm in OOP")

L1=Label( text="Enter your Full Name :", font=44, fg = "Blue")
L1.grid(row=0, column=0)
L1=Label( text="", font=40)
L1.grid(row=1, column=0)

E1=Entry(win)
E1.grid(row=0, column=1)

def C1():
    E1.insert(0, "")
    L2=Label(LF, text=E1.get())
    L2.pack()


B1=Button(win, text="Click to Display Full Name :", font=55, command=C1, fg="Blue")
B1.grid(row=1, column=0)

LF=Label(win)
LF.grid(row=1, column=1)

win.mainloop()