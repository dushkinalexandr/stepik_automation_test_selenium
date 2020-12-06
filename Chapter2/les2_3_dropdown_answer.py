import time
from selenium import webdriver
from Chapter2 import les1_0_stepik_login
from Chapter2 import les1_0_stepik_answer
from Chapter2 import les2_3_dropdown


def main():
    link1 = "http://suninjuly.github.io/selects1.html"
    link2 = "http://suninjuly.github.io/selects2.html"
    link_answer = "https://stepik.org/lesson/228249/step/3?unit=200781"
    browser = webdriver.Firefox()

    try:
        # get verification code
        answer_value = les2_3_dropdown.main(browser, link1)

        # log in
        les1_0_stepik_login.main(browser)
        time.sleep(1)

        # send answer
        les1_0_stepik_answer.main(browser, link_answer, answer_value)
        time.sleep(1)

    except Exception as error:
        print(f'Произошла ошибка, вот её трэйсбэк: {error}')

    finally:
        time.sleep(1)
        # close browser
        browser.quit()

if __name__ == '__main__':
    main()
