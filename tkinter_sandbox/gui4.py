from tkinter import *

w = Frame()
w.pack(side=TOP, expand=YES, fill=Y)


# BUTTON 1
def button1_pressed():
    print('Button 1 is pressed')
    l.config(text='Button 1 is pressed')
    b.config(text='PRESSED!')


b = Button(w, text='Hello', command=button1_pressed)
b.pack(side=LEFT, fill=Y)

# LABEL
l = Label(w, text='Hello container world')
l.pack(side=TOP)

# BUTTON 2
def button2_pressed():
    print('Button 2 is pressed')
    w.quit()


Button(w, text='Quit', command=button2_pressed).pack(side=RIGHT, expand=YES, fill=X)
# Button(text='Quit', command=button2_pressed).pack(anchor=SW, padx=100, pady=30, expand=YES, fill=BOTH)

w.mainloop()
