import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename, asksaveasfile, askopenfile, \
    askopenfiles

from resourses.constants import *

# from main import run

import shelve
import db_helper
import db_viewer
import login
import reports
import raw_query
import custom_widgets

toolbar = None
grid_viewer_toolbar1 = None
main_frame = None
statusbar = None
status_label = None
selected_item_label = None


# shelve.open(writeback=True)
# все загруженные записи будут сохраняться в кэше и автоматически записываться обратно в файл при закрытии хранилища.

def make_menu(root, account):
    root_menu = Menu(root)
    root.config(menu=root_menu)

    file_menu = Menu(root_menu, tearoff=False)
    file_menu.add_command(label='Открыть...', command=do_nothing)
    file_menu.add_separator()
    file_menu.add_command(label='Настройки...', command=do_nothing)
    file_menu.add_separator()
    file_menu.add_command(label='Выход из аккаунта', command=(lambda: login.run(root)))
    file_menu.add_command(label='Выход', command=root.quit)
    root_menu.add_cascade(label='Файл', menu=file_menu)

    report_menu = Menu(root_menu, tearoff=False)
    # report_names = db_helper.get_report_names()
    # print('REPORT NAMES :', report_names)
    # print('get_number_of_kilometers_traveled :', db_helper.get_number_of_kilometers_traveled(2))
    # print('get_driver_path_lengths :', db_helper.get_driver_path_lengths())
    # print('get_profit_on_period :', db_helper.get_profit_on_period((12, 1, 2015), (12, 4, 2015)))
    # print('count_costs_on_company_development :',
    #       db_helper.count_costs_on_company_development((12, 3, 2015), (13, 3, 2015)))
    # print('year_profit_statistics :', db_helper.year_profit_statistics())
    report_menu.add_command(label='Сгенерировать...', command=(lambda: reports.run(root, account)))
    root_menu.add_cascade(label='Отчет', menu=report_menu)

    if account.is_admin():
        tools_menu = Menu(root_menu, tearoff=False)
        tools_menu.add_command(label='SQL запрос к базе данных...', command=(lambda: raw_query.make_raw_query(root)))
        tools_menu.add_separator()
        tools_menu.add_command(label='Статистика', command=(lambda: do_nothing()))
        root_menu.add_cascade(label='Инструменты', menu=tools_menu)

    help_menu = Menu(root_menu, tearoff=False)
    help_menu.add_command(label='Просмотреть справку')
    help_menu.add_separator()
    help_menu.add_command(label='О программе')
    root_menu.add_cascade(label='Справка', menu=help_menu)



    # open_menu = Menu(root_menu, tearoff=False)
    # root_menu.add_cascade(label='Открыть', menu=open_menu)


class ToolbarButton(Button):
    def __init__(self, parent, **options):
        Button.__init__(self, parent, **options)
        self.config(font=TOOLBAR_BUTTON_FONT)
        self.config(fg='black', bg='#FFF')  # FFA


def make_toolbar(root, account):
    global toolbar

    toolbar = Frame(root)
    toolbar.pack(side=TOP, fill=X)
    toolbar.config(padx=5, pady=3)
    toolbar.config(bg='#CCF')  # FFA

    clear_main_frame_button = ToolbarButton(toolbar, text='Очистить main_frame')
    clear_main_frame_button.pack(side=LEFT, fill=Y)
    clear_main_frame_button.config(command=(lambda: clear_main_frame(root, account)))

    open_table_button = ToolbarButton(toolbar, text='Таблица...')
    open_table_button.pack(side=LEFT, fill=Y)
    open_table_button.config(command=(lambda: db_viewer.run(TABLES, root, account)))

    open_view_button = ToolbarButton(toolbar, text='Представление...')
    open_view_button.pack(side=LEFT, fill=Y)
    open_view_button.config(command=(lambda: db_viewer.run(VIEWS, root, account, )))

    if account.is_admin():
        make_row_query_button = ToolbarButton(toolbar, text='SQL запрос к базе данных...')
        make_row_query_button.pack(side=LEFT, fill=Y)
        make_row_query_button.config(command=(lambda: raw_query.make_raw_query(root)))

    make_report_button = ToolbarButton(toolbar, text='Отчет...')
    make_report_button.pack(side=LEFT, fill=Y)
    make_report_button.config(command=(lambda: reports.run(root, account)))

    logout_button = ToolbarButton(toolbar)
    logout_image_path = '../TransportationsDBInterface/resourses/logout2.png'
    logout_image = PhotoImage(file=logout_image_path)
    logout_button.config(image=logout_image, bg='#CCF', relief=FLAT)
    logout_button.image = logout_image
    logout_button.config(width=50, height=50)
    logout_button.pack(side=RIGHT)
    logout_button.config(command=(lambda: login.run(root)))
    logout_button.config(activebackground='#CCF', bd=0)

    preferencies_button = ToolbarButton(toolbar, text='Настройки')
    blue_referencies_path = '../TransportationsDBInterface/resourses/blue_preferencies2.png'
    blue_referencies_image = PhotoImage(file=blue_referencies_path)
    preferencies_button.config(image=blue_referencies_image, bg='#CCF', relief=FLAT)  # bg='#CCF'
    preferencies_button.image = blue_referencies_image
    preferencies_button.pack(side=RIGHT, fill=Y)
    preferencies_button.config(activebackground='#CCF', bd=0)

    search_button = ToolbarButton(toolbar)
    lens_image_path = '../TransportationsDBInterface/resourses/blue_lens.png'
    lens_image = PhotoImage(file=lens_image_path)
    search_button.config(image=lens_image, bg='#CCF',
                         relief=FLAT)  # relief ::= FLAT, SUNKEN, RAISED, GROOVE, SOLID, RIDGE
    search_button.image = lens_image
    search_button.config(width=50, height=50)
    search_button.pack(side=RIGHT)
    # search_button.bind('<ButtonPress>', lambda event: search_button.config(bg='#CCF'))
    search_button.config(activebackground='#CCF', bd=0)


