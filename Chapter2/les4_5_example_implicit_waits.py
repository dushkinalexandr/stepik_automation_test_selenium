"""
Тестовый сценарий выглядит так:

1. Открыть страницу http://suninjuly.github.io/wait1.html
2. Нажать на кнопку "Verify"
3. Проверить, что появилась надпись "Verification was successful!"

"""

"""
1.
кнопка появляется с задержкой.
потму тест падает с ошибкой 
selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="verify"]
"""

from selenium import webdriver

browser = webdriver.Firefox()
"""
2.
Неявное ожидание (Implicit wait) - автоматически применяется при вызове каждой следующей команды.
говорим WebDriver искать каждый элемент в течение Х секунд (в примере 5сек)
проверять наличие элемента каждые 500мс
"""
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
browser.quit()
