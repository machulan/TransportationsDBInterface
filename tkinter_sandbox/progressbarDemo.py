from tkinter import *
from tkinter.ttk import *

root = Tk()

pb = Progressbar(root)
pb.pack()

pb.config()
pb.step(70)

pb.start()
# pb.stop()


root.mainloop()