import tkinter

from tkinter_sandbox.tkinter1 import MyGui

# главное окно приложения
main_window = tkinter.Tk()
tkinter.Label(main_window, text=__name__).pack()

# окно диалога
popup = tkinter.Toplevel()
tkinter.Label(popup, text='Attach').pack(side=tkinter.LEFT)
MyGui(popup).pack(side=tkinter.RIGHT)  # присоединить виджеты
main_window.mainloop()
