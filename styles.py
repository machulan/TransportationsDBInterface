import tkinter.ttk as ttk
import tkinter.font as tkinterfont

NOTEBOOK_STYLE = None


def set_styles():
    global NOTEBOOK_STYLE

    NOTEBOOK_FONT = tkinterfont.Font(family='consolas', size=-30)
    NOTEBOOK_STYLE = ttk.Style()
    # st.configure('.', font=f)
    NOTEBOOK_STYLE.configure('Notebook', font=NOTEBOOK_FONT)
