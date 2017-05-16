"""
4 класса демонстрационных компонентов (вложенных фреймов) в одном окне;
в одном окне присутствуют также 5 кнопок Quitter, причем щелчок на любой из
них приводит к завершению программы; графические интерфейсы могут повторно
использоваться, как фреймы в контейнере, независимые окна или процессы;
"""
from tkinter import *
from tkinter_sandbox.Tour.quitter import Quitter

demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)  # импортировать по имени в виде строки
        part = module.Demo(root)  # прикрепить экземпляр
        part.config(bd=2, relief=GROOVE)  # или передать параметры
        # конструктору Demo()
        part.pack(side=LEFT, expand=YES, fill=BOTH)  # растягивать
        # вместе с окном
        parts.append(part)  # добавить в список


def dumpState():
    print('=' * 30)
    for part in parts:
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):  # вызвать метод report,
            part.report()  # если имеется
        else:
            print('none')


root = Tk()  # явно создать корневое окно
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
