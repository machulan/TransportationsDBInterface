import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename, asksaveasfile, askopenfile, \
    askopenfiles

from resourses.constants import *
# from main import run

import shelve
import db_helper


# shelve.open(writeback=True)
# все загруженные записи будут сохраняться в кэше и автоматически записываться обратно в файл при закрытии хранилища.


class Account():
    def __init__(self, name='UNKNOWN', login='UNKNOWN', password='UNKNOWN', account_type='user'):
        self.name = name
        self.login = login
        self.password = password
        self.rights = account_type

    def is_user(self):
        return self.rights == 'user'

    def get_rights(self):
        if self.is_user():
            return 'Пользователь'
        return 'Администратор'

    def __repr__(self):
        return '(' + ', '.join([self.name, self.login, self.password, self.rights]) + ')'

    def __str__(self):
        return '(' + ', '.join([self.name, self.login, self.password, self.rights]) + ')'


def run_raw_query(text, raw_query):
    print('Running raw SQL query...')
    conn = db_helper.get_connection()

    cursor = conn.cursor()
    cursor.execute(raw_query)

    row = cursor.fetchone()
    if row:
        print('Making result table...')
        while row:
            print(row)
            row = cursor.fetchone()

    conn.close()


def make_raw_query(root):
    def cancel_making_query(db, text, window):
        data = text.get('1.0', END)
        if len(data) > 0 and (data[-1] == '\n' or data[-1] == '\r'):
            db['text'] = data[:-1]
        else:
            db['text'] = data
        db.close()
        window.destroy()

    def save_query_to_file(text):
        file = asksaveasfile(mode='w', defaultextension='.sql', filetypes=[('sql files', '.sql'), ('all files', '.*')],
                             initialdir='C:\\')
        if file is None:
            return
        data = text.get('1.0', END)
        print(type(data))
        if len(data) > 0 and (data[-1] == '\n' or data[-1] == '\r'):
            data = data[:-1]
        file.write(data)
        file.close()

    def open_query_from_file(text):
        file_name = askopenfilename(initialdir='C:\\Users\\User\\PycharmProjects\\TransportationsDBInterface\\',
                                    initialfile='query.sql', title='Открыть SQL файл',
                                    filetypes=[('sql files', '.sql'), ('all files', '.*')], defaultextension='.sql')
        if file_name is None:
            return
        file = open(file_name, 'r')
        data = file.read()
        print(type(data))
        text.insert('1.0', data)
        file.close()

    db = shelve.open('raw_query')
    if not db['text']:
        db['text'] = ''

    window = Toplevel(root)
    window.title('Запрос к базе данных')

    footer = Frame(window)
    footer.pack(side=BOTTOM, expand=NO, fill=X)

    open_query_button = Button(footer)
    open_query_button.config(text='Открыть', font=TOOLBAR_BUTTON_FONT)
    open_query_button.pack(side=LEFT)
    open_query_button.config(bg='#55F', fg='#000')
    open_query_button.config(command=(lambda: open_query_from_file(text)))

    save_query_button = Button(footer)
    save_query_button.config(text='Сохранить', font=TOOLBAR_BUTTON_FONT)
    save_query_button.pack(side=LEFT)
    save_query_button.config(bg='#FF5', fg='#000')
    save_query_button.config(command=(lambda: save_query_to_file(text)))

    cancel_button = Button(footer)
    cancel_button.config(text='Отмена', font=TOOLBAR_BUTTON_FONT)
    cancel_button.pack(side=RIGHT)
    cancel_button.config(bg='#F55')
    cancel_button.config(command=(lambda: cancel_making_query(db, text, window)))
    # PanedWindow

    run_query_button = Button(footer)
    run_query_button.config(text='Выполнить', font=TOOLBAR_BUTTON_FONT)
    run_query_button.pack(side=RIGHT)
    run_query_button.config(bg='#0F0', fg='#000')  # #F77 #7F7 '#1F1' #0F0

    text = Text(window)
    text.config(relief=SUNKEN, font=RAW_QUERY_FONT)
    text.config(bg='#333')  # '#35A')#FFA
    text.config(fg='white')
    text.config(height=10, width=45)  # cursor ::= 'gumby', 'watch', 'pencil', 'cross', 'hand2', 'xter'
    text.config(insertontime=500, insertofftime=500)
    text.config(cursor='xterm', insertwidth=5, insertbackground='white')
    text.config(wrap=WORD)
    text.insert('1.0', db['text'])

    yscrollbar = Scrollbar(window, orient=VERTICAL)
    yscrollbar.config(command=text.yview)
    yscrollbar.pack(side=RIGHT, fill=Y)

    xscrollbar = Scrollbar(window, orient=HORIZONTAL)
    xscrollbar.config(command=text.xview)
    # xscrollbar.pack(side=BOTTOM, fill=X)

    text.config(xscrollcommand=xscrollbar.set, yscrollcommand=yscrollbar.set)
    text.pack(expand=YES, fill=BOTH)
    text.focus_set()

    run_query_button.config(command=(lambda: run_raw_query(text, text.get('1.0', END))))

    # win.minsize(width=200, height=150)
    window.protocol('WM_DELETE_WINDOW', lambda: cancel_making_query(db, text, window))
    window.grab_set()
    window.focus_set()
    window.wait_window()


