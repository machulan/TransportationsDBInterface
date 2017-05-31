from tkinter import *
import tkinter.tix as tix
import tkinter.ttk as ttk
import tkinter.font as tkinterfont

from tkinter.messagebox import showinfo, showerror, showwarning, askokcancel

from resourses.constants import *
from styles import *

import db_helper
import preferencies
import main_window
import dialogs

table_frame = None
view_frame = None

table_grid_viewer = None
view_grid_viewer = None

table_toolbar = None
view_toolbar = None

table_progressbar = None
view_progressbar = None

displayed_table_name = None
displayed_view_name = None
displayed_notebook_tab = None


def clear_frame(frame):
    frame_copy = frame.children.copy()
    for key, widget in frame_copy.items():
        widget.destroy()


def clear_table_frame():
    table_frame_copy = table_frame.children.copy()
    for key, widget in table_frame_copy.items():
        widget.destroy()


def clear_view_frame():
    view_frame_copy = view_frame.children.copy()
    for key, widget in view_frame_copy.items():
        widget.destroy()


# constraint = get_table_constraint(table_id, account)
def get_table_constraint(table_id, account):
    admin_column_names = DATABASE_TABLE_COLUMN_NAMES[table_id]
    if account.is_admin():
        return tuple([True] * len(admin_column_names))

    # user
    result = []
    user_column_names = USER_DATABASE_TABLE_COLUMN_NAMES[table_id]
    user_column_id, admin_column_id = 0, 0
    while user_column_id < len(user_column_names) and admin_column_id < len(admin_column_names):
        while user_column_names[user_column_id] != admin_column_names[admin_column_id]:
            admin_column_id += 1
            result.append(False)
        result.append(True)
        user_column_id += 1
        admin_column_id += 1

    while admin_column_id < len(admin_column_names):
        admin_column_id += 1
        result.append(False)

    print(table_id, result)
    return tuple(result)


class ScrolledGridViewer(Frame):
    def __init__(self, master=None, headings=tuple(), rows=tuple(), constraint=None):
        Frame.__init__(self, master)

        if constraint is None or len(constraint) < len(headings):
            constraint = tuple([True] * len(headings))

        table = ttk.Treeview(self)
        table.config(show="headings", selectmode=BROWSE)
        # table.config(columns=headings, displaycolumns=headings)
        table.config(columns=headings)
        displaycolumns_list = []
        for i, item in enumerate(constraint):
            if item:
                displaycolumns_list.append(i)
        # displaycolumns_list = [1,3]
        table.config(displaycolumns=displaycolumns_list)

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

        self.table = table
        self.table.bind("<<TreeviewSelect>>", lambda event: self.print_status())

        self.table_size = (len(headings), len(rows))

        self.constraint = constraint

        self.selected_item = None
        main_window.clear_selected_item_label()

    def print_status(self):
        print('Constraint :', self.constraint)
        iid = self.table.focus()
        print('Selected item with id :', iid)
        selected_item_label_text = 'Запись ' + str(int('0x' + iid[1:], 16)) + ':' + str(self.table_size[1]) + ''
        main_window.selected_item_label.config(text=selected_item_label_text)

        # print('SIZE :', self.table.size())
        # print('ELEMENT :', self.table.identify_element(1, 1))
        # print('REGION :', self.table.identify_region(1, 1))
        # print('COLUMN :', self.table.identify_column(3))
        # print('ELEMENTS')
        # for i in range(10):
        #    print('ELEMENT :', self.table.identify_element(i, 3))

        item = self.table.item(iid)
        print(item)
        self.selected_item = item

        # def selected_item(self):
        # iid = self.table.focus()
        # item = self.table.item(iid)
        # print('Selected item id:', item)
        # return item


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


def show_child_records(table_id, root, account):
    print('Просмотр дочерних записей для таблицы ' + INTERFACE_TABLE_NAMES[table_id].upper())
    selected_item = table_grid_viewer.selected_item
    if selected_item is None:
        print('Для изменения ничего не выбрано')
        showinfo('Справка', 'Выберите запись в таблице')
        # showerror('Информация', 'Для изменения ничего не выбрано')
        # showwarning('Информация', 'Для изменения ничего не выбрано')
        return

    selected_record = selected_item['values']
    print(selected_record)


def insert_into_table(table_id, root, account):
    print('Вставка данных в таблицу')
    inserted_data = dialogs.ask_table_inserted_data(table_id, root, account)
    if inserted_data is None:
        print('Cancel button pressed')
        return
    print(inserted_data)
    db_helper.insert_into_table(DATABASE_TABLE_NAMES[table_id], inserted_data)

    showinfo('Справка', 'Данные успешно добавлены в таблицу!')


