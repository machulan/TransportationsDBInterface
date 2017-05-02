from tkinter import *

root = Tk()
# root.wm_minsize(400, 300)
# root.wm_maxsize(500, 400)
labelfont = ('times', 20, 'bold roman')
# (family, size, style)
# family ::= Times, Courier, Helvetica, system (Windows)
# style ::= normal, bold, roman, italic, underline, overstrike
widget = Label(root, text='Hello config world')
widget.config(bg='orange', fg='yellow')
widget.config(font=labelfont)
widget.config(height=3, width=20)

widget.config(bd=20, relief=RIDGE)
# relief ::= FLAT, SUNKEN, RAISED, GROOVE, SOLID, RIDGE
widget.config(cursor='hand2')
# cursor ::= 'gumby', 'watch', 'pencil', 'cross', 'hand2'
widget.config(state=NORMAL)
# state ::= DISABLED, NORMAL, READONLY
widget.config(padx=100)

# widget.pack(expand=YES, fill=BOTH)
widget.pack(padx=50, pady=20)
root.mainloop()
