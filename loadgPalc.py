from tkinter import *
from tkinter import tkMessageBox, Tk
import tkinter
load = Tk()
load.title("gPalc -- Loading")
Label(load, text="gPalc is loading -- please wait")
print("Loading")
load.mainloop()
exec("gPalc.py")