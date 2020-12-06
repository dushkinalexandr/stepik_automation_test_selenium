"""
Explicit Waits (WebDriverWait и expected_conditions)

Явное ожидание (Explicit Waits) - позволяет задать специальное ожидание для конкретного элемента.
Например:
кнопка находится на странице, но заблокирована.
ождаем когда кнопка стане кликабельной.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

"""
поиск элементов с помощью класса By
element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае.

в объекте WebDriverWait используется функция until, в которую передается правило ожидания, элемент, 
а также значение, по которому мы будем искать элемент. 

В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания:
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions
https://selenium-python.readthedocs.io/waits.html
https://habr.com/ru/post/273089/
https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

Примеры правил:
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
"""

"""
Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное правило с помощью метода until_not:
"""
# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
