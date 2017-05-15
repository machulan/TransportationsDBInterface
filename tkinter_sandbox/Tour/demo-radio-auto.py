# переключатели, простой способ
from tkinter import *

root = Tk()  # IntVar также можно использовать
var = IntVar(0)  # выбрать 0-й переключатель при запуске
for i in range(10):
    rad = Radiobutton(root, text=str(i), value=i, variable=var)
    rad.pack(side=LEFT)
root.mainloop()
print(var.get())  # вывести информацию о состоянии перед выходом
