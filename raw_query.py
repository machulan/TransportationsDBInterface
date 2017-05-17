from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename, asksaveasfile, askopenfile, \
    askopenfiles
import db_helper
import shelve

from resourses.constants import *


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
        if file_name == '':
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