def clear_grid_viewer_toolbar1():
    global grid_viewer_toolbar
    if not (grid_viewer_toolbar is None):
        grid_viewer_toolbar_copy = grid_viewer_toolbar.children.copy()
        for key, widget in grid_viewer_toolbar_copy.items():
            widget.destroy()
        # grid_viewer_toolbar


def make_grid_viewer_toolbar1(root, account):
    global grid_viewer_toolbar
    grid_viewer_toolbar = Frame(root)
    grid_viewer_toolbar.pack(side=TOP, fill=X)
    grid_viewer_toolbar.config(padx=5, pady=3)
    grid_viewer_toolbar.config(bg='#CCF')  # FFA


class StatusbarLabel(Label):
    def __init__(self, parent, **options):
        Label.__init__(self, parent, **options)
        self.config(font=STATUSBAR_LABEL_FONT)


def clear_selected_item_label():
    selected_item_label.config(text='')


def make_statusbar(root, account):
    global statusbar
    global status_label
    global selected_item_label

    statusbar = Frame(root)
    statusbar.pack(side=BOTTOM, fill=X)

    status_label = StatusbarLabel(statusbar)
    status_label.config(text='Ничего не открыто')
    status_label.pack(side=LEFT)

    selected_item_label = StatusbarLabel(statusbar)
    selected_item_label.config(text='Ничего не выбрано')
    selected_item_label.pack(side=LEFT, padx=50)

    account_label = StatusbarLabel(statusbar)
    account_label.config(text=account.get_rights() + ' : ' + account.name)
    account_label.pack(side=RIGHT)

    # widget.bind("<Control-Shift-KeyPress-q>", callback)


def clear_main_frame(root, account):
    root.title(ROOT_TITLE + ' [' + account.get_rights() + ']')

    global main_frame
    main_frame_copy = main_frame.children.copy()
    for key, widget in main_frame_copy.items():
        widget.destroy()

    bg_path = '../TransportationsDBInterface/resourses/gradient.png'
    bi = PhotoImage(file=bg_path)
    # blabel = Label(root, bg='#9AF')
    blabel = Label(main_frame, image=bi)  # , text='asd')  # , bg='#9AF')
    # blabel.place(x=-220, y=-50, relwidth=1.5, relheight=1.3)
    blabel.image = bi
    blabel.place(x=0, y=0, relwidth=1, relheight=1)

    # status_label['text'] = 'main_frame очищен'
    print('main_frame очищен')


def make_main_frame(root):
    global main_frame

    main_frame = Frame(root)
    main_frame.pack(expand=YES, fill=BOTH)
    # main_frame.config(image=)
    # main_frame.config(bg='red')

    bg_path = '../TransportationsDBInterface/resourses/gradient.png'
    bi = PhotoImage(file=bg_path)
    # blabel = Label(root, bg='#9AF')
    blabel = Label(main_frame, image=bi)  # , text='asd')  # , bg='#9AF')
    # blabel.place(x=-220, y=-50, relwidth=1.5, relheight=1.3)
    blabel.image = bi
    blabel.place(x=0, y=0, relwidth=1, relheight=1)
    # blabel.pack(expand=YES, fill=BOTH)

    show_demo_main_frame_button = False
    if show_demo_main_frame_button:
        btn = Button(main_frame, text='SDLFhds')
        btn.pack(expand=YES)


def run(root, account):
    # print(account.login, account.name, account.password, account.rights)
    root.title(ROOT_TITLE + ' [' + account.get_rights() + ']')

    make_menu(root, account)
    # make_toolbar(root, account)

    #make_grid_viewer_toolbar(root, account)

    make_main_frame(root)

    make_toolbar(root, account)

    make_statusbar(root, account)



    # print()
    # print('MAIN_WINDOW [main_window.main_frame] ::', main_frame)
    # print('MAIN_WINDOW [main_window.status_label] ::', status_label)

    # b = Button(root, text='Statusbar')
    # b.pack()
    # b.config(command=(lambda: print('MAIN_WINDOW [main_window.statusbar] ::', statusbar)
    # or print('MAIN_WINDOW [main_window.main_frame] ::', main_frame)))
