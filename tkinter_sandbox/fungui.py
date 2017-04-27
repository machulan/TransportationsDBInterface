import tkinter
import random

fontsize = 30
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'cyan', 'purple']


def onSpam():
    popup = tkinter.Toplevel()
    color = random.choice(colors)
    tkinter.Label(popup, text='Popup', bg='black', fg=color).pack(fill=tkinter.BOTH)
    mainLabel.config(fg=color)


def onFlip():
    mainLabel.config(fg=random.choice(colors))
    main.after(1000, onFlip)


def onGrow():
    global fontsize
    fontsize = random.randint(20, 22)
    mainLabel.config(font=('arial', fontsize, 'italic'))
    main.after(10, onGrow)


main = tkinter.Tk()
mainLabel = tkinter.Label(main, text='FunGui!', relief=tkinter.RAISED)
mainLabel.config(font=('arial', fontsize, 'italic'),
                 fg='cyan', bg='navy')
mainLabel.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)
tkinter.Button(main, text='spam', command=onSpam).pack(fill=tkinter.X)
tkinter.Button(main, text='flip', command=onFlip).pack(fill=tkinter.X)
tkinter.Button(main, text='grow', command=onGrow).pack(fill=tkinter.X)
main.mainloop()
