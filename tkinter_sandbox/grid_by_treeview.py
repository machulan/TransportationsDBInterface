from tkinter import *
import tkinter.tix as tix
import tkinter.ttk as ttk
from resourses.constants import *

class TaskTable(Frame):
    def __init__(self, parent=None, headings=tuple(), result=tuple()):
        Frame.__init__(self, parent)
        table = ttk.Treeview(self, show="headings", selectmode=BROWSE, height=12) # 'headings'

        table["columns"] = headings
        table["displaycolumns"] = headings
        #table.config(padding=30)
        for head in headings:
            table.heading(head, text=head, anchor=CENTER)
        for head in headings:
            table.column(head, stretch=True, anchor=CENTER, width=70)
        for i, row in enumerate(result):
            #table.insert('', 0, values=row)
            if i % 2 == 0:
                table.insert('', END, str(i), values=row)
            else:
                table.insert('', END, str(i), values=row, tags=['row'])

        table.tag_configure('row', background='#CCC')
        # print(table.item('1', 'values'))
        # print(table.item('1', 'relief'))

        scrollbar = Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)

        table.pack(side=LEFT, expand=YES, fill=BOTH)
        scrollbar.pack(side=RIGHT, expand=NO, fill=Y)

root = tix.Tk()

headings = ['first', 'second', 'third']

rows = []
for i in range(100):
    rows.append((i, i, i))

#print(rows)
rows = tuple(rows)
#print(rows)

tt = TaskTable(root, headings, rows)
tt.pack(side=LEFT, expand=YES, fill=BOTH)

#headings[0] = 'HUHUH'
root.mainloop()

exit()

treeview_font = ('consolas', 20, '')

treeview = ttk.Treeview(root)
treeview.pack(side=LEFT, fill=Y)
treeview.config(padding=50)
# treeview.config(font=('consolas', 20, ''))
# treeview.config(background='green')

treeview.insert('', 0, 'tables', text='Tables', tags=['tables tag'])
treeview.insert('tables', 0, 'table 1', text='first table', tags=['table tag', 'table 1 tag'])
treeview.insert('tables', 1, 'table 2', text='second table')

treeview.insert('', 1, 'views', text='Views', tags=['views tag'])
treeview.insert('views', 0, 'view 1', text='first view', tags=['views tag'])
treeview.insert('views', 1, 'view 2', text='second view', tags=['views tag'])

treeview.config(selectmode=BROWSE, show=['tree'])
treeview.tag_configure('tables tag', background='green')
treeview.tag_configure('table 1 tag', font=treeview_font)
treeview.tag_configure('views tag', font=treeview_font)