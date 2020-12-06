from selenium import webdriver
import time
from Chapter1 import les1_0_stepik_login
from Chapter1 import les1_0_stepik_answer
from Chapter1 import les6_4_get_verify_code
from Chapter1 import les6_5_find_element_by_link_text


def main():
    link_find_text = "http://suninjuly.github.io/find_link_text"
    link_answer = "https://stepik.org/lesson/138920/step/5?unit=196194"
    browser = webdriver.Firefox()

    try:
        # get verification code
        ref = les6_5_find_element_by_link_text.main(browser, link_find_text)
        browser, answer_value = les6_4_get_verify_code.main(browser, link=ref.get_attribute('href'))

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
