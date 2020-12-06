import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "Подтверждаю, что являюсь роботом".
7. Переключить radiobutton "Роботы рулят!".
8. Нажать на кнопку "Отправить".
'''


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# default_browser = webdriver.Firefox()
# default_link = "https://suninjuly.github.io/execute_script.html"
#
#
# def main(browser=default_browser, link=default_link):
def main(browser, link):
    try:
        # get verification code
        browser.get(link)

        # находим значение Х, считаем функцию и вводим в поле
        x = browser.find_element(By.ID, "input_value").text
        browser.find_element(By.ID, "answer").send_keys(calc(x))

        # capcha
        robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
        browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
        robot_checkbox.click()
        robots_rule = browser.find_element(By.ID, "robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
        robots_rule.click()

        # прокручиваем страницу до кнопки
        button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        assert True

        alert = browser.switch_to.alert
        text_alert = alert.text
        answer_value = text_alert[(text_alert.index(': '))+2:]
        time.sleep(1)
        alert.accept()

    finally:
        time.sleep(1)
        # close browser
        # browser.quit()

    return answer_value


# print(main())
