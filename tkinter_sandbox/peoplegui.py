import tkinter
from tkinter.messagebox import showerror
import shelve

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')


def makeWidgets():
    global entries
    window = tkinter.Tk()
    window.title('People Shelve')
    form = tkinter.Frame(window)
    form.pack()
    entries = {}
    for (i, label) in enumerate(('key',) + fieldnames):
        lab = tkinter.Label(form, text=label)
        ent = tkinter.Entry(form)
        lab.grid(row=i, column=0)
        ent.grid(row=i, column=1)
        entries[label] = ent
    tkinter.Button(window, text='Fetch', command=fetchRecord).pack(side=tkinter.LEFT)
    tkinter.Button(window, text='Update', command=updateRecord).pack(side=tkinter.LEFT)
    tkinter.Button(window, text='Quit', command=window.quit).pack(side=tkinter.RIGHT)
    return window


def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, tkinter.END)
            entries[field].insert(0, repr(getattr(record, field)))

def temp():
    window = tkinter.Tk()
    window.title('People Shelve')
    form = tkinter.Frame(window)
    form.pack()
    e = tkinter.Entry(form)
    e.delete(0, tkinter.END)


class Person:
    def __init__(self, name='Unknown name', age=0, job='Unknown job', pay='Unknown pay'):
        self.name = name
        self.age = age
        self.job = job
        self.pay = pay

def updateRecord():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        # record = 'UNKNOWN RECORD'
        # from person import Person
        record = Person()

    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
# db.clear()
db['nikinsta'] = Person(name='Никита', age=20, job='Нет', pay=1900)
# name, age, job, pay
# db['nikinsta2'] = ['Никита', '20', 'Нет', '0']
# db['nikinsta'] = ['Никита', '20', 'Нет', '']
# print(*db.values())
# print(*db.keys())
# print(db['nikinsta'], db['nikinsta2'])
# print(*db.items())
# print(db.get('nikinsta').age)
window = makeWidgets()
window.mainloop()
db.close()
