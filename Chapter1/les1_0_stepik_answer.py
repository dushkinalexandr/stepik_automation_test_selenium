from selenium import webdriver
import time


def main(browser, link_answer, answer_value):
    # link_answer = "https://stepik.org/lesson/138920/step/4?unit=196194"

    try:
        # browser = webdriver.Firefox()

        # input verification code in textarea
        browser.get(link_answer)
        time.sleep(2)

        textarea = browser.find_element_by_css_selector(".textarea")
        textarea.send_keys(answer_value)
        time.sleep(1)

        submit_button = browser.find_element_by_css_selector(".submit-submission")
        submit_button.click()
        time.sleep(1)

    finally:
        time.sleep(1)
        # close browser
        # browser.close()

    return browser

if __name__ == '__main__':
    main()
