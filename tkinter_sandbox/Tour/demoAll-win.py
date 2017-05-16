"""
4 демонстрационных класса в независимых окнах верхнего уровня;
не процессы: при завершении одного щелчком на кнопке Quit завершаются все
остальные, потому что все окна выполняются в одном и том же процессе; здесь
первое окно Tk создается вручную, иначе будет создано пустое окно
"""
from tkinter import *

demoModules = ['demoDlg', 'demoRadio', 'demoCheck', 'demoScale']


def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname)  # импортировать по имени в виде строки
        window = Toplevel()  # создать новое окно
        demo = module.Demo(window)  # родительским является новое окно
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects


def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()


root = Tk()  # явно создать корневое окно
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()
