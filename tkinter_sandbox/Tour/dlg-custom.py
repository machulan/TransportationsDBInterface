#!/usr/bin/python
# coding=UTF-8

# Модальный диалог, focus_set(), grab_set(), wait_window()

import sys
import tkinter
from tkinter import *

sys.argv.extend([2, 5])
print(sys.argv)
makemodal = (len(sys.argv) > 1)
# makemodal = True

def dialog():
    win = Toplevel()
    Label(win, text='Hard drive reformatted!').pack()
    Button(win, text='OK', command=win.destroy).pack()
    if makemodal:
        win.focus_set()  # принять фокус ввода,
        win.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
        win.wait_window()  # ждать, пока win не будет уничтожен
    print('dialog exit')

root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()
