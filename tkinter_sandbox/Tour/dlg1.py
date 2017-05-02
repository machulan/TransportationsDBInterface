# showinfo, showerror, showwarning, askyesno

from tkinter import *
from tkinter.messagebox import *


def callback():
    if askyesno('Verify', 'Do you really wnat to quit?'):
        showwarning('Yes', 'Quit not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')
        # showerror('UNKNOWN ERROR', errmsg)


errmsg = 'Sorry, no Spam allowed!'

Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()
