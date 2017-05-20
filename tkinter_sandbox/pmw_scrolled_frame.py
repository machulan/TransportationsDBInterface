import tkinter
#from tkinter import *
import tkinter.tix as tix
import tkinter.ttk as ttk
import Pmw

from resourses.constants import *

class TaskTable(tkinter.Frame):
    def __init__(self, parent=None, headings=tuple(), result=tuple()):
        tkinter.Frame.__init__(self, parent)
        table = ttk.Treeview(self, show="headings", selectmode=tkinter.BROWSE, height=20) # 'headings'

        table["columns"] = headings
        table["displaycolumns"] = headings
        #table.config(padding=30)
        for head in headings:
            table.heading(head, text=head, anchor=tkinter.CENTER)
        for head in headings:
            table.column(head, stretch=True, anchor=tkinter.CENTER, width=70)
        for i, row in enumerate(result):
            #table.insert('', 0, values=row)
            if i % 2 == 0:
                table.insert('', tkinter.END, str(i), values=row)
            else:
                table.insert('', tkinter.END, str(i), values=row, tags=['row'])

        table.tag_configure('row', background='#CCC')
        # print(table.item('1', 'values'))
        # print(table.item('1', 'relief'))

        scrollbar = tkinter.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)

        table.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)
        scrollbar.pack(side=tkinter.RIGHT, expand=tkinter.NO, fill=tkinter.Y)

root = tkinter.Tk()
Pmw.initialise(root, size=12, fontScheme='pmw2')
root.title('PMW Scrolled Frame')

sframe = Pmw.ScrolledFrame(root, usehullsize=1,
                       hull_width=400,
                       hull_height=220
                       )

sframe.pack(expand=tkinter.YES, fill=tkinter.BOTH)

#btn = tkinter.Button(sframe.interior(), text='BUBUBT', command=(lambda : print('DO IT DO IT')))
#btn.pack()

headings = ('first', 'second', 'third')

rows = []
for i in range(100):
    rows.append((i, i, i))

rows = tuple(rows)

# from tkinter_sandbox.grid_by_treeview import TaskTable
#import tkinter_sandbox.grid_by_treeview as grid
#sframe.interior()

tt = TaskTable(sframe.interior(), headings, rows)
tt.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)




#buttonBox = Pmw.ButtonBox(sframe.interior())
#buttonBox.pack(side='bottom')
#buttonBox.add('add', text='Add a button', command=(lambda : print('DO IT DO IT')))

root.mainloop()



exit()

title = 'Pmw.ScrolledFrame demonstration'

# Import Pmw from this directory tree.
import sys
sys.path[:0] = ['../../..']

import tkinter
import Pmw

class Demo:
    def __init__(self, parent):
        # Create the ScrolledFrame.
        self.sf = Pmw.ScrolledFrame(parent,
                labelpos = 'n', label_text = 'ScrolledFrame',
                usehullsize = 1,
                hull_width = 400,
                hull_height = 220,
        )

        # Create a group widget to contain the flex options.
        w = Pmw.Group(parent, tag_text='Flex')
        w.pack(side = 'bottom', padx = 5, pady = 3)

        hflex = Pmw.OptionMenu(w.interior(),
                labelpos = 'w',
                label_text = 'Horizontal:',
                items = ['fixed', 'expand', 'shrink', 'elastic'],
                command = self.sethflex,
                menubutton_width = 8,
        )
        hflex.pack(side = 'left', padx = 5, pady = 3)
        hflex.invoke('fixed')

        vflex = Pmw.OptionMenu(w.interior(),
                labelpos = 'w',
                label_text = 'Vertical:',
                items = ['fixed', 'expand', 'shrink', 'elastic'],
                command = self.setvflex,
                menubutton_width = 8,
        )
        vflex.pack(side = 'left', padx = 5, pady = 3)
        vflex.invoke('fixed')

        # Create a group widget to contain the scrollmode options.
        w = Pmw.Group(parent, tag_text='Scroll mode')
        w.pack(side = 'bottom', padx = 5, pady = 0)

        hmode = Pmw.OptionMenu(w.interior(),
                labelpos = 'w',
                label_text = 'Horizontal:',
                items = ['none', 'static', 'dynamic'],
                command = self.sethscrollmode,
                menubutton_width = 8,
        )
        hmode.pack(side = 'left', padx = 5, pady = 3)
        hmode.invoke('dynamic')

        vmode = Pmw.OptionMenu(w.interior(),
                labelpos = 'w',
                label_text = 'Vertical:',
                items = ['none', 'static', 'dynamic'],
                command = self.setvscrollmode,
                menubutton_width = 8,
        )
        vmode.pack(side = 'left', padx = 5, pady = 3)
        vmode.invoke('dynamic')

        self.radio = Pmw.RadioSelect(parent, selectmode = 'multiple',
            command = self.radioSelected)
        self.radio.add('center', text = 'Keep centered vertically')
        self.radio.pack(side = 'bottom')

        buttonBox = Pmw.ButtonBox(parent)
        buttonBox.pack(side = 'bottom')
        buttonBox.add('add', text = 'Add a button', command = self.addButton)
        buttonBox.add('yview', text = 'Show yview', command = self.showYView)
        buttonBox.add('scroll', text = 'Page down', command = self.pageDown)

        # Pack this last so that the buttons do not get shrunk when
        # the window is resized.
        self.sf.pack(padx = 5, pady = 3, fill = 'both', expand = 1)

        self.frame = self.sf.interior()

        self.row = 0
        self.col = 0

        for count in range(15):
            self.addButton()

    def sethscrollmode(self, tag):
        self.sf.configure(hscrollmode = tag)

    def setvscrollmode(self, tag):
        self.sf.configure(vscrollmode = tag)

    def sethflex(self, tag):
        self.sf.configure(horizflex = tag)

    def setvflex(self, tag):
        self.sf.configure(vertflex = tag)

    def addButton(self):
        button = tkinter.Button(self.frame,
            text = '(%d,%d)' % (self.col, self.row))
        button.grid(row = self.row, column = self.col, sticky = 'nsew')

        self.frame.grid_rowconfigure(self.row, weight = 1)
        self.frame.grid_columnconfigure(self.col, weight = 1)
        if self.sf.cget('horizflex') == 'expand' or \
                self.sf.cget('vertflex') == 'expand':
            self.sf.reposition()

        if 'center' in self.radio.getcurselection():
            self.sf.update_idletasks()
            self.centerPage()

        if self.col == self.row:
            self.col = 0
            self.row = self.row + 1
        else:
            self.col = self.col + 1

    def showYView(self):
        print((self.sf.yview()))

    def pageDown(self):
        self.sf.yview('scroll', 1, 'page')

    def radioSelected(self, name, state):
        if state:
            self.centerPage()

    def centerPage(self):
        # Example of how to use the yview() method of Pmw.ScrolledFrame.
        top, bottom = self.sf.yview()
        size = bottom - top
        middle = 0.5 - size / 2
        self.sf.yview('moveto', middle)

######################################################################

# Create demo in root window for testing.
if __name__ == '__main__':
    import os
    if os.name == 'nt':
        size = 16
    else:
        size = 12
    root = tkinter.Tk()
    Pmw.initialise(root, size = size, fontScheme = 'pmw2')
    root.title(title)

    exitButton = tkinter.Button(root, text = 'Exit', command = root.destroy)
    exitButton.pack(side = 'bottom')
    widget = Demo(root)
    root.mainloop()