def make_menu(root, account):
    root_menu = Menu(root)
    root.config(menu=root_menu)

    file_menu = Menu(root_menu, tearoff=False)
    file_menu.add_command(label='Открыть...', command=do_nothing)
    file_menu.add_separator()
    file_menu.add_command(label='Настройки...', command=do_nothing)
    file_menu.add_separator()
    file_menu.add_command(label='Выход из аккаунта', command=(lambda: run_login(root)))
    file_menu.add_command(label='Выход', command=root.quit)
    root_menu.add_cascade(label='Файл', menu=file_menu)

    report_menu = Menu(root_menu, tearoff=False)
    report_names = db_helper.get_report_names()
    print('REPORT NAMES :', report_names)
    print('get_number_of_kilometers_traveled :', db_helper.get_number_of_kilometers_traveled(2))
    print('get_driver_path_lengths :', db_helper.get_driver_path_lengths())
    print('get_profit_on_period :', db_helper.get_profit_on_period((12, 1, 2015), (12, 4, 2015)))
    print('count_costs_on_company_development :',
          db_helper.count_costs_on_company_development((12, 3, 2015), (13, 3, 2015)))
    print('year_profit_statistics :', db_helper.year_profit_statistics())
    report_menu.add_command(label='')
    root_menu.add_cascade(label='Отчет', menu=report_menu)

    tools_menu = Menu(root_menu, tearoff=False)
    tools_menu.add_command(label='SQL запрос к базе данных...', command=(lambda: make_raw_query(root)))
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
    toolbar = Frame(root)
    toolbar.pack(side=TOP, fill=X)
    toolbar.config(padx=5, pady=3)
    toolbar.config(bg='#CCF')  # FFA

    open_table_button = ToolbarButton(toolbar, text='Таблица...')
    open_table_button.pack(side=LEFT, fill=Y)

    open_view_button = ToolbarButton(toolbar, text='Представление...')
    open_view_button.pack(side=LEFT, fill=Y)

    make_row_query_button = ToolbarButton(toolbar, text='SQL запрос к базе данных...')
    make_row_query_button.pack(side=LEFT, fill=Y)
    make_row_query_button.config(command=(lambda: make_raw_query(root)))

    search_button = ToolbarButton(toolbar)
    lens_path = '../TransportationsDBInterface/resourses/blue_lens.png'
    lens_image = PhotoImage(file=lens_path)
    search_button.config(image=lens_image, bg='#FFF')
    search_button.image = lens_image
    search_button.config(width=50, height=50)
    search_button.pack(side=RIGHT)

    preferencies_button = ToolbarButton(toolbar, text='Настройки')
    blue_referencies_path = '../TransportationsDBInterface/resourses/blue_preferencies2.png'
    blue_referencies_image = PhotoImage(file=blue_referencies_path)
    preferencies_button.config(image=blue_referencies_image, bg='#FFF')  # bg='#CCF'
    preferencies_button.image = blue_referencies_image
    preferencies_button.pack(side=RIGHT, fill=Y)


class FooterLabel(Label):
    def __init__(self, parent, **options):
        Label.__init__(self, parent, **options)
        self.config(font=FOOTER_LABEL_FONT)


def make_footer(root, account):
    footer = Frame(root)
    footer.pack(side=BOTTOM, fill=X)

    current_entity_label = FooterLabel(footer)
    current_entity_label.config(text='Ничего не выбрано')
    current_entity_label.pack(side=LEFT)

    current_account_rights_label = FooterLabel(footer)
    current_account_rights_label.config(text=account.get_rights() + ' : ' + account.name)
    current_account_rights_label.pack(side=RIGHT)

    # widget.bind("<Control-Shift-KeyPress-q>", callback)
    return footer


def make_main_frame(root):
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

    btn = Button(main_frame, text='SDLFhds')
    btn.pack(expand=YES)


def run(root, account):
    # print(account.login, account.name, account.password, account.rights)
    root.title(ROOT_TITLE + ' [' + account.get_rights() + ']')

    make_menu(root, account)

    # make_toolbar(root, account)

    make_main_frame(root)

    make_toolbar(root, account)

    make_footer(root, account)


def try_enter(login, password, login_entry, password_entry, input_frame, root):
    print('Попытка ввести логин [', login, '] и пароль [', password, ']')

    db = shelve.open('accounts')
    # for key in db:
    #    print(key, '=> \n ', db[key])
    # print(db['admin'])

    for name, account in db.items():
        if account.login == login and account.password == password:
            rights = account.rights
            input_frame.destroy()
            print(name, 'успешно вошел в систему под логином [', login, '] и паролем [', password, '] с правами',
                  rights)
            db.close()
            run(root, account)
            return

    login_entry.config(bg='#FCC')
    password_entry.config(bg='#FCC')

    db.close()


