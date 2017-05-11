from tkinter import *


def showPosEvent(event):
    print('Widget=%s X=%s Y=%s' % (event.widget, event.x, event.y))


def showAllEvent(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(attr, '=>', getattr(event, attr))


def onKeyPress(event):
    print('Got key press:', event.char)


def onArrowKey(event):
    print('Got up arrow key press')


def onReturnKey(event):
    print('Got return key press')


def onLeftClick(event):
    print('Got left mouse button click:', end=' ')
    showPosEvent(event)


def onRightClick(event):
    print('Got right mouse button click:', end=' ')
    showPosEvent(event)


def onMiddleClick(event):
    print('Got middle mouse button click:', end=' ')
    showPosEvent(event)
    showAllEvent(event)


def onLeftDrag(event):
    print('Got left mouse button drag:', end=' ')
    showPosEvent(event)


def onDoubleLeftClick(event):
    print('Got double left mouse click', end=' ')
    showPosEvent(event)
    tkroot.quit()


tkroot = Tk()
labelfont = ('courier', 20, 'bold')  # семейство, размер, стиль
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)  # красный фон, большой шрифт
widget.config(height=5, width=20)  # начальн. размер: строк,символов
widget.pack(expand=YES, fill=BOTH)
widget.bind('<Button-1>', onLeftClick)  # щелчок мышью
widget.bind('<Button-3>', onRightClick)
widget.bind('<Button-2>', onMiddleClick)  # средняя = обе на некот. мышах
widget.bind('<Double-1>', onDoubleLeftClick)  # двойной щелчок левой кнопкой
widget.bind('<B1-Motion>', onLeftDrag)  # щелчок левой кнопкой и перемещ.
widget.bind('<KeyPress>', onKeyPress)  # нажатие любой клавиши на клав.
widget.bind('<Up>', onArrowKey)  # нажатие клавиши со стрелкой
widget.bind('<Return>', onReturnKey)  # return/enter key pressed
widget.focus()  # или привязать нажатие клавиши
# к tkroot
tkroot.title('Click Me')
tkroot.mainloop()
