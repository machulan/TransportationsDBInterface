from tkinter import *
import db_helper
import custom_widgets
from resourses.constants import *
import main_window


class ScrolledReportList(Frame):
    def __init__(self, parent, reports, **options):
        Frame.__init__(self, parent, **options)
        # self.pack(expand=YES, fill=BOTH)  # сделать растягиваемым
        self.reports = reports
        self.make_widgets()

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

        self.listbox.config(selectmode=SINGLE, setgrid=1)
        self.listbox.bind('<Double-1>', self.handle_list)
        self.listbox.bind('<Return>', self.handle_list)

        # def run_command(self, selection):  # необходимо переопределить
        #   print('You selected:', selection)


def get_number_of_kilometers_traveled(report_name, account):
    print('Report getting window 0')
    window = Toplevel()
    window.title(report_name + ' [' + account.get_rights() + ']')
    window.focus_set()


def get_driver_path_lengths(report_name, account):
    print('Report getting window 1')


def get_profit_on_period(report_name, account):
    print('Report getting window 2')


def count_costs_on_company_development(report_name, account):
    print('Report getting window 3')


def year_profit_statistics(report_name, account):
    print('Report getting window 4')

def run(root, account):
    """В MAIN_FRAME"""

    # window = Toplevel(root)
    root.title(REPORT_LIST_WINDOW_TITLE + ' [' + account.get_rights() + ']')
    # window.wm_minsize(height=5, width=55)
    # window.maxsize(height=5)

    # main_window.status_label['text'] = 'Выбор отчета'
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

    scrolled_report_list = ScrolledReportList(main_window.main_frame, reports)
    scrolled_report_list.pack(side=LEFT, expand=NO, fill=Y)
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
