from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def main(browser, link):
    try:
        # get verification code
        browser.get(link)

        first_name = "first_name"
        last_name = "last_name"
        city = "city"
        country = "country"

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys(first_name)
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys(last_name)
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys(city)
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys(country)
        button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
        button.click()

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

if __name__ == '__main__':
    main()
