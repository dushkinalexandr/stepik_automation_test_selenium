import time
from selenium import webdriver
from Chapter2 import les1_0_stepik_login
from Chapter2 import les1_0_stepik_answer
from Chapter2 import les1_7_get_attribute


def main():
    link = "http://suninjuly.github.io/get_attribute.html"
    link_answer = "https://stepik.org/lesson/165493/step/7?unit=140087"
    browser = webdriver.Firefox()

    try:
        # get verification code
        answer_value = les1_7_get_attribute.main(browser, link)

        # log in
        les1_0_stepik_login.main(browser)
        time.sleep(1)

        # send answer
        les1_0_stepik_answer.main(browser, link_answer, answer_value)
        time.sleep(1)

    finally:
        time.sleep(1)
        # close browser
        browser.quit()

if __name__ == '__main__':
    main()
