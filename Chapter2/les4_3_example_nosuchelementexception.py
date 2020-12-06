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

import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get("http://suninjuly.github.io/wait1.html")

"""
2.
если добивать time.sleep(1), то ошибки уже не будет
но задержка может меняться в коде, зависит от машин и от скорости интернета.
потому это плохой способ ожидания загрузки станиц
"""
time.sleep(1)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
browser.quit()

