from tkinter import *
# widget = Label(None, text='Hello GUI world!')
widget = Label()
widget['text'] = 'Hello!'
widget.pack(expand=YES, fill=BOTH)
widget.mainloop()