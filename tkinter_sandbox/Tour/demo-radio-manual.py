"""
select() deselect()

переключатели, сложный способ (без переменных)
обратите внимание, что метод deselect переключателя просто устанавливает пустую
строку в качестве его значения, поэтому нам по-прежнему требуется присвоить
переключателям уникальные значения или использовать флажки;
"""
from tkinter import *

state = ''
buttons = []


def onPress(i):
    global state
    state = i
    for btn in buttons:
        btn.deselect()
    buttons[i].select()


root = Tk()
for i in range(10):
    rad = Radiobutton(root, text=str(i),
                      value=str(i), command=(lambda i=i: onPress(i)))
    rad.pack(side=LEFT)
    buttons.append(rad)

onPress(0)  # первоначально выбрать первый переключатель
root.mainloop()
print(state)  # вывести информацию о состоянии перед выходом
