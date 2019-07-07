'''
tkinter tutorial 
https://www.tutorialspoint.com/python/python_gui_programming
'''


from tkinter import *
from tkinter import messagebox

top = Tk()


def helloCallBack():
    messagebox.showinfo("Title", "a Tk MessageBox")


B = Button(top, text="Hello", command=helloCallBack)

B.pack()
top.mainloop()
