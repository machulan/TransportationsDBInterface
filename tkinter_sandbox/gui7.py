from tkinter import *


class HelloPackage:
    def __init__(self, parent=None):
        self.top = Frame(parent)
        self.top.pack()
        self.data = 0
        self.b1 = None
        self.make_widgets()


    def make_widgets(self):
        self.b1 = Button(self.top, text='Bye', command=self.top.quit)
        self.b1.pack(side=LEFT)
        # Button(self.top, text='Hye', command=self.message).pack(side=RIGHT)
        Button(self.top, text='Hye', command=self.change_place).pack(side=RIGHT)
        # # #
        self.b1.config(state=DISABLED)

    def message(self):
        self.data += 1
        print('Hello number', self.data)

    def change_place(self):
        Button.__setattr__({})
        self.b1.pack(side=RIGHT)


if __name__ == '__main__':
    HelloPackage().top.mainloop()
