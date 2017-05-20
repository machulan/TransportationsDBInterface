from tkinter import *
import tkinter.tix as tix
from resourses.constants import *

root = tix.Tk()

tlist = tix.TList(root)
tlist.pack(expand=YES, fill=BOTH, side=LEFT)
tlist.config(orient=HORIZONTAL)
tlist.config(font=TABLE_NAME_FONT)

scrollbar = Scrollbar(root)
scrollbar.config(orient=VERTICAL)

scrollbar.config(command=tlist.yview)
tlist.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)

for i in range(30):
    tlist.insert(END, text=i)

root.mainloop()