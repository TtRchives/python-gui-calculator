#Import necessary modules
from tkinter import *
from tkinter import Tk, ttk
import csv
import tkinter
import tkinter.messagebox
import tkinter.simpledialog #https://stackoverflow.com/questions/43149229/tkinter-input-and-output-in-python-3
root = Tk()
root.title("gPalc")
def askFirstNumber():
    num1=tkinter.simpledialog.askstring("Number One: ", "Type the first number: ")
def askSecondNumber():
    num2=tkinter.simpledialog.askstring("Number two: ", "Type the second number: ")
def askNumber(func):
    num=tkinter.simpledialog.askstring("Number", "Type the number to be " +func)
output=values()
#def __init__(self, parent, controller):
#    tkinter.Frame.__init__(self, parent)
#    self.controller = controller
#    button = ttk.Button(self, text="Submit", command=tkmessagebox.showinfo("Results",output))
root.mainloop()