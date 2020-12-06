"""
1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3. Нажать на кнопку "Book"
4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100,
используйте метод text_to_be_present_in_element из библиотеки expected_conditions.

5. Если все сделано правильно и быстро, то вы увидите окно с числом. Отправьте его в качестве ответа на это задание.

"""
import math, time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from Chapter2 import les1_0_stepik_login
from Chapter2 import les1_0_stepik_answer


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


def wait_text(browser, link):
    browser.get(link)

    # говорим Selenium проверять в течение 15 секунд, пока цена не станет равна 100$
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    # жмём заразервировать
    browser.find_element(By.ID, "book").click()

    # получаем значение и считаем функцию
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(int(x)))
    browser.find_element(By.ID, "solve").click()

    # из алерта получаем ответ
    alert = browser.switch_to.alert
    text_alert = alert.text
    answer = text_alert[(text_alert.index(': ')) + 2:]
    alert.accept()

    return answer


link = "https://suninjuly.github.io/explicit_wait2.html"
link_answer = "https://stepik.org/lesson/181384/step/8?unit=156009"
browser = webdriver.Firefox()
browser.implicitly_wait(5)

try:
    # get verification code
    answer_value = wait_text(browser, link)
    print("Answer -", answer_value)

    # log in
    les1_0_stepik_login.main(browser)

    # send answer
    les1_0_stepik_answer.main(browser, link_answer, answer_value)

finally:
    time.sleep(1)
    # close browser
    print("Close browser.")
    browser.quit()
