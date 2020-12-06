import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
1. Открыть страницу http://suninjuly.github.io/alert_accept.html
2. Нажать на кнопку
3. Принять confirm
4. На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро 
(в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. 
5. Отправьте полученное число в качестве ответа на это задание.
"""



def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# browser_default = webdriver.Firefox()
# link_default = "http://suninjuly.github.io/alert_accept.html"
# def main(browser=browser_default, link=link_default):
def main(browser, link):
    try:
        browser.get(link)

        # жмём кнопку
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        time.sleep(1)
        # получаем alert
        alert = browser.switch_to.alert
        alert.accept()
        time.sleep(1)

        # считаем функцию и вводим в поле
        x = browser.find_element(By.ID, "input_value").text
        browser.find_element(By.ID, "answer").send_keys(calc(x))

        # жмём кнопку
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        # получаем ответ из alert
        alert = browser.switch_to.alert
        text_alert = alert.text
        answer_value = text_alert[(text_alert.index(': ')) + 2:]
        time.sleep(1)
        alert.accept()

    finally:
        time.sleep(1)
        # browser.quit()

    return answer_value


# print(main())
