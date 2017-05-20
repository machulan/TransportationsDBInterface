from tkinter import *
import tkinter.tix as tix

from resourses.constants import *

import db_helper
import preferencies
import main_window


def run(root, account):
    main_window.status_label['text'] = 'Просмотр таблиц и представлений'

    print('DB_VIEWER [main_window.status_label] ::', main_window.status_label)

    main_window.clear_main_frame()

    hlist = tix.HList(main_window.main_frame)
    hlist.pack(side=LEFT, fill=Y)
    hlist.config(indent=14, drawbranch=TRUE, wideselection=FALSE)
    hlist.config(font=('consolas', 20, ''))

    hlist.add('f', text='f')
    hlist.add('s', text='s')

    hlist.add('f.f', text='f.f')
    hlist.add('f.s', text='f.s')

    hlist.add('s.f', text='s.f')
    hlist.add('s.s', text='s.s')

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
        label.config(relief=GROOVE) # SUNKEN FLAT RIDGE RAISED GROOVE SOLID
        main_window.main_frame.columnconfigure(j, weight=(j % 2) + 1)
    for i in range(len(data)):
        for j in range(len(column_names)):
            entry = Entry(main_window.main_frame)
            entry.grid(row=i+1, column=j, sticky=NSEW)
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
