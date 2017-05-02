# destroy, iconbitmap, protocol, title
from tkinter import *

root = Tk()

trees = [('The Larch!', 'light blue'),
         ('The Pine!', 'light green'),
         ('The Giant Redwood!', 'red')]

for (tree, color) in trees:
    win = Toplevel()
    win.title('Sing...')
    win.protocol('WM_DELETE_WINDOW', lambda: None)
    # win.iconbitmap('py-blue-trans-out.ico')

    msg = Button(win, text=tree, command=win.destroy)
    # msg = Button(win, text=tree, command=(lambda: root.lower(win)))
    msg.pack(expand=YES, fill=BOTH)
    msg.config(padx=10, pady=10, bd=10, relief=RAISED)
    msg.config(bg='black', fg=color, font=('times', 30, 'bold italic'))

root.title('Lumberjack demo')
root.minsize(300, 200)
root.geometry(newGeometry='300x300+200+200')

Label(root, text='Main window', width=30).pack()
Button(root, text='Quit All', command=root.iconify).pack()
root.mainloop()
