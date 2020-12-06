from selenium import webdriver
from selenium.webdriver.common.by import By
import time


'''
идеальный селектор находит один элемент
хороший тест проверяет только маленькую, атомарную часть функциональности
'''


'''
Задание:
заполнить только поля со * (обязательные)
Не совсем корректно было сформулировано изначальное задание, но как есть :)

Используется браузер Firefox, webdriver.Firefox

Подставляя нужную ссылку (переменные есть в коде) можно проверить задание:
browser.get(link2)
'''

try:
    # ссылки заданий
    link1 = "http://suninjuly.github.io/registration1.html"  # les6_10
    link2 = "http://suninjuly.github.io/registration2.html"  # les6_11

    browser = webdriver.Firefox()
    browser.get(link2)

    # значения для заполнения полей
    first_name = "first_name"
    last_name = "last_name"
    email = "email@email.edu"

    # код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys(first_name)
    browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys(last_name)
    browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys(email)
    time.sleep(1)

    # Отправляем заполненную форму
    browser.find_element_by_css_selector("button.btn").click()

    # ждем загрузки страницы
    time.sleep(1)

    # Проверяем, что смогли зарегистрироваться
    # находим элемент, содержащий текст
    welcome_text = browser.find_element_by_tag_name("h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    # выполнится assert True, либо assert False
    assert "Congratulations! You have successfully registered!" == welcome_text
    print("Congratulations! You have successfully registered!")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер/процесс после всех манипуляций
    browser.quit()
