import tkinter
from tkinter.messagebox import showinfo


class MyGui(tkinter.Frame):
    def __init__(self, parent=None):
        tkinter.Frame.__init__(self, parent)
        button = tkinter.Button(self, text='press', command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='popup', message='Button pressed!')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()


    # if __name__ == '__main__':
    #     import tkinter
    #     from tkinter.messagebox import showinfo
    #
    #     #tkinter.Label(text='Spam').pack()
    #
    #     def reply():
    #         showinfo(title='popup', message='Button pressed!')
    #
    #     window = tkinter.Tk()
    #     button = tkinter.Button(window, text='press', command=reply)
    #     button.pack()
    #     window.mainloop()
    #
    #     #tkinter.mainloop()
