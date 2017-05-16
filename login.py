import tkinter
from tkinter import *

from resourses.constants import *
# from main import run

import shelve


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
    root_menu.add_cascade(label='Отчеты', menu=report_menu)

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


def make_footer(root, account):
    footer = Frame(root)
    footer.pack(side=BOTTOM, fill=X)

    current_entity_label = Label(footer)
    current_entity_label.config(text='Ничего не выбрано')
    current_entity_label.pack(side=LEFT)

    # widget.bind("<Control-Shift-KeyPress-q>", callback)


def run(root, account):
    # print(account.login, account.name, account.password, account.rights)
    make_menu(root, account)

    make_toolbar(root, account)

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
