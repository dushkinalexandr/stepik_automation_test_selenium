from selenium import webdriver
import time
from Chapter1 import les1_0_stepik_login
from Chapter1 import les1_0_stepik_answer
from Chapter1 import les6_4_get_verify_code


def main():
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    link_answer = "https://stepik.org/lesson/138920/step/4?unit=196194"
    browser = webdriver.Firefox()

    try:
        # get verification code
        browser, answer_value = les6_4_get_verify_code.main(browser, link)

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
