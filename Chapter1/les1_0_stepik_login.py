from selenium import webdriver
import time

link = "https://stepik.org/"


def main(browser, link=link):
    login_email = "login"
    login_password = "password"

    try:
        # log in
        # browser = webdriver.Firefox()
        browser = browser
        browser.get(link)
        time.sleep(5)

        submit_button = browser.find_element_by_css_selector(".navbar__auth")
        submit_button.click()

        s_username = browser.find_element_by_id("id_login_email")
        s_username.send_keys(login_email)

        s_password = browser.find_element_by_id("id_login_password")
        s_password.send_keys(login_password)

        button = browser.find_element_by_css_selector(".sign-form__btn")
        button.click()

        time.sleep(1)

    finally:
        time.sleep(1)
        # закрываем акивное окно/вкладку
        # browser.close()

    return browser


if __name__ == '__main__':
    main()
