from selenium import webdriver
import time

browser = webdriver.Firefox()
try:

    link = 'http://ya.ru'
    browser.get(link)
    time.sleep(2)
    browser.execute_script("prompt('Hello!');")
    prompt = browser.switch_to.alert
    time.sleep(2)
    prompt.send_keys("OKI DOKI lolololadasdasdasd")
    time.sleep(2)
    prompt.accept()

finally:
    time.sleep(2)
    browser.quit()
