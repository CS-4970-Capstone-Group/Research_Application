from tkinter import *
import tkinter as tk

root =tk.Tk()

mystring =tk.StringVar(root)
def getvalue():
    print(mystring.get())

root.mainloop()