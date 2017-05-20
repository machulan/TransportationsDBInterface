from tkinter import *
import db_helper
import custom_widgets
from resourses.constants import *
import main_window

# from main import root

report_frame = None


class ScrolledReportList(Frame):
    def __init__(self, parent, reports, root, **options):
        Frame.__init__(self, parent, **options)
        # self.pack(expand=YES, fill=BOTH)  # сделать растягиваемым
        self.reports = reports
        self.make_widgets()
        self.root = root

    def handle_list(self, event):
        index = self.listbox.curselection()[0]  # при двойном щелчке на списке
        # report_name = self.listbox.get(index)

        report = self.reports[index]
        print('Report [', report[0], '] was chosen')
        report[1]()
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

        for pos, (report_name, report_function) in enumerate(self.reports):
            self.listbox.insert(pos, report_name)

        self.listbox.config(selectmode=SINGLE)  # , setgrid=1)
        self.listbox.bind('<Double-1>', self.handle_list)
        self.listbox.bind('<Return>', self.handle_list)

        # def run_command(self, selection):  # необходимо переопределить
        #   print('You selected:', selection)


class ScrolledCanvas(Canvas):
    def __init__(self, master, **options):
        Canvas.__init__(self, master, **options)

        self.scrollbar = Scrollbar(master, orient=VERTICAL)
        # self.canvas = Canvas(self, 0, 0, bg='yellow')

        self.scrollbar.config(command=self.yview)
        self.config(yscrollcommand=self.scrollbar.set)

        self.pack(side=LEFT, expand=YES, fill=BOTH)
        self.scrollbar.pack(side=LEFT, fill=Y)


class ScrolledFrame(Frame):
    def __init__(self, master=None, **options):
        Frame.__init__(self, master, **options)

        self.canvas = Canvas(self)
        self.canvas.pack(side=LEFT, expand=YES, fill=BOTH)

        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, orient=VERTICAL, fill=Y)

        self.scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=NW)


def get_number_of_kilometers_traveled(report_name, root, account):
    print('Report getting window 0')
    # main.root.title()
    main_window.status_label['text'] = 'Отчет : ' + report_name
    # window = Toplevel()
    # window.title(report_name + ' [' + account.get_rights() + ']')
    # window.focus_set()
    global report_frame

    report_arguments_frame = Frame(report_frame)
    report_frame.pack()

    report_viewer_frame = Frame(report_frame)
    report_frame.pack()


def get_driver_path_lengths(report_name, root, account):
    print('Report getting window 1')
    main_window.status_label['text'] = 'Отчет : ' + report_name
    # window = Toplevel()
    # window.title(report_name + ' [' + account.get_rights() + ']')
    # window.focus_set()
    global report_frame
    global report_viewer_frame

    # report_viewer_frame = ScrolledFrame(report_frame)
    # report_viewer_frame.pack(expand=YES, fill=BOTH)
    scrolled_canvas = ScrolledCanvas(report_frame)
    scrolled_canvas.pack(expand=YES, fill=BOTH)
    report_viewer_frame = Frame(scrolled_canvas)
    scrolled_canvas.create_window((0, 0), window=report_viewer_frame, anchor=NW)

    report_viewer_frame.config(bg='red')

    report_viewer_frame.config(width=500, height=2000)

    import tkinter.tix as tix
    #bln = tix.Balloon(report_viewer_frame)
    # b = Button(report_viewer_frame, text='ASD:AKD')


    # tix.Tli
    import Pmw.Pmw_2_0_1.demos.Balloon
    return

    report_data = db_helper.get_driver_path_lengths()

    #canvas = ScrolledCanvas(report_viewer_frame)  # , bg='green')#, width=200, height=300, bg='green')
    #canvas.pack(expand=YES, fill=BOTH)

    column_names = ['Идентификатор', 'Имя', 'Фамилия', 'Длина пути']
    column_count = len(column_names)

    for j in range(len(column_names)):
        label = Label(report_viewer_frame)
        label.grid(row=0, column=j, sticky=NSEW)
        label.config(text=column_names[j])
        label.config(relief=GROOVE)  # SUNKEN FLAT RIDGE RAISED GROOVE SOLID
        report_viewer_frame.columnconfigure(j, weight=1)

    print(len(report_data))

    for i in range(30):
        for j in range(column_count):
            entry = Entry(report_viewer_frame)
            entry.grid(row=i + 1, column=j, sticky=NSEW)
            entry.insert(END, report_data[i][j])
            entry.config(justify=CENTER)
            report_viewer_frame.columnconfigure(j, weight=1)
        report_viewer_frame.rowconfigure(i, weight=1)


