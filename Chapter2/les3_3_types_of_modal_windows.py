import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Chapter2 import les1_0_stepik_login


def main():
    link_answer = "https://stepik.org/lesson/184253/step/3?thread=solutions&unit=158843"
    browser = webdriver.Firefox()

    try:
        # log in
        les1_0_stepik_login.main(browser)
        time.sleep(1)

        # старница задания
        browser.get(link_answer)

        # тип: метод
        types_windows = {
            "alert": ["accept"],
            "confirm": ["accept", "dismiss"],
            "prompt": ["accept", "dismiss", "send_keys"]
        }
        # ожидаем загрузки старницы
        time.sleep(5)

        # получаем заголовки колонок
        table_header = browser.find_elements(By.CSS_SELECTOR, ".table-quiz__table > tr > th")
        # print(table_header)
        # print(type(table_header))
        # print(len(table_header))
        header_num = {}
        for i in range(len(table_header) - 1):
            header_num[i + 1] = table_header[i + 1].text
        # print("header_num:", header_num)

        # получаем заголовки строк
        table_row = browser.find_elements(By.CSS_SELECTOR, ".table-quiz__table > tbody > tr")
        # print(table_row)
        # print(type(table_row))
        # print(len(table_row))
        row_num = {}
        for i in range(len(table_row)):
            row_num[i + 1] = table_row[i].text
        # print("row_num:", row_num)

        # header_num: {1: 'accept', 2: 'dismiss', 3: 'send_keys'}
        # row_num: {1: 'alert', 2: 'confirm', 3: 'prompt'}

        for j, k in row_num.items():
            for z, x in header_num.items():
                if x in types_windows[k]:
                    pattern = f'.table-quiz__table > tbody > tr:nth-child({j}) > td:nth-child({z+1}) .s-checkbox__circle'
                    browser.find_element(By.CSS_SELECTOR, pattern).click()
                else:
                    pass

        time.sleep(5)

        # click on submit button
        submit_button = browser.find_element(By.CLASS_NAME, "submit-submission")
        submit_button.click()
        time.sleep(1)

    except Exception as error:
        print(f'Произошла ошибка, вот её трэйсбэк: {error}')

    finally:
        time.sleep(1)
        # close browser
        print("Mission complete.")
        browser.quit()


if __name__ == '__main__':
    main()