def run_login(root):
    preferencies = shelve.open('preferencies')

    root.title(ROOT_TITLE)

    path = r'C:\Users\User\PycharmProjects\TransportationsDBInterface\resourses\transportations.jpg'
    path1 = '.\\resourses\\transportations.jpg'
    path2 = r'C:\Users\User\PycharmProjects\TransportationsDBInterface\resourses\transportations2.png'
    # path3 = '../TransportationsDBInterface/resourses/transportations2.png'
    # bi = tkinter.PhotoImage(file=path3)
    # blabel = tkinter.Label(root, image=bi, text='asd', bg='#9AF')
    # blabel.place(x=-220, y=-50, relwidth=1.5, relheight=1.3)




    # bi.config(width=10, height=10)
    # blabel.bind('<Configure>', lambda event: event.width)

    # canv = Canvas(root)
    # canv.pack(fill=BOTH)
    # canv.config(width=bi.width(), height=bi.height())
    # canv.create_image(2, 2, image=bi, anchor=NW)


    # btn = tkinter.Button(root, text='adkfdjf')
    # btn.pack()
    # blabel.pack()

    # io = Image.open('.\\resourses\\transportations.jpg')
    # l = Label(root)
    # root.withdraw()
    root_copy = root.children.copy()
    for key, widget in root_copy.items():
        widget.destroy()

    path5 = '../TransportationsDBInterface/resourses/gradient.png'
    path4 = '../TransportationsDBInterface/resourses/showing.gif'
    path3 = '../TransportationsDBInterface/resourses/transportations2.png'
    bi = PhotoImage(file=path5)
    bi.config(gamma=1)
    # blabel = Label(root, bg='#9AF')
    blabel = Label(root, image=bi)  # , text='asd')  # , bg='#9AF')
    # blabel.place(x=-220, y=-50, relwidth=1.5, relheight=1.3)
    blabel.image = bi
    blabel.place(x=0, y=0, relwidth=1, relheight=1)
    # blabel.pack(expand=YES, fill=BOTH)

    # print('LABEL')

    input_frame = Frame(root)
    input_frame.config(width=300, height=200)
    # input_frame.config(bd=5, relief=SOLID) # relief ::= FLAT, SUNKEN, RAISED, GROOVE, SOLID, RIDGE
    input_frame.config(bg='#FFF')  # bg='#CCF'
    input_frame.pack(expand=YES)
    # input_frame.geometry(newGeometry='300x300+200+200')
    input_frame.place(x=150, y=220)  # , relwidth=1, relheight=1)

    login_label = Label(input_frame)
    login_label.config(text='Логин', font=LOGIN_PASSWORD_FONT)
    login_label.config(bg='#CCF')
    # login_label.pack(anchor=W)

    login_entry = Entry(input_frame)
    login_entry.config(font=LOGIN_PASSWORD_FONT, insertofftime=500, insertontime=500)
    # login_entry.config(cursor='xterm')
    login_entry.config(justify=preferencies['login_page']['justify'])
    login_entry.config(bg='#FFA')
    if preferencies['login_page']['show_default_account']:
        login_entry.insert(0, 'admin')
    if not preferencies['login_page']['set_focus_on_enter_button']:
        login_entry.focus_set()
    login_entry.pack(expand=NO, padx=30, pady=20)

    password_label = Label(input_frame)
    password_label.config(text='Пароль', font=LOGIN_PASSWORD_FONT)
    password_label.config(bg='#CCF')
    # password_label.pack(anchor=W)

    password_entry = Entry(input_frame)
    password_entry.config(show='*', font=LOGIN_PASSWORD_FONT, insertofftime=500, insertontime=500)
    password_entry.config(justify=preferencies['login_page']['justify'])
    password_entry.config(bg='#FFA')
    if preferencies['login_page']['show_default_account']:
        password_entry.insert(0, 'admin')
    password_entry.pack(expand=NO, padx=30, pady=20)

    enter_button = Button(input_frame)
    enter_button.config(text='Войти', font=LOGIN_PASSWORD_FONT)
    enter_button.config(bg='#35F', fg='#FFF')  # bg='#77F'
    # enter_button.config(width=10)#, justify=CENTER)
    enter_button.config(activebackground='#25C', activeforeground='#FFF')
    enter_button.config(command=(
        lambda: try_enter(login_entry.get(), password_entry.get(), login_entry, password_entry, input_frame, root)))
    # enter_button.bind('<Tab>', lambda event: enter_button.focus_set)
    # enter_button.focus_set()
    if preferencies['login_page']['set_focus_on_enter_button']:
        enter_button.focus_set()
    enter_button.pack(side=LEFT, padx=30, pady=20, expand=YES, fill=X)

    exit_button = Button(input_frame)
    exit_button.config(text='Выход', font=LOGIN_PASSWORD_FONT)
    exit_button.config(command=root.quit)
    # exit_button.config(width=10)#, justify=CENTER)
    exit_button.config(bg='#F55')  # , fg='#FFF') bg='#7F7'
    exit_button.config(activebackground='#F77')
    exit_button.pack(side=RIGHT, padx=30, pady=20, expand=YES, fill=X)


if __name__ == '__main__':
    admin = Account('admin', 'admin', 'admin', 'admin')
    db = shelve.open('accounts')
    db['admin'] = admin
