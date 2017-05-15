# флажки, сложный способ (без переменных)

from tkinter import *

states = []  # изменение объекта – не имени


def onPress(i):  # сохраняет состояния
    states[i] = not states[i]  # изменяет False->True, True->False


root = Tk()
for i in range(10):
    chk = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)))
    chk.pack(side=LEFT)
    states.append(False)
root.mainloop()
print(states)  # при выходе вывести все состояния
