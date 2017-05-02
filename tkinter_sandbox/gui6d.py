from tkinter import *
from tkinter_sandbox.gui6 import Hello

class HelloExtender(Hello):
    def make_widgets(self):
        Hello.make_widgets(self)
        Button(self, text="Extend", command=self.quit).pack(side=RIGHT)

    def message(self):
        # self.data *= 2
        # if self.data > 10 ** 3:
        #     self.data = 1
        print('hello', self.data)

if __name__ == '__main__':
    HelloExtender().mainloop()