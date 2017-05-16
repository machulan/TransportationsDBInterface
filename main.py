from tkinter import *
import login

root = Tk()


root.state('zoomed')
root.title('Транспортные перевозки')
root.minsize(width=1000, height=500)

# root.protocol('WM_ICONIFY_WINDOW', lambda: None)
root.resizable(width=False, height=False)
# root.maxsize(width=1000, height=1000)
# root.config(bg='#000')

path3 = '../TransportationsDBInterface/resourses/transportations2.png'
bi = PhotoImage(file=path3)
blabel = Label(root, image=bi, text='asd', bg='#9AF')
blabel.place(x=-220, y=-50, relwidth=1.5, relheight=1.3)

login.login(root)

root.mainloop()
