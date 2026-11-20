from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Mathematical table generator")

title = Label(window, text = "Mathematical table")
caption = Label(window, text = "Number and Range")

title.grid(row = 0, column = 0, columnspan = 3, pady =25)
caption.grid(column = 0, row = 1, padx =10)


