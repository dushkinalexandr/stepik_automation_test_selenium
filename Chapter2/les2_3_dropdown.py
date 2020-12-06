import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# default_browser = webdriver.Firefox()
# default_link1 = "https://suninjuly.github.io/selects1.html"
# default_link2 = "https://suninjuly.github.io/selects2.html"


def main(browser, link):
# def main(browser=default_browser, link=default_link2):
    try:
        browser.get(link)

        num1 = browser.find_element(By.ID, "num1").text
        num2 = browser.find_element(By.ID, "num2").text
        sum_x = str(int(num1) + int(num2))

        select = Select(browser.find_element(By.TAG_NAME, "select"))
        select.select_by_value(sum_x)

        button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
        button.click()

        # get verification code
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
