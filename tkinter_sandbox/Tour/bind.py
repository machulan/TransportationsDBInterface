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


def onMapWindow(event):
    print('Окно восстановлено')


def onUnmapWindow(event):
    print('Окно свернуто')

tkroot = Tk()
labelfont = ('courier', 20, 'bold')  # семейство, размер, стиль
widget = Label(tkroot, text='Hello bind world')
widget.config(bg='red', font=labelfont)  # красный фон, большой шрифт
widget.config(height=5, width=20)  # начальн. размер: строк,символов
widget.pack(expand=YES, fill=BOTH)
widget.bind('<Button-1>', onLeftClick)  # щелчок мышью
widget.bind('<Button-3>', onRightClick) # правая кнопка мыши
widget.bind('<Button-2>', onMiddleClick)  # средняя = обе на некот. мышах
widget.bind('<Double-1>', onDoubleLeftClick)  # двойной щелчок левой кнопкой
widget.bind('<B1-Motion>', onLeftDrag)  # щелчок левой кнопкой и перемещ.
widget.bind('<KeyPress>', onKeyPress)  # нажатие любой клавиши на клав.
widget.bind('<Up>', onArrowKey)  # нажатие клавиши со стрелкой
widget.bind('<Return>', onReturnKey)  # return/enter key pressed

widget.bind('<Map>', onMapWindow)
widget.bind('<Unmap>', onUnmapWindow)
widget.bind('<Escape>', lambda event: print('Escape pressed'))
widget.bind('<BackSpace>', lambda event: print('BackSpace pressed'))
widget.bind('<Tab>', lambda event: print('Tab pressed'))

widget.bind('<KeyPress-o>', lambda event: print('O pressed'))

ent = Entry(tkroot)
ent.pack()
ent.insert(END, 'x')
ent.insert(0, 'y')


widget.focus()  # или привязать нажатие клавиши
# к tkroot
tkroot.title('Click Me')
tkroot.mainloop()

# TODO ВИРТУАЛЬНЫЕ события <<PasteText>>

# <ButtonRelease> # отпускание кнопки мыши
# <ButtonPress> # нажатие кнопки мыши
# <Motion> # перемещение указателя мыши
# <Enter> # момент входа указателя мыши из области окна
# <Leave> # момент выхода указателя мыши из области окна
# <Configure> # изменени размеров окна, его положения
# <FocusIn> # когда виджет получает фокус ввода
# <FocusOut> # когда виджет теряет фокус ввода
# <Map> # сворачивание окна
# <Unmap> # восстановление окна
# <Escape> # при нажатии на ESC
# <BackSpace> # при нажатии на BACKSPACE
# <Tab> # при нажатии на TAB
# <Down> # нажатие на клавишу со стрелкой "ВНИЗ"
# <Left> # нажатие на клавишу со стрелкой "ВЛЕВО"
# <Right> # нажатие на клавишу со стрелкой "ВПРАВО"
# <Top> # нажатие на клавишу со стрелкой "ВВЕРХ"
# <B1-Motion> # перемещение указателя мыши при нажатой левой кнопке
# <KeyPress-a> # генерируется только при нажатии клавиши "a"
# <Key-a> # тоже самое
# <ButtonPress-1> # нажатие левой кнопки мыши
# <Button-1> # тоже самое
# <1> # тоже самое

# event :
# .char
# .x
# .y



