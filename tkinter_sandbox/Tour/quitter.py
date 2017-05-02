"""
кнопка Quit, которая запрашивает подтверждение на завершение;
для повторного использования достаточно прикрепить экземпляр к другому
графическому интерфейсу и скомпоновать с желаемыми параметрами
"""

from tkinter import *
from tkinter.messagebox import askokcancel


class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')

        # import tkinter
        # ans2 = tkinter.messagebox.askquestion('TITLE', "MESSAGE")
        # print(ans2)
        # ans3 = tkinter.messagebox.askretrycancel('TITLE3', 'message3')
        # print(ans3)
        # ans4 = tkinter.messagebox.askyesnocancel('TITLE4', 'message4')
        # print(ans4)

        if ans:
            Frame.quit(self)


if __name__ == '__main__':
    Quitter().mainloop()