def get_profit_on_period(report_name, root, account):
    print('Report getting window 2')


def count_costs_on_company_development(report_name, root, account):
    print('Report getting window 3')


def year_profit_statistics(report_name, root, account):
    print('Report getting window 4')


def run(root, account):
    """В MAIN_FRAME"""

    # window = Toplevel(root)
    root.title(REPORT_LIST_WINDOW_TITLE + ' [' + account.get_rights() + ']')
    # window.wm_minsize(height=5, width=55)
    # window.maxsize(height=5)

    main_window.status_label['text'] = 'Выбор отчета'
    # print('REPORTS [main_window.statusbar] ::', main_window.statusbar)
    # main_window.statusbar = Frame(root)
    # main_window.statusbar.pack()
    # print('REPORTS [main_window.statusbar] ::', main_window.statusbar)
    # print('REPORTS [main_window.main_frame] ::', main_window.main_frame)

    main_window.clear_main_frame()
    paned_window = PanedWindow(main_window.main_frame)
    paned_window.pack(fill=BOTH, expand=YES, side=LEFT)
    paned_window.config(orient=HORIZONTAL)
    paned_window.config(sashrelief=GROOVE, sashwidth=10)  # relief ::= FLAT, SUNKEN, RAISED, GROOVE, SOLID, RIDGE

    # b = Button(main_window.main_frame, text='ЗАГЛУШКА')
    # b.pack()

    report_names = [
        'Количество километров в пути для заданного водителя',
        'Количество километров в пути для всех водителей',
        'Расчет прибыли за заданный период',
        'Расчет затрат на развитие предприятия за период',
        'Статистика доходов предприятия по годам за все время'
    ]

    report_functions = [
        lambda: get_number_of_kilometers_traveled(report_names[0], root, account),
        lambda: get_driver_path_lengths(report_names[1], root, account),
        lambda: get_profit_on_period(report_names[2], root, account),
        lambda: count_costs_on_company_development(report_names[3], root, account),
        lambda: year_profit_statistics(report_names[4], root, account)
    ]

    reports = [(report_names, report_function) for report_names, report_function in zip(report_names, report_functions)]

    # listbox = Listbox(main_window.main_frame, relief=SUNKEN)
    # listbox.pack(side=LEFT, expand=NO, fill=Y)  # список обрезается первым
    # for pos, (report_name, report_function) in enumerate(reports):
    #     listbox.insert(pos, report_name)
    # listbox.config(selectmode=SINGLE)# , setgrid=1)
    # def handle_list(event):
    #     index = listbox.curselection()[0]  # при двойном щелчке на списке
    #     # report_name = self.listbox.get(index)
    #     report = reports[index]
    #     print('Report [', report[0], '] was chosen')
    #     report[1]()
    main_window.status_label['text'] = 'Выбор отчета'
    # listbox.bind('<Double-1>', handle_list)
    # listbox.bind('<Return>', handle_list)

    # scrolled_report_list = ScrolledReportList(main_window.main_frame, reports, root)
    scrolled_report_list = ScrolledReportList(paned_window, reports, root)
    # scrolled_report_list.pack(side=LEFT, expand=NO, fill=Y)
    paned_window.add(scrolled_report_list)
    scrolled_report_list.listbox.config(width=55)
    scrolled_report_list.listbox.config(font=REPORT_NAME_FONT)
    scrolled_report_list.listbox.config(selectmode=BROWSE, activestyle=DOTBOX)  # setgrid=10) '#5F5' - light green
    scrolled_report_list.listbox.config(selectbackground='#5F5', selectforeground='black')
    scrolled_report_list.listbox.config(selectborderwidth=5, relief=FLAT, exportselection=0, cursor='hand2')
    # scrolled_report_list.listbox.curselection()
    # scrolled_report_list.listbox.select_anchor(2)
    scrolled_report_list.listbox.select_set(0)
    scrolled_report_list.listbox.focus_set()

    scrolled_report_list.listbox.config(bg='#EEE')
    scrolled_report_list_item_colors = ['#DDD', '#AAA']  # ['#CCF', '#EEF']
    for pos in range(len(scrolled_report_list.reports)):
        scrolled_report_list.listbox.itemconfig(pos, background=scrolled_report_list_item_colors[pos % 2])

    # scrolled_report_list2 = ScrolledReportList(paned_window, reports, root)
    # paned_window.add(scrolled_report_list2)
    global report_frame
    report_frame = Frame(paned_window)
    paned_window.add(report_frame)
    # report_frame.config()

    report_frame.config(bd=10, relief=SOLID)

    # li = (str(x * x) for x in range(5))

    # scrolled_list = custom_widgets.ScrolledList(li, window)
    # scrolled_list.listbox.config(selectmode=SINGLE)  # selectmode=EXTENDED or SINGLE or BROWSE or MULTIPLE

    # TODO reports

    show_demo_reports = False
    if show_demo_reports:
        report_names = db_helper.get_report_names()
        print('REPORT NAMES :', report_names)
        print('get_number_of_kilometers_traveled :', db_helper.get_number_of_kilometers_traveled(2))
        print('get_driver_path_lengths :', db_helper.get_driver_path_lengths())
        print('get_profit_on_period :', db_helper.get_profit_on_period((12, 1, 2015), (12, 4, 2015)))
        print('count_costs_on_company_development :',
              db_helper.count_costs_on_company_development((12, 3, 2015), (13, 3, 2015)))
        print('year_profit_statistics :', db_helper.year_profit_statistics())

        # window.protocol('WM_DELETE_WINDOW', lambda: None)
        # window.grab_set()
        # window.focus_set()
        # window.wait_window()


