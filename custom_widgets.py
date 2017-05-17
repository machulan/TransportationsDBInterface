from tkinter import *

# http://effbot.org/tkinterbook/listbox.htm
# https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python#place.28.29.5B10.5D



class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)  # сделать растягиваемым
        self.makeWidgets(options)

    def handleList(self, event):
        index = self.listbox.curselection()  # при двойном щелчке на списке
        label = self.listbox.get(index)  # извлечь выбранный текст
        self.runCommand(label)  # и вызвать действие
        # или get(ACTIVE)

    def makeWidgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)  # связать sbar и list
        list.config(yscrollcommand=sbar.set)  # сдвиг одного = сдвиг другого
        sbar.pack(side=RIGHT, fill=Y)  # первым добавлен – посл. обрезан
        list.pack(side=LEFT, expand=YES, fill=BOTH)  # список обрезается первым
        pos = 0
        for label in options:  # добавить в виджет списка
            list.insert(pos, label)  # или insert(END,label)
            pos += 1  # или enumerate(options)
        # list.config(selectmode=SINGLE, setgrid=1) # режимы выбора, измен. разм.
        list.bind('<Double-1>', self.handleList)  # установить обр-к события
        self.listbox = list

    def runCommand(self, selection):  # необходимо переопределить
        print('You selected:', selection)


if __name__ == '__main__':
    options = (('Lumberjack - %s' % x) for x in range(20))  # или map/lambda,
    ScrolledList(options).mainloop()
