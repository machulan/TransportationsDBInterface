"""создает два связанных ползунка для запуска демонстрационных диалогов"""
from tkinter import *  # импортировать базовый набор виджетов
from tkinter_sandbox.Tour.dialogTable import demos  # обработчики событий
from tkinter_sandbox.Tour.quitter import Quitter  # прикрепить к "себе" объект Quitter


class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Scale demos").pack()
        self.var = IntVar()
        Scale(self, label='Pick demo number',
              command=self.onMove,  # перехватывать перемещения
              variable=self.var,  # отражает положение
              from_=0, to=len(demos) - 1).pack()
        Scale(self, label='Pick demo number',
              command=self.onMove,  # перехватывать перемещения
              variable=self.var,  # отражает положение
              from_=0, to=len(demos) - 1,
              length=200, tickinterval=1,
              showvalue=YES, orient=HORIZONTAL).pack()
        Quitter(self).pack(side=RIGHT)
        Button(self, text="Run demo", command=self.onRun).pack(side=LEFT)
        Button(self, text="State", command=self.report).pack(side=RIGHT)

    def onMove(self, value):
        print('in onMove', value)

    def onRun(self):
        pos = self.var.get()
        print('You picked', pos)
        demo = list(demos.values())[pos]  # отображение позиции на ключ
        # (представление в версии 3.X)
        print(demo())  # или
        # demos[ list(demos.keys())[pos] ]()

    def report(self):
        print(self.var.get())


if __name__ == '__main__':
    print(list(demos.keys()))
    Demo().mainloop()