def insert_into_view(view_id, root, account):
    print('Ввод данных через представление')
    inserted_data = dialogs.ask_view_inserted_data(view_id, root, account)
    if inserted_data is None:
        print('Cancel button pressed')
        return
    print(inserted_data)
    db_helper.insert_into_view(DATABASE_VIEW_NAMES[view_id], inserted_data)

    showinfo('Справка', 'Данные успешно добавлены через представление!')


def delete_data_from(table_id, root, account):
    print('Удаление данных из таблицы ' + INTERFACE_TABLE_NAMES[table_id].upper())
    selected_item = table_grid_viewer.selected_item
    if selected_item is None:
        print('Для изменения ничего не выбрано')
        showinfo('Справка', 'Выберите запись в таблице')
        # showerror('Информация', 'Для изменения ничего не выбрано')
        # showwarning('Информация', 'Для изменения ничего не выбрано')
        return

    deleted_data = selected_item['values']

    deletion_confirmed = askokcancel('Внимание', 'Вы действительно хотите удалить выбранную запись?')
    if not deletion_confirmed:
        print('Операция удаления отменена')
        return
    # new_data = dialogs.ask_table_inserted_data(table_id, root, account)
    # primary_keys = TABLES_PRIMARY_KEYS[table_id]

    db_helper.delete(DATABASE_TABLE_NAMES[table_id], deleted_data)

    print(deleted_data, ' => ', 'Небытие')

    # open_table(table_id, root, account)

    showinfo('Справка', 'Запись успешно удалена!')


def update_data_of(table_id, root, account):
    print('Изменение данных в таблице ' + INTERFACE_TABLE_NAMES[table_id].upper())
    selected_item = table_grid_viewer.selected_item
    if selected_item is None:
        print('Для изменения ничего не выбрано')
        showinfo('Справка', 'Выберите запись в таблице')
        # showerror('Информация', 'Для изменения ничего не выбрано')
        # showwarning('Информация', 'Для изменения ничего не выбрано')
        return

    old_data = selected_item['values']
    new_data = dialogs.ask_table_inserted_data(table_id, root, account)
    # primary_keys = TABLES_PRIMARY_KEYS[table_id]
    if new_data is None:
        print('Cancel button pressed')
        return

    new_data = list(new_data)
    for i, old_item in enumerate(old_data):
        if new_data[i] is None:
            new_data[i] = old_item
    new_data = tuple(new_data)

    db_helper.update(DATABASE_TABLE_NAMES[table_id], old_data, new_data)

    print(old_data, ' => ', new_data)

    showinfo('Справка', 'Данные успешно изменены!')


def make_table_toolbar(table_id, root, account):
    clear_table_toolbar()

    # table_name = DATABASE_TABLE_NAMES[table_id]
    print('Grid viewer toolbar is filling...')

    global table_toolbar

    show_child_records_button = main_window.ToolbarButton(table_toolbar, text='Дочерние записи...')
    show_child_records_button.pack(side=LEFT, fill=Y)
    show_child_records_button.config(command=(lambda: show_child_records(table_id, root, account)))

    if account.is_admin():
        insert_button = main_window.ToolbarButton(table_toolbar, text='Вставить...')
        insert_button.pack(side=RIGHT, fill=Y)
        insert_button.config(command=(lambda: insert_into_table(table_id, root, account)))

        delete_button = main_window.ToolbarButton(table_toolbar, text='Удалить...')
        delete_button.pack(side=RIGHT, fill=Y)
        delete_button.config(command=(lambda: delete_data_from(table_id, root, account)))

    update_button = main_window.ToolbarButton(table_toolbar, text='Изменить...')
    update_button.pack(side=RIGHT, fill=Y)
    update_button.config(command=(lambda: update_data_of(table_id, root, account)))


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


after_id = None


def cancel_table_progressbar_after():
    global after_id
    table_progressbar.after_cancel(after_id)
    print('cancel after')
    table_progressbar.stop()


