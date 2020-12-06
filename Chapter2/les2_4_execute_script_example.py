from selenium import webdriver

browser = webdriver.Firefox()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
# button = browser.find_element_by_tag_name("button")
# button.click()
# assert True

"""
Для клика в WebDriver мы используем метод click(). 
Если элемент оказывается перекрыт другим элементом, то наша программа вызовет следующую ошибку:

selenium.common.exceptions.WebDriverException: 
Message: unknown error: 
Element <button type="submit" class="btn btn-default" style="margin-bottom: 1000px;">...</button> is not clickable at point (87, 420). Other element would receive the click: <p>...</p>

Из описания ошибки можно понять, что указанный нами элемент нельзя кликнуть в данной точке, 
т.к. клик произойдёт на другом элементе с тегом <p>.
"""

"""
как работает метод click()

1. WebDriver проверит, что ширина и высота элемента больше 0, чтобы по нему можно было кликнуть;

2. если элемент находится за границей окна браузера, WebDriver автоматически проскроллит страницу, 
чтобы элемент попал в область видимости, то есть не находился за границей экрана. 
Но это не гарантирует того, что элемент не перекрыт другим элементом, 
который тоже находится в области видимости

3. Selenium рассчитывает координаты центра элемента и производит клик в вычисленную точку. 
Это тоже приведёт к ошибке, если часть элемента всё-таки видна, 
но элемент перекрыт больше чем на половину своей высоты или ширины.
"""

"""
Спомощью JS-скрипта, можно проскролить страницу:
"return arguments[0].scrollIntoView(true);"

Передаём аргумент True, чтобы элемент оказался в области видимости.

Другие параметры метода:
https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView
"""

# находим элемент
# В метод execute_script мы передали текст js-скрипта и найденный элемент button,
# к которому нужно будет проскроллить страницу.
# После выполнения кода элемент button должен оказаться в верхней части страницы.
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True

# Подробнее о методе:
# https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView

# То же самое на JS
# можно выполнить в console браузера
# // javascript
# button = document.getElementsByTagName("button")[0];
# button.scrollIntoView(true);

# Также можно проскроллить всю страницу целиком на строго заданное количество пикселей.
# Эта команда проскроллит страницу на 100 пикселей вниз:
# browser.execute_script("window.scrollBy(0, 100);")

