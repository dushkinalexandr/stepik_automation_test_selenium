import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
Задание:
сопоставьте типы модальных окон в браузере с методами WebDriver для взаимодействия с ним.
"""


def main():
    link_login = "https://stepik.org/"
    login_email = "login"
    login_password = "password"

    link_answer = "https://stepik.org/lesson/184253/step/3?thread=solutions&unit=158843"
    browser = webdriver.Firefox()

    try:
        # log in
        browser.get(link_login)
        time.sleep(5)

        # жмём кнопку "Войти"
        browser.find_element(By.CSS_SELECTOR, ".navbar__auth").click()

        # вводим login/password
        browser.find_element(By.ID, "id_login_email").send_keys(login_email)
        browser.find_element(By.ID, "id_login_password").send_keys(login_password)
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
        time.sleep(1)

        # страница задания
        browser.get(link_answer)

        # тип: метод
        types_windows = {
            "alert":    ["accept"],
            "confirm":  ["accept", "dismiss"],
            "prompt":   ["accept", "dismiss", "send_keys"]
        }
        # ожидаем загрузки страницы
        time.sleep(5)

        # получаем заголовки колонок
        table_header = browser.find_elements(By.CSS_SELECTOR, ".table-quiz__table > tr > th")
        header_num = {}
        for i in range(len(table_header) - 1):
            header_num[i + 1] = table_header[i + 1].text

        # получаем заголовки строк
        table_row = browser.find_elements(By.CSS_SELECTOR, ".table-quiz__table > tbody > tr")
        row_num = {}
        for i in range(len(table_row)):
            row_num[i + 1] = table_row[i].text

        # header_num: {1: 'accept', 2: 'dismiss', 3: 'send_keys'}
        # row_num: {1: 'alert', 2: 'confirm', 3: 'prompt'}

        # проходим по строкам и выставляем нужные чекбоксы
        for j, k in row_num.items():
            for z, x in header_num.items():
                if x in types_windows[k]:
                    pattern = f'.table-quiz__table > tbody > tr:nth-child({j}) > td:nth-child({z+1}) .s-checkbox__circle'
                    browser.find_element(By.CSS_SELECTOR, pattern).click()
                else:
                    pass

        # ожидаем завершение процедуры
        time.sleep(5)

        # click on submit button
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(1)

    # ловим ошибки на всякий случай
    except Exception as error:
        print(f'Произошла ошибка, вот её трэйсбэк: {error}')

    finally:
        time.sleep(1)
        print("Mission complete.")

        # close browser
        browser.quit()


if __name__ == '__main__':
    main()
