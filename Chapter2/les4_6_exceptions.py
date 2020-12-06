"""
Exceptions

Во время поиска WebDriver каждые 0.5 секунды проверяет, появился ли нужный элемент в DOM-модели браузера
(Document Object Model — «объектная модель документа», интерфейс для доступа к HTML-содержимому сайта).
Если произойдет ошибка, то WebDriver выбросит одно из следующих исключений (exceptions):

1. NoSuchElementException
Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.


2. StaleElementReferenceException
Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился,
то получим StaleElementReferenceException.
Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click.
Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно —
элемент "устарел" (stale) и мы увидим исключение.

3. ElementNotVisibleException
Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),
и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.
"""

"""
Задание:

Какую ошибку вы увидите в консоли,
если попытаетесь выполнить команду browser.find_element_by_id("button")
после открытия страницы http://suninjuly.github.io/cats.html?

NoSuchElementsException

MoveTargetOutOfBoundsException

NoSuchElementException

ElementNotVisibleException
"""