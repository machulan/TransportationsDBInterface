import tkinter
from tkinter import *

from resourses.constants import *

import shelve


class Account():
    def __init__(self, login='UNKNOWN', password='UNKNOWN', account_type='user'):
        self.login = login
        self.password = password
        self.rights = account_type

    def is_user(self):
        return self.rights == 'user'


def try_enter(login, password):
    print('trying to enter with login [', login, '] and password [', password, ']')

    db = shelve.open('accounts')
    for key in db:
        print(key, '=> \n ', db[key])
    print(db['admin'])
    db.close()


def login(root):
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
    login_entry.config(font=LOGIN_PASSWORD_FONT, justify=CENTER, insertofftime=500, insertontime=500)
    # login_entry.config(cursor='xterm')
    login_entry.config(justify=LEFT)
    login_entry.config(bg='#FFA')
    login_entry.focus_set()
    login_entry.pack(expand=NO, padx=30, pady=20)

    password_label = Label(input_frame)
    password_label.config(text='Пароль', font=LOGIN_PASSWORD_FONT)
    password_label.config(bg='#CCF')
    # password_label.pack(anchor=W)

    password_entry = Entry(input_frame)
    password_entry.config(show='*', font=LOGIN_PASSWORD_FONT, insertofftime=500, insertontime=500)
    password_entry.config(justify=LEFT)
    password_entry.config(bg='#FFA')
    password_entry.pack(expand=NO, padx=30, pady=20)

    enter_button = Button(input_frame)
    enter_button.config(text='Войти', font=LOGIN_PASSWORD_FONT)
    enter_button.config(bg='#35F', fg='#FFF')  # bg='#77F'
    # enter_button.config(width=10)#, justify=CENTER)
    enter_button.config(command=(lambda: try_enter(login_entry.get(), password_entry.get())))
    enter_button.pack(side=LEFT, padx=30, pady=20, expand=YES, fill=X)

    exit_button = Button(input_frame)
    exit_button.config(text='Выход', font=LOGIN_PASSWORD_FONT)
    exit_button.config(command=root.quit)
    # exit_button.config(width=10)#, justify=CENTER)
    exit_button.config(bg='#F77')  # , fg='#FFF') bg='#7F7'
    exit_button.pack(side=RIGHT, padx=30, pady=20, expand=YES, fill=X)


if __name__ == '__main__':
    admin = Account('admin', 'admin', 'admin')
