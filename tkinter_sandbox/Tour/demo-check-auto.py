# проверка состояния флажков, простой способ

from tkinter import *

root = Tk()
states = []
for i in range(10):
    var = IntVar()
    chk = Checkbutton(root, text=str(i), variable=var)
    chk.pack(side=LEFT)
    states.append(var)
root.mainloop()  # пусть следит библиотека tkinter
print([var.get() for var in states])  # вывести все состояния при выходе
# (можно также реализовать с помощью
# функции map и lambda-выражения)
