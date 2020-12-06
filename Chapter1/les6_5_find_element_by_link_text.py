from selenium import webdriver
import time
import math

# link_find_text = "http://suninjuly.github.io/find_link_text"


def main(browser, link_find_text):
    try:
        # get verification code
        # browser = webdriver.Firefox()
        browser.get(link_find_text)

        find_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
        new_link = browser.find_element_by_partial_link_text(find_text)
        # new_link.click()

    finally:
        time.sleep(1)
        # close browser
        # browser.quit()

    return new_link

if __name__ == '__main__':
    main()