def run2(root, account):
    """НОВОЕ ОКНО"""

    window = Toplevel(root)
    window.title(REPORT_LIST_WINDOW_TITLE + ' [' + account.get_rights() + ']')
    window.wm_minsize(height=5, width=55)
    window.maxsize(height=5)

    main_window.status_label['text'] = 'Выбор отчета'
    # print('REPORTS [main_window.statusbar] ::', main_window.statusbar)
    # main_window.statusbar = Frame(root)
    # main_window.statusbar.pack()
    # print('REPORTS [main_window.statusbar] ::', main_window.statusbar)

    report_names = [
        'Количество километров в пути для заданного водителя',
        'Количество километров в пути для всех водителей',
        'Расчет прибыли за заданный период',
        'Расчет затрат на развитие предприятия за период',
        'Статистика доходов предприятия по годам за все время'
    ]

    report_functions = [
        lambda: get_number_of_kilometers_traveled(report_names[0], account),
        lambda: get_driver_path_lengths(report_names[1], account),
        lambda: get_profit_on_period(report_names[2], account),
        lambda: count_costs_on_company_development(report_names[3], account),
        lambda: year_profit_statistics(report_names[4], account)
    ]

    reports = [(report_names, report_function) for report_names, report_function in zip(report_names, report_functions)]

    scrolled_report_list = ScrolledReportList(window, reports)
    scrolled_report_list.pack(expand=YES, fill=BOTH)
    scrolled_report_list.listbox.config(font=REPORT_NAME_FONT)
    scrolled_report_list.listbox.config(selectmode=BROWSE, activestyle=DOTBOX)  # setgrid=10) '#5F5' - light green
    scrolled_report_list.listbox.config(selectbackground='#5F5', selectforeground='black')
    scrolled_report_list.listbox.config(selectborderwidth=5, relief=FLAT, exportselection=0, cursor='hand2')
    # scrolled_report_list.listbox.curselection()
    # scrolled_report_list.listbox.select_anchor(2)
    scrolled_report_list.listbox.select_set(0)
    scrolled_report_list.listbox.focus_set()

    scrolled_report_list.listbox.config(bg='#EEE')
    scrolled_report_list_item_colors = ['#DDD', '#AAA']  # ['#CCF', '#EEF']
    for pos in range(len(scrolled_report_list.reports)):
        scrolled_report_list.listbox.itemconfig(pos, background=scrolled_report_list_item_colors[pos % 2])

    # li = (str(x * x) for x in range(5))

    # scrolled_list = custom_widgets.ScrolledList(li, window)
    # scrolled_list.listbox.config(selectmode=SINGLE)  # selectmode=EXTENDED or SINGLE or BROWSE or MULTIPLE

    # TODO reports

    show_demo_reports = False
    if show_demo_reports:
        report_names = db_helper.get_report_names()
        print('REPORT NAMES :', report_names)
        print('get_number_of_kilometers_traveled :', db_helper.get_number_of_kilometers_traveled(2))
        print('get_driver_path_lengths :', db_helper.get_driver_path_lengths())
        print('get_profit_on_period :', db_helper.get_profit_on_period((12, 1, 2015), (12, 4, 2015)))
        print('count_costs_on_company_development :',
              db_helper.count_costs_on_company_development((12, 3, 2015), (13, 3, 2015)))
        print('year_profit_statistics :', db_helper.year_profit_statistics())

    # window.protocol('WM_DELETE_WINDOW', lambda: None)
    # window.grab_set()
    window.focus_set()
    # window.wait_window()
