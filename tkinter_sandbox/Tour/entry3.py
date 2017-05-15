# StringVar, IntVar, DoubleVar и BooleanVar

"""
использует переменные StringVar
компоновка по колонкам: вертикальные координаты виджетов могут не совпадать
(смотрите entry2)
"""

from tkinter import *
from  tkinter_sandbox.Tour.quitter import Quitter

fields = 'Name', 'Job', 'Pay'


def fetch(variables):
    for variable in variables:
        print('Input => "%s" %s' % (variable.get(), type(variable.get())))  # извлечь из переменных


def makeform(root, fields):
    form = Frame(root)  # создать внешний фрейм
    left = Frame(form)  # создать две колонки
    rite = Frame(form)
    form.pack(fill=X)
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)  # растягивать по горизонтали

    variables = []
    for field in fields:
        lab = Label(left, width=5, text=field)  # добавить в колонки
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)  # растягивать по горизонтали
        var = StringVar()
        ent.config(textvariable=var)  # связать поле с переменной
        var.set('enter here')
        variables.append(var)
    return variables


if __name__ == '__main__':
    root = Tk()
    vars = makeform(root, fields)
    Button(root, text='Fetch', command=(lambda: fetch(vars))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: fetch(vars)))
    root.mainloop()
