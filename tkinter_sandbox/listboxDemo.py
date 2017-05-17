from tkinter import *

root = Tk()

lb = Listbox(root)
lb.pack(expand=NO, fill=X)
lb.config(height=5)

f = Frame()
b = Button(f, text='BUTTTON')

li = ['asdf', 'weird', f]
for item in li:
    lb.insert(END, item)

root.mainloop()