import time
from selenium import webdriver
from Chapter2 import les1_0_stepik_login
from Chapter2 import les1_0_stepik_answer
from Chapter2 import les3_6_move_to_new_tab


def main():
    link = "http://suninjuly.github.io/redirect_accept.html"
    link_answer = "https://stepik.org/lesson/184253/step/6?unit=158843"
    browser = webdriver.Firefox()

    try:
        # get verification code
        answer_value = les3_6_move_to_new_tab.main(browser, link)

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
