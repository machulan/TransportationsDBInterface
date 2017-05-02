import sys
from tkinter import *
from tkinter_sandbox.gui6 import Hello

parent = Frame()
parent.pack(expand=YES, fill=BOTH)
Hello(parent).pack(side=RIGHT)

Button(parent, text='Attach', command=sys.exit).pack(side=LEFT, expand=YES, fill=BOTH)
parent.mainloop()