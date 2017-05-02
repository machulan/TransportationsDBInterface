from tkinter import *

user_bg = 'red'


class HelloButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack()
        self.config(command=self.callback)

    def callback(self):
        print('Goodbye world...')
        self.quit()


class MyButton(HelloButton):
    def callback(self):
        print('MyButton, no quit!')


class ThemedButton(Button):
    def __init__(self, parent=None, **config):
        Button.__init__(self, parent, **config)
        self.pack(expand=YES, fill=BOTH)
        self.config(fg='red', bg=user_bg, font=('consolas', 12), relief=RAISED, bd=5)


def onSpam():
    print('onSpam')


def makeYellowUserBg():
    user_bg = 'yellow'
    yButton.config(bg=user_bg)


def makeGreenUserBg():
    user_bg = 'green'
    gButton.config(bg=user_bg)
    yButton.config(bg=user_bg)

if __name__ == '__main__':
    # HelloButton(text='Hello subclass world')
    # MyButton(text='MyButton')

    # B1 = ThemedButton(text='Spam', command=onSpam)
    # B2 = ThemedButton(text='eggs')
    # B2.pack(expand=YES, fill=BOTH)

    yButton = ThemedButton(text='make yellow', command=makeYellowUserBg)
    gButton = ThemedButton(text='make green', command=makeGreenUserBg)

    yButton.pack()
    gButton.pack()

    mainloop()
