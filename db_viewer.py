from tkinter import *

from resourses.constants import *

import db_helper
import preferencies
import main_window


def run(root, account):
    print('DB_VIEWER [main_window.status_label] ::', main_window.status_label)

    # window = Toplevel(root)
    # window.title(VIEW_TITLE + ' [' + account.get_rights() + ']')
    # window.state('zoomed')
    # # window.resizable(width=True)
    #
    #
    # window.focus_set()
