import sys
from tkinter import *


def hello(event):
    print('Press twice to exit')  # одиночный щелчок левой кнопкой


def quit(event):  # двойной щелчок левой кнопкой
    print('Hello, I must be going...')  # event дает виджет, координаты и т.д.
    sys.exit()


widget = Button(None, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)  # привязать обработчик щелчка
widget.bind('<Double-1>', quit)  # привязать обработчик двойного щелчка
widget.mainloop()