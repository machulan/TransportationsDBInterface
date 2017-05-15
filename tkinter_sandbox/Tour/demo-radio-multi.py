# посмотрите, что произойдет, если несколько переключателей
# будут иметь одно и то же значение
from tkinter import *

root = Tk()
var = StringVar()
for i in range(10):
    rad = Radiobutton(root, text=str(i), variable=var, value=str(i % 3))
    # rad.config(bg='green')
    rad.pack(side=LEFT)
var.set(' ')  # все переключатели сделать невыбранными
root.mainloop()
