# https://docs.python.org/2/library/ttk.html#ttk.Notebook

from tkinter import *
from tkinter.ttk import *

root = Tk()
notebook = Notebook(root)
notebook.config(width=200, height=200)
notebook.pack()

f = Frame(notebook)
f.pack()

l = Label(notebook, text='adlsfasdf')
l.pack()

notebook.add(f)
notebook.add(l)
notebook.tab(0, text="TANTA")
notebook.tab(1, text='LABEKE')

b = Button(f, text='AJSD:LKA')
b.pack()

sep = Separator(f)
sep.config(orient=HORIZONTAL)
sep.pack(expand=NO, fill=BOTH)

b2 = Button(f, text='AJSD:LKA')
b2.pack()

root.mainloop()