import time
from selenium import webdriver
from Chapter1 import les1_0_stepik_login
from Chapter1 import les1_0_stepik_answer
from Chapter1 import les6_7_huge_form


def main():
    link_huge_form = "http://suninjuly.github.io/huge_form.html"
    link_answer = "https://stepik.org/lesson/138920/step/7?unit=196194"

    try:
        # get verification code
        browser = webdriver.Firefox()
        answer_value = les6_7_huge_form.main(browser, link_huge_form)

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
