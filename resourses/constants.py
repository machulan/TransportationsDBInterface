# Fonts
LOGIN_PASSWORD_FONT = ('consolas', 24, 'bold')
TOOLBAR_BUTTON_FONT = ('consolas', 12, 'bold')
STATUSBAR_LABEL_FONT = ('consolas', 12, 'italic')
RAW_QUERY_FONT = ('consolas', 20, 'bold')
REPORT_NAME_FONT = ('consolas', 16, 'bold')
TABLE_NAME_FONT = ('consolas', 20, 'bold')
VIEW_NAME_FONT = ('consolas', 20, 'bold')
ASK_DATE_DIALOG_LABEL_FONT = ('consolas', 12, '')

# Titles
ROOT_TITLE = 'Транспортные перевозки'
REPORT_LIST_WINDOW_TITLE = 'Отчеты'
TABLE_LIST_WINDOW_TITLE = 'Таблицы'
VIEW_LIST_WINDOW_TITLE = 'Представления'
VIEW_TITLE = 'Работа с базой данных'

# Data base settings
CONNECTION_DATA = {'server': "PC", 'port': 1433, 'user': "sa", 'password': "123456789", 'database': "Transportations"}

# Data base table information
DATABASE_TABLE_NAMES = ['Cars', 'Cities', 'Clients', 'Countries', 'Drivers', 'Dues', 'Goods', 'OrderGoodsPair',
                        'Orders',
                        'OrderTripPair', 'Regions', 'Trips']

DATABASE_VIEW_NAMES = ['IndexedViewCities1', 'ViewCars1', 'ViewCities1', 'ViewCitiesCountries1']

INTERFACE_TABLE_NAMES = ['Машины', 'Города', 'Клиенты', 'Страны', 'Водители', 'Пошлины', 'Товары', 'Заказ-Товар',
                         'Заказы', 'Заказ-Рейс', 'Регионы', 'Рейсы']

INTERFACE_VIEW_NAMES = ['Города 1', 'Машины 1', 'Города 2', 'Города и страны']

DATABASE_COLUMN_NAMES = [['car_id', 'car_model', 'color', 'car_type', 'weight', 'transportation_coefficient',
                          'travel_costs_per_kilometre', 'total_run'],
                         ['city_name', 'region_id', 'country_id', 'city_id'],
                         ['address', 'first_name', 'last_name', 'age', 'gender', 'client_id'],
                         ['country_id', 'country_name'],
                         ['driver_id', 'passport_number', 'first_name', 'last_name', 'insurance_number', 'experience',
                          'driver_licence_number', 'driver_licence_category'],
                         ['destination_country_id', 'ship_from_country_id', 'duty_value'],
                         ['goods_id', 'name', 'decription', 'transportation_cost_per_unit_weight', 'type'],
                         ['order_id', 'weight', 'amount', 'goods_id'],
                         ['destination_city_id', 'ship_from_city_id', 'order_id', 'order_status', 'profit',
                          'client_id'],
                         ['trip_id', 'order_id'],
                         ['country_id', 'region_id', 'region_name'],
                         ['trip_id', 'driver_id', 'car_id', 'start_time', 'end_time', 'distance']
                         ]

INTERFACE_COLUMN_NAMES = [['Идентификатор', 'Модель', 'Цвет', 'Тип', 'Вес', 'Коэффициент передвижения',
                           'Расходы на километр', 'Пробег'],
                          ['Название', 'Идентификатор региона', 'Идентификатор страны', 'Идентификатор'],
                          ['Адрес', 'Имя', 'Фамилия', 'Возраст', 'Пол', 'Идентификатор'],
                          ['Идентификатор', 'Название'],
                          ['Идентификатор', 'Серия и номер паспорта', 'Имя', 'Фамилия', 'Номер страховки', 'Опыт',
                           'Номер водительского удостоверения', 'Категории (подкатегории) водительского удостоверения'],
                          ['Страна пункта назначения', 'Страна пункта отправления', 'Размер таможенной пошлины'],
                          ['Идентификатор', 'Название', 'Описание', 'Расходы на перевозку единицы веса товара', 'Тип'],
                          ['Идентификатор заказа', 'Вес', 'Количество', 'Идентификатор товара'],
                          ['Идентификатор города пункта назначения', 'Идентификатор города пункта отправления',
                           'Идентификатор заказа', 'Статус', 'Прибыль', 'Идентификатор клиента'],
                          ['Идентификатор рейса', 'Идентификатор заказа'],
                          ['Идентификатор страны', 'Идентификатор региона', 'Название'],
                          ['Идентификатор рейса', 'Идентификатор водителя', 'Идентификатор машины', 'Время отправления',
                           'Время прибытия', 'Дистанция']
                          ]


# Preferencies

# Rights

# Functions
def do_nothing():
    print('Doing nothing...')
