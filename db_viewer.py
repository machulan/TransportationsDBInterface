from tkinter import *
import tkinter.tix as tix
import tkinter.ttk as ttk
import tkinter.font as tkinterfont

from resourses.constants import *
from styles import *

import db_helper
import preferencies
import main_window

table_frame = None
view_frame = None


class ScrolledGridViewer(Frame):
    def __init__(self, master=None, headings=tuple(), rows=tuple()):
        Frame.__init__(self, master)

        table = ttk.Treeview(self)
        table.config(show="headings", selectmode=BROWSE)
        table.config(columns=headings, displaycolumns=headings)

        for heading in headings:
            table.heading(heading, text=heading, anchor=CENTER)
            table.column(heading, stretch=True, anchor=CENTER)

        for i, row in enumerate(rows):
            table.insert('', END, values=row, tags=['first type'] if i % 2 == 0 else ['second type'])

        table.tag_configure('first type', background='#EEE')

        xscrollbar = Scrollbar(self, orient=HORIZONTAL, command=table.xview)
        yscrollbar = Scrollbar(self, orient=VERTICAL, command=table.yview)
        table.config(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)

        yscrollbar.pack(side=RIGHT, expand=NO, fill=Y)
        xscrollbar.pack(side=BOTTOM, expand=NO, fill=X)
        table.pack(side=LEFT, expand=YES, fill=BOTH)




class ScrolledTableList(Frame):
    def __init__(self, parent, tables, **options):
        Frame.__init__(self, parent, **options)
        # self.pack(expand=YES, fill=BOTH)  # сделать растягиваемым
        self.tables = tables
        self.make_widgets()

    def handle_list(self, event):
        index = self.listbox.curselection()[0]  # при двойном щелчке на списке
        # report_name = self.listbox.get(index)

        table = self.tables[index]
        print('Item [', table[0], '] was chosen')
        table[1]()
        # report_name = self.listbox.get(index)  # извлечь выбранный текст
        # self.run_command()  # и вызвать действие
        # или get(ACTIVE)

    def make_widgets(self):
        self.scrollbar = Scrollbar(self)
        self.listbox = Listbox(self, relief=SUNKEN)
        self.scrollbar.config(command=self.listbox.yview)  # связать sbar и list
        self.listbox.config(yscrollcommand=self.scrollbar.set)  # сдвиг одного = сдвиг другого
        self.scrollbar.pack(side=RIGHT, fill=Y)  # первым добавлен – посл. обрезан
        self.listbox.pack(side=LEFT, expand=YES, fill=BOTH)  # список обрезается первым

        for pos, (table_name, table_function) in enumerate(self.tables):
            self.listbox.insert(pos, table_name)

        self.listbox.config(selectmode=SINGLE)
        self.listbox.bind('<Double-1>', self.handle_list)
        self.listbox.bind('<Return>', self.handle_list)


def get_test_table(column_count, row_count):
    headings = []
    for i in range(column_count):
        headings.append('column ' + str(i))

    alphabet = ''
    for i in range(26):
        alphabet += chr(ord('a') + i)

    rows = []
    for i in range(row_count):
        rows.append(tuple([i] * column_count))
    return tuple(headings), tuple(rows)


def open_table(table_id):
    print('Table [ ' + TABLE_NAMES_INTERFACE[table_id] + ' ] is opening...')

    global table_frame
    table_frame.config(bd=5)

    temp_headings, temp_rows = get_test_table(7, 100)

    grid_viewer = ScrolledGridViewer(table_frame, temp_headings, temp_rows)
    grid_viewer.pack(expand=YES, fill=BOTH)

    # treeview.insert('', 0, 'tables', text='Tables', tags=['tables tag'])
    # treeview.insert('tables', 0, 'table 1', text='first table', tags=['table tag', 'table 1 tag'])
    # treeview.insert('tables', 1, 'table 2', text='second table')
    #
    # treeview.insert('', 1, 'views', text='Views', tags=['views tag'])
    # treeview.insert('views', 0, 'view 1', text='first view', tags=['views tag'])
    # treeview.insert('views', 1, 'view 2', text='second view', tags=['views tag'])
    #
    # treeview.config(selectmode=BROWSE, show=['tree'])
    # treeview.tag_configure('tables tag', background='green')


def open_view(view_id):
    print('View [ ' + VIEW_NAMES_INTERFACE[view_id] + ' ] is opening...')
    pass


