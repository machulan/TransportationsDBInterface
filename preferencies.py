import tkinter


def set_preferencies():
    clear_preferencies = True

    import shelve
    # admin = 'admin'
    # user = 'TestUser'

    db = shelve.open('preferencies')

    if clear_preferencies:
        db.clear()

    db['login_page'] = {'show_default_account': True,
                        'set_focus_on_enter_button': True,
                        'justify': tkinter.LEFT}

    import db_helper

    report_names = [
        'Подсчет количества километров в пути для заданного водителя',
        'Подсчет количетсва километров в пути для всех водителей',
        'Расчет прибыли за заданный период',
        'Расчет затрат на развитие предприятия за период',
        'Статистика доходов предприятия по годам за все время'
    ]

    report_functions = [
        db_helper.get_number_of_kilometers_traveled,
        db_helper.get_driver_path_lengths,
        db_helper.get_profit_on_period,
        db_helper.count_costs_on_company_development,
        db_helper.year_profit_statistics
    ]

    db['reports'] = {}
