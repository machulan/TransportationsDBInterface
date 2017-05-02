# Toplevel

import sys
from tkinter import Toplevel, Button, Label

win1 = Toplevel()
win1.wm_title('Toplevel1')
win2 = Toplevel()
win2.wm_title('Toplevel2')
win2.title('HAUSDHOUSN')
Button(win1, text='Spam', command=sys.exit).pack()
b = Button(win2, text='SPAM', command=sys.exit)
b.pack()


Label(text='Popups').pack() # on default to Tk()
win1.mainloop()