def open_table(table_id, root, account):
    table_progressbar.start(10)
    global after_id
    after_id = table_progressbar.after(1130, cancel_table_progressbar_after)

    table_name = INTERFACE_TABLE_NAMES[table_id].upper()
    print('Table [ ' + INTERFACE_TABLE_NAMES[table_id] + ' ] is opening...')

    root.title('Таблица ' + table_name + ' [' + account.get_rights() + ']')
    main_window.status_label['text'] = 'Таблица : ' + table_name
    global displayed_table_name
    displayed_table_name = main_window.status_label['text']

    global table_frame
    clear_table_frame()
    # table_frame.config(bd=5)

    make_table_toolbar(table_id, root, account)

    # temp_headings, temp_rows = get_test_table(7, 100)

    column_names = INTERFACE_TABLE_COLUMN_NAMES[table_id]
    table_data = db_helper.select_all_from(DATABASE_TABLE_NAMES[table_id])

    # print(table_data)
    # column_names = tuple(['column ' + str(i) for i in range(len(table_data[0]))])
    constraint = get_table_constraint(table_id, account)

    global table_grid_viewer
    table_grid_viewer = ScrolledGridViewer(table_frame, column_names, table_data, constraint)
    table_grid_viewer.pack(expand=YES, fill=BOTH)

    # table_progressbar.stop()
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


def make_view_toolbar(view_id, root, account):
    clear_view_toolbar()

    view_name = DATABASE_VIEW_NAMES[view_id]
    print('Grid viewer toolbar is filling...')

    global view_toolbar

    insert_button = main_window.ToolbarButton(view_toolbar, text='Вставить...')
    insert_button.pack(side=RIGHT, fill=Y)
    insert_button.config(command=(lambda: insert_into_view(view_id, root, account)))

    if account.is_admin():
        delete_button = main_window.ToolbarButton(view_toolbar, text='Удалить...')
        # delete_button.pack(side=RIGHT, fill=Y)
        delete_button.config(command=(lambda: delete_data_from(view_name, root, account)))

        update_button = main_window.ToolbarButton(view_toolbar, text='Обновить...')
        # update_button.pack(side=RIGHT, fill=Y)
        update_button.config(command=(lambda: update_data_of(view_name, root, account)))


def cancel_view_progressbar_after():
    global after_id
    view_progressbar.after_cancel(after_id)
    print('cancel after')
    view_progressbar.stop()


def open_view(view_id, root, account):
    view_progressbar.start(10)
    global after_id
    after_id = view_progressbar.after(1100, cancel_view_progressbar_after)
    # view_progressbar.update()

    view_name = INTERFACE_VIEW_NAMES[view_id].upper()
    print('View [ ' + INTERFACE_VIEW_NAMES[view_id] + ' ] is opening...')

    root.title('Представление ' + view_name + ' [' + account.get_rights() + ']')
    main_window.status_label['text'] = 'Представление : ' + view_name
    global displayed_view_name
    displayed_view_name = main_window.status_label['text']

    global view_frame
    clear_view_frame()
    # view_frame.config(bd=5)

    make_view_toolbar(view_id, root, account)

    # temp_headings, temp_rows = get_test_table(7, 100)

    column_names = INTERFACE_VIEW_COLUMN_NAMES[view_id]
    view_data = db_helper.select_all_from(DATABASE_VIEW_NAMES[view_id])

    # print(table_data)
    # column_names = tuple(['column ' + str(i) for i in range(len(table_data[0]))])
    global view_grid_viewer
    view_grid_viewer = ScrolledGridViewer(view_frame, column_names, view_data)
    view_grid_viewer.pack(expand=YES, fill=BOTH)

    # view_progressbar.stop()


def clear_table_toolbar():
    global table_toolbar
    if not (table_toolbar is None):
        table_toolbar_copy = table_toolbar.children.copy()
        for key, widget in table_toolbar_copy.items():
            widget.destroy()
            # grid_viewer_toolbar


def clear_view_toolbar():
    global view_toolbar
    if not (view_toolbar is None):
        view_toolbar_copy = view_toolbar.children.copy()
        for key, widget in view_toolbar_copy.items():
            widget.destroy()
            # grid_viewer_toolbar


# def make_grid_viewer_toolbar():
#     global grid_viewer_toolbar
#     grid_viewer_toolbar = Frame(main_window.main_frame)
#     grid_viewer_toolbar.pack(side=TOP, fill=X)
#     grid_viewer_toolbar.config(padx=5, pady=3)
#     grid_viewer_toolbar.config(bg='#CCF')  # FFA


