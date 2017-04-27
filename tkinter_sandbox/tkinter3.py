import tkinter
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='Reply', message='Hello, {}!'.format(name))


top = tkinter.Tk()
top.title("Ec ho")
# top.iconbitmap('py-blue-trans-out.ico')

tkinter.Label(top, text='Enter your name:').pack(side=tkinter.TOP)
ent = tkinter.Entry(top)
ent.pack(side=tkinter.TOP)
btn = tkinter.Button(top, text="Submit", command=(lambda: reply(ent.get())))
btn.pack(side=tkinter.LEFT)

top.mainloop()
