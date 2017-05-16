# http://effbot.org/tkinterbook/panedwindow.htm

from tkinter import *

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)
m.config(sashrelief=GROOVE, sashwidth=10)

top = Label(m, text="top pane")
m.add(top)

bottom = Label(m, text="bottom pane")
m.add(bottom)

mainloop()