def run(entity_type, root, account):
    main_window.clear_main_frame(root, account)

    if entity_type == TABLES:
        root.title(TABLE_LIST_WINDOW_TITLE + ' [' + account.get_rights() + ']')
    else:
        root.title(VIEW_LIST_WINDOW_TITLE + ' [' + account.get_rights() + ']')
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

    table_tab_frame = Frame(notebook)
    table_tab_frame.pack(fill=BOTH, expand=YES, side=LEFT)

    notebook.add(table_tab_frame)
    notebook.tab(0, text=TABLE_LIST_WINDOW_TITLE)

    global table_progressbar
    table_progressbar = ttk.Progressbar(table_tab_frame)
    table_progressbar.pack(side=BOTTOM, expand=NO, fill=X)
    table_progressbar.config(mode='determinate')

    global table_toolbar
    table_toolbar = Frame(table_tab_frame)
    table_toolbar.pack(side=BOTTOM, expand=NO, fill=X)
    table_toolbar.config(padx=5, pady=3)
    table_toolbar.config(bg='#CCF')

    # table_progressbar.start(20)
    # table_progressbar.start(20)

    # progressbar.step(50)

    #    paned_window = PanedWindow(main_window.main_frame)
    paned_window = PanedWindow(table_tab_frame)
    paned_window.pack(fill=BOTH, expand=YES, side=LEFT)

    # notebook.add(paned_window)
    # notebook.tab(0, text=TABLE_LIST_WINDOW_TITLE)

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
    for table_id in range(len(DATABASE_TABLE_NAMES)):
        table_functions.append(lambda table_id=table_id: open_table(table_id, root, account))

    tables = [(table_name, table_function) for table_name, table_function in
              zip(INTERFACE_TABLE_NAMES, table_functions)]

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

    # table_frame.config(bd=1, relief=SOLID)

    ###########################################################
    # VIEWS
    ###########################################################

    view_tab_frame = Frame(notebook)
    view_tab_frame.pack(fill=BOTH, expand=YES, side=LEFT)

    notebook.add(view_tab_frame)
    notebook.tab(1, text=VIEW_LIST_WINDOW_TITLE)

    global view_toolbar
    view_toolbar = Frame(view_tab_frame)
    view_toolbar.pack(side=BOTTOM, expand=NO, fill=X)
    view_toolbar.config(padx=5, pady=3)
    view_toolbar.config(bg='#CCF')
    # view_grid_viewer_toolbar

    global view_progressbar
    view_progressbar = ttk.Progressbar(view_tab_frame)
    view_progressbar.pack(side=BOTTOM, expand=NO, fill=X)
    view_progressbar.config(mode='determinate')

    view_paned_window = PanedWindow(view_tab_frame)
    view_paned_window.pack(fill=BOTH, expand=YES, side=LEFT)

    # notebook.add(view_paned_window)
    # notebook.tab(1, text=VIEW_LIST_WINDOW_TITLE)
    # notebook.config(font=VIEW_LIST_WINDOW_TITLE)


    view_paned_window.config(orient=HORIZONTAL)
    view_paned_window.config(sashrelief=GROOVE, sashwidth=10)  # relief ::

    # view_functions = [
    #     lambda: do_nothing(),
    #     lambda: do_nothing(),
    #     lambda: do_nothing(),
    #     lambda: do_nothing()
    # ]

    view_functions = []
    for view_id in range(len(DATABASE_VIEW_NAMES)):
        view_functions.append(lambda view_id=view_id: open_view(view_id, root, account))

    views = [(view_name, view_function) for view_name, view_function in
             zip(INTERFACE_VIEW_NAMES, view_functions)]

    scrolled_view_list = ScrolledTableList(view_paned_window, views)
    # scrolled_report_list.pack(side=LEFT, expand=NO, fill=Y)
    view_paned_window.add(scrolled_view_list)

    scrolled_view_list.listbox.config(width=26)
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

    # view_frame.config(bd=10, relief=SOLID)

    global displayed_notebook_tab
    if entity_type == TABLES:
        notebook.select(0)
        displayed_notebook_tab = 1
    else:
        notebook.select(1)
        displayed_notebook_tab = 0

    print('displayed_notebook_tab : ', displayed_notebook_tab)

    def refresh_statusbar():
        # clear_grid_viewer_toolbar()

        global displayed_notebook_tab, displayed_table_name, displayed_view_name
        displayed_notebook_tab = 1 - displayed_notebook_tab
        print('displayed_notebook_tab : ', displayed_notebook_tab)
        print('displayed_table_name : ', displayed_table_name)
        print('displayed_view_name : ', displayed_view_name)
        if displayed_notebook_tab == 0:
            # tables
            main_window.status_label['text'] = displayed_table_name
        else:
            # views
            main_window.status_label['text'] = displayed_view_name
        main_window.selected_item_label['text'] = ''

    notebook.bind('<<NotebookTabChanged>>', lambda event: refresh_statusbar())

    ###########################################################################


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

        for i in range(len(DATABASE_TABLE_NAMES)):
            hlist.add(ts + '.' + DATABASE_TABLE_NAMES[i], text=INTERFACE_TABLE_NAMES[i])
        for i in range(len(DATABASE_VIEW_NAMES)):
            hlist.add(vs + '.' + DATABASE_VIEW_NAMES[i], text=INTERFACE_VIEW_NAMES[i])

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
