from tkinter import *
from tkinter import ttk as ttk

root = Tk()

tree = ttk.Treeview(root)
tree.pack()

tree["columns"] = ("one", "two")
tree.column("one", width=100)
tree.column("two", width=200)
tree.heading("one", text="column A")
tree.heading("two", text="column B")

tree.insert("", 0, text="", values=("1A", "1b"))


id2 = tree.insert("", 1, "dir2", text="", values=('ZZZ', 'YYY'))

tree.insert("", 3, "dir3", text="", values=('abacaba', 'aba'))
b = Button(text='BUTTON')
tree.insert("dir3", 3, text="sub dir 3", values=("3A", "3B"))
tree.insert("dir3", 3, text="sub dir 3", values=("3A"))


tree.insert("", 3, "dir4", text="", values=('abacaba', 'aba'))
b = Button(text='BUTTON')
tree.insert("dir4", 3, text="sub dir 4", values=("3A", "3B"))
tree.insert("dir4", 3, text="sub dir 4", values=('AbcdeAbcdeAbcdeAbcdeAbcdeAbcde', 'asd'))

#tree.selection_set(['dir3'])
tree.selection_toggle(['dir3'])


c = tree.get_children('dir3')
print(tree.selection())

root.mainloop()
