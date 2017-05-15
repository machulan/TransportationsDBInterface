"""создает группу флажков, которые вызывают демонстрационные диалоги"""
from tkinter import *  # импортировать базовый набор виджетов
from tkinter_sandbox.Tour.dialogTable import demos  # импортировать готовые диалоги
from tkinter_sandbox.Tour.quitter import Quitter  # прикрепить к "себе" объект Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        self.tools()
        Label(self, text="Check demos").pack()

        self.vars = []
        for key in demos:
            var = IntVar()
            Checkbutton(self,
                        text=key,
                        variable=var,
                        command=demos[key]).pack(side=LEFT)
            self.vars.append(var)

    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')  # текущие значения флажков: 1 или 0
        print()

    def tools(self):
        frm = Frame(self)
        frm.pack(side=RIGHT)
        Button(frm, text='State', command=self.report).pack(fill=X)
        Quitter(frm).pack(fill=X)


if __name__ == '__main__':
    Demo().mainloop()
