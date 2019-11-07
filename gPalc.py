#Import necessary modules
from tkinter import *
from tkinter import Tk, ttk
import csv
import tkinter
import tkinter.messagebox
import tkinter.simpledialog #https://stackoverflow.com/questions/43149229/tkinter-input-and-output-in-python-3
root = Tk()
root.title("gPalc")
file=tkinter.simpledialog.askstring("Number One: ", "Type the first number: ")
def values():
    print("Some text")
output=values()
def __init__(self, parent, controller):
    tkinter.Frame.__init__(self, parent)
    self.controller = controller
    button = ttk.Button(self, text="Submit", command=tkmessagebox.showinfo("Results",output))
root.mainloop()