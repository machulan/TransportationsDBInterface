import tkinter

def set_preferencies():
    import shelve
    # admin = 'admin'
    # user = 'TestUser'
    db = shelve.open('preferencies')
    db['login_page'] = {'show_default_account': True,
                        'set_focus_on_enter_button': True,
                        'justify': tkinter.LEFT}

    # db['']
