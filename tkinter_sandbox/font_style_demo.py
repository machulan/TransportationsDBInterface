from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkfont


root = Tk()

f = tkfont.Font(family='consolas', size=-30)
st = ttk.Style()
#st.configure('.', font=f)
#st.configure('Notebook', font=f)

nb = ttk.Notebook(root)
nb.pack(fill='both', expand=1)
t = Text(nb, font=f)
nb.add(t, text='foo')
c = Canvas(nb)
nb.add(c, text='bar')

def toggle_font(event):
    if event.keysym == '0':
        f['size'] = -12
    elif event.keysym == 'plus':
        if f['size'] > -31:
            f['size'] = f['size'] - 1
    elif event.keysym == 'minus':
        if f['size'] < -6:
            f['size'] = f['size'] + 1

root.bind('<Control-plus>', toggle_font)
root.bind('<Control-minus>', toggle_font)
root.bind('<Control-0>', toggle_font)

root.mainloop()