from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Asad's Clock")

def time():
    string = strftime('%I:%M:%S %p')
    lable.config(text=string)
    lable.after(1000, time)

lable = Label(root, font=("ds_digital", 90), background = "black", foreground = "cyan")
lable.pack(anchor='center')
time()

mainloop()