def run(root, account):
    main_window.clear_main_frame(root, account)

    root.title(TABLE_LIST_WINDOW_TITLE + ' [' + account.get_rights() + ']')
    main_window.status_label['text'] = 'Просмотр таблиц и представлений'

    print('DB_VIEWER [main_window.status_label] ::', main_window.status_label)

    # nf = tkinterfont.Font(family='consolas', size=30)
    # style = ttk.Style()
    # st.configure('.', font=f)
    # style.configure('Notebook', font=VIEW_NAME_FONT)

    notebook = ttk.Notebook(main_window.main_frame)
    notebook.pack(expand=YES, fill=BOTH)
    # notebook.config(style='Notebook')
    # notebook.add(frame)
    # notebook.tab(0, text=TABLE_LIST_WINDOW_TITLE)
    # notebook.tab(1, text=VIEW_LIST_WINDOW_TITLE)

    ###########################################################
    # TABLES
    ###########################################################

    #    paned_window = PanedWindow(main_window.main_frame)
    paned_window = PanedWindow(notebook)
    paned_window.pack(fill=BOTH, expand=YES, side=LEFT)

    notebook.add(paned_window)
    notebook.tab(0, text=TABLE_LIST_WINDOW_TITLE)

    paned_window.config(orient=HORIZONTAL)
    paned_window.config(sashrelief=GROOVE, sashwidth=10)  # relief ::

    """table_functions = [
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing()
    ]"""

    table_functions = []
    for table_id in range(len(TABLE_NAMES_DATABASE)):
        table_functions.append(lambda table_id=table_id: open_table(table_id))

    tables = [(table_name, table_function) for table_name, table_function in
              zip(TABLE_NAMES_INTERFACE, table_functions)]

    scrolled_table_list = ScrolledTableList(paned_window, tables)
    # scrolled_report_list.pack(side=LEFT, expand=NO, fill=Y)
    paned_window.add(scrolled_table_list)
    scrolled_table_list.listbox.config(width=12)
    scrolled_table_list.listbox.config(font=TABLE_NAME_FONT)
    scrolled_table_list.listbox.config(selectmode=BROWSE, activestyle=DOTBOX)  # setgrid=10) '#5F5' - light green
    scrolled_table_list.listbox.config(selectbackground='#5F5', selectforeground='black')
    scrolled_table_list.listbox.config(selectborderwidth=5, relief=FLAT, exportselection=0, cursor='hand2')
    # scrolled_table_list.listbox.curselection()
    # scrolled_table_list.listbox.select_anchor(2)
    scrolled_table_list.listbox.select_set(0)
    scrolled_table_list.listbox.focus_set()

    scrolled_table_list.listbox.config(bg='#EEE')
    scrolled_table_list_item_colors = ['#DDD', '#AAA']  # ['#CCF', '#EEF']
    for pos in range(len(scrolled_table_list.tables)):
        scrolled_table_list.listbox.itemconfig(pos, background=scrolled_table_list_item_colors[pos % 2])

    global table_frame
    table_frame = Frame(paned_window)
    paned_window.add(table_frame)
    # report_frame.config()

    table_frame.config(bd=10, relief=SOLID)

    ###########################################################
    # VIEWS
    ###########################################################

    view_paned_window = PanedWindow(notebook)
    view_paned_window.pack(fill=BOTH, expand=YES, side=LEFT)

    notebook.add(view_paned_window)
    notebook.tab(1, text=VIEW_LIST_WINDOW_TITLE)
    # notebook.config(font=VIEW_LIST_WINDOW_TITLE)
    notebook.select(1)

    view_paned_window.config(orient=HORIZONTAL)
    view_paned_window.config(sashrelief=GROOVE, sashwidth=10)  # relief ::

    view_functions = [
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing(),
        lambda: do_nothing()
    ]

    views = [(view_name, view_function) for view_name, view_function in
             zip(VIEW_NAMES_INTERFACE, view_functions)]

    scrolled_view_list = ScrolledTableList(view_paned_window, views)
    # scrolled_report_list.pack(side=LEFT, expand=NO, fill=Y)
    view_paned_window.add(scrolled_view_list)

    scrolled_view_list.listbox.config(width=15)
    scrolled_view_list.listbox.config(font=VIEW_NAME_FONT)
    scrolled_view_list.listbox.config(selectmode=BROWSE, activestyle=DOTBOX)  # setgrid=10) '#5F5' - light green
    scrolled_view_list.listbox.config(selectbackground='#5F5', selectforeground='black')
    scrolled_view_list.listbox.config(selectborderwidth=5, relief=FLAT, exportselection=0, cursor='hand2')
    # scrolled_view_list.listbox.curselection()
    # scrolled_view_list.listbox.select_anchor(2)
    scrolled_view_list.listbox.select_set(0)
    scrolled_view_list.listbox.focus_set()

    scrolled_view_list.listbox.config(bg='#EEE')
    scrolled_view_list_item_colors = ['#DDD', '#AAA']  # ['#CCF', '#EEF']
    for pos in range(len(scrolled_view_list.tables)):
        scrolled_view_list.listbox.itemconfig(pos, background=scrolled_view_list_item_colors[pos % 2])

    global view_frame
    view_frame = Frame(view_paned_window)
    view_paned_window.add(view_frame)
    # report_frame.config()

    view_frame.config(bd=10, relief=SOLID)

    show_treeview = False
    if show_treeview:
        treeview_font = ('consolas', 20, '')

        treeview = ttk.Treeview(main_window.main_frame)
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

        # treeview.column(0, stretch=True)

        b = Button(main_window.main_frame)
        b.config(command=lambda: print(treeview.selection()))
        b.pack(side=RIGHT)

        # treeview.selection_set(['tables'])
        # treeview.selection()


        # tree = tix.Tree(main_window.main_frame)
        # tree.pack(side=LEFT, fill=Y)
        # tree.config(hlist.indent=30, drawbranch=TRUE, wideselection=FALSE)
        # ree.
        # tree.config(font=('consolas', 20, ''))

    show_hlist = False
    if show_hlist:
        hlist = tix.HList(main_window.main_frame)
        # hlist = tree.subwidget('hlist')
        hlist.pack(side=LEFT, fill=Y)
        hlist.config(indent=30, drawbranch=TRUE,
                     wideselection=FALSE)  # , separator='/') #itemtype='imagetext')#, separator='=')
        hlist.config(font=('consolas', 20, ''))
        hlist.config(selectbackground='green')

        # tree.autosetmode()

        # hlist.config(bd)

        # hlist.add('f', text='f')
        # hlist.add('s', text='s')

        # hlist.add('f.f', text='f.f')
        # hlist.add('f.s', text='f.s')

        # hlist.add('s.f', text='s.f')
        # hlist.add('s.s', text='s.s')

        # hlist.add('s.f.s', text='s.f.s')
        # hlist.item_configure('s.f.s', 0, bd=10)

        ts = 'tables'
        vs = 'views'

        hlist.add(ts, text='Таблицы')
        hlist.add(vs, text='Представления')

        for i in range(len(TABLE_NAMES_DATABASE)):
            hlist.add(ts + '.' + TABLE_NAMES_DATABASE[i], text=TABLE_NAMES_INTERFACE[i])
        for i in range(len(VIEW_NAMES_DATABASE)):
            hlist.add(vs + '.' + VIEW_NAMES_DATABASE[i], text=VIEW_NAMES_INTERFACE[i])

    return

    # TODO BELOW TEMP

    data = db_helper.year_profit_statistics()
    print('year_profit_statistics :', data)

    column_names = ['Год', 'Прибыль', 'Абсолютный рост', 'Относительный рост']

    # rowspan=2 colunmspan=3

    for j in range(len(column_names)):
        label = Label(main_window.main_frame)
        label.grid(row=0, column=j, sticky=NSEW)
        label.config(text=column_names[j])
        label.config(relief=GROOVE)  # SUNKEN FLAT RIDGE RAISED GROOVE SOLID
        main_window.main_frame.columnconfigure(j, weight=(j % 2) + 1)
    for i in range(len(data)):
        for j in range(len(column_names)):
            entry = Entry(main_window.main_frame)
            entry.grid(row=i + 1, column=j, sticky=NSEW)
            entry.insert(END, data[i][j])
            main_window.main_frame.columnconfigure(j, weight=(j % 2) + 1)
        main_window.main_frame.rowconfigure(i, weight=1)

        # __import__('os').system('cmd')


        # window = Toplevel(root)
        # window.title(VIEW_TITLE + ' [' + account.get_rights() + ']')
        # window.state('zoomed')
        # # window.resizable(width=True)
        #
        #
        # window.focus_set()
