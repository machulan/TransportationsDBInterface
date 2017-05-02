# askopenfilename, askcolor, askquestion, showerror, askfloat, askdirectory
# определяет таблицу имя:обработчик с демонстрационными примерами

from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.colorchooser import askcolor
from tkinter.messagebox import askquestion, showerror
from tkinter.simpledialog import askfloat

demos = {
    'Open': lambda: askopenfilename(initialdir='C:\\wamp64', initialfile='неизвестный ФАЙЛ',
                                    title='НАЗВАНИЕ ДИАЛОГА', defaultextension='txt'),
    'Open dir': lambda: askdirectory(title='DS<JHSD', initialdir='D:\\'),
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He's dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}
