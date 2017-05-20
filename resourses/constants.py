# Fonts
LOGIN_PASSWORD_FONT = ('consolas', 24, 'bold')
TOOLBAR_BUTTON_FONT = ('consolas', 12, 'bold')
STATUSBAR_LABEL_FONT = ('consolas', 12, 'italic')
RAW_QUERY_FONT = ('consolas', 20, 'bold')
REPORT_NAME_FONT = ('consolas', 16, 'bold')
TABLE_NAME_FONT = ('consolas', 20, 'bold')
VIEW_NAME_FONT = ('consolas', 20, 'bold')

# Titles
ROOT_TITLE = 'Транспортные перевозки'
REPORT_LIST_WINDOW_TITLE = 'Отчеты'
TABLE_LIST_WINDOW_TITLE = 'Таблицы'
VIEW_LIST_WINDOW_TITLE = 'Представления'
VIEW_TITLE = 'Работа с базой данных'

# Data base settings
CONNECTION_DATA = {'server': "PC", 'port': 1433, 'user': "sa", 'password': "123456789", 'database': "Transportations"}

# Data base table information
TABLE_NAMES_DATABASE = ['Cars', 'Cities', 'Clients', 'Countries', 'Drivers', 'Dues', 'Goods', 'OrderGoodsPair', 'Orders',
               'OrderTripPair', 'Regions', 'Trips']

VIEW_NAMES_DATABASE = ['IndexedViewCities1', 'ViewCars1', 'ViewCities1', 'ViewCitiesCountries1']

TABLE_NAMES_INTERFACE = ['Машины', 'Города', 'Клиенты', 'Страны', 'Водители', 'Пошлины', 'Товары', 'Заказ-Товар',
                         'Заказы', 'Заказ-Рейс', 'Регионы', 'Рейсы']

VIEW_NAMES_INTERFACE = ['Города 1', 'Машины 1', 'Города 2', 'Города и страны']

# Preferencies

# Rights

# Functions
def do_nothing():
    print('Doing nothing...')


