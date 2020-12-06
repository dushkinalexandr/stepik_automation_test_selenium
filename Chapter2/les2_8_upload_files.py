import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
1. Открыть страницу http://suninjuly.github.io/file_input.html
2. Заполнить текстовые поля: имя, фамилия, email
3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4. Нажать кнопку "Submit"
5. Отправьте полученное число в качестве ответа для этого задания.
"""

# browser_default = webdriver.Firefox()
# link_default = "https://suninjuly.github.io/file_input.html"
#
#
# def main(browser=browser_default, link=link_default):
def main(browser, link):
    try:
        browser.get(link)

        first_name = "first_name"
        last_name = "last_name"
        email = "email@email.edu"

        # заполняем поля
        browser.find_element(By.NAME, "firstname").send_keys(first_name)
        browser.find_element(By.NAME, "lastname").send_keys(last_name)
        browser.find_element(By.NAME, "email").send_keys(email)

        # получаем путь к файлу
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_name = "les2_7_upload_file_example.txt"
        file_path = os.path.join(current_dir, file_name)
        # проверка, если файла не существует, то создать
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass

        # отправляем файл
        browser.find_element(By.ID, "file").send_keys(file_path)

        # жмём кнопку
        browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        # получаем ответ из alert
        alert = browser.switch_to.alert
        text_alert = alert.text
        answer_value = text_alert[(text_alert.index(': ')) + 2:]
        time.sleep(1)
        alert.accept()

    finally:
        time.sleep(1)
        # browser.quit()

    return answer_value


# print(main())
