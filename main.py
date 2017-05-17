from tkinter import *
import login
from resourses.constants import *
from preferencies import *
from tkinter.messagebox import *

import shelve

root = Tk()

root.state('zoomed')
root.title(ROOT_TITLE)
root.minsize(width=1000, height=500)

# root.protocol('WM_ICONIFY_WINDOW', lambda: None)

# root.maxsize(width=1000, height=1000)
# root.config(bg='#000')

root.resizable(width=True, height=True)

set_preferencies()
login.run(root)

#b = Button(root, text='BBUBUBT')
#b.pack()
# print(root.cget('b'))
# root.attributes('-alpha', 0.5)
# root.attributes('-transparentcolor', '#FFF')
# root.attributes('-fullscreen', 1)
# root.attributes('-toolwindow',1)
# print(root.attributes())

root.mainloop()


# def notdone():
#    showerror('Not implemented', 'Not yet available')

# root_menu = Menu(root)
# root.config(menu=root_menu)
#
# file_menu = Menu(root_menu)
# file_menu.add_command(label='New...', command=notdone, underline=0)
# file_menu.add_command(label='Open...', command=notdone, underline=0)
# file_menu.add_separator()
# file_menu.add_command(label='Quit', command=root.quit, underline=0)
# root_menu.add_cascade(label='File', menu=file_menu, underline=0)
#
# edit_menu = Menu(root_menu, tearoff=False)
# edit_menu.add_command(label='Cut', command=notdone, underline=0)
# edit_menu.add_command(label='Paste', command=notdone, underline=0)
# edit_menu.add_separator()
# root_menu.add_cascade(label='Edit', menu=edit_menu, underline=0)
#
# sub_menu = Menu(edit_menu, tearoff=True)
# sub_menu.add_command(label='Spam', command=root.quit, underline=0)
# sub_menu.add_command(label='Eggs', command=notdone, underline=0)
# edit_menu.add_cascade(label='Stuff', menu=sub_menu, underline=0)




