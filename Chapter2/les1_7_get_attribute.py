import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# default_browser = webdriver.Firefox()
# default_link = "https://suninjuly.github.io/get_attribute.html"


def main(browser, link):
# def main(browser=default_browser, link=default_link):
    try:
        # get verification code
        browser.get(link)

        x = browser.find_element(By.ID, "treasure").get_attribute("valuex")

        browser.find_element(By.ID, "answer").send_keys(calc(x))

        checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
        checkbox_robot.click()

        radio_robot = browser.find_element(By.ID, "robotsRule")
        radio_robot.click()

        button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        button.click()

        # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
        # for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
        #     browser.find_element_by_css_selector(selector).click()

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
