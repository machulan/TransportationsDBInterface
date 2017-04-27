import tkinter
from tkinter.messagebox import showinfo
from tkinter_sandbox.tkinter1 import MyGui


class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Ouch!')


if __name__ == '__main__':
    CustomGui().pack()
    tkinter.mainloop()
