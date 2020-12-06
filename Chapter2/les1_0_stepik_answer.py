from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

# browser = webdriver.Firefox()
# link_answer = "https://stepik.org/lesson/181384/step/8?unit=156009"
# answer_value = "28.984156776975"


def main(browser, link_answer, answer_value):
    browser.implicitly_wait(5)

    try:

        # перход на страницу ввода ответа
        browser.get(link_answer)

        # проверка, доступно ли поле ввода ответа
        # если не доступно, то нажать кнопку "Решить снова"

        # if WebDriverWait(browser, 5).until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, ".again-btn"))):
        #     button_again = browser.find_element(By.CSS_SELECTOR, ".again-btn")
        #     button_again.click()
        # else:
        #     pass

        #  ввести ответ в поле textarea
        browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer_value)

        #  нажать кнопку submit
        browser.find_element(By.CLASS_NAME, "submit-submission").click()

        # correct - если появилась зеоёная голочка
        if WebDriverWait(browser, 15).until_not(EC.visibility_of_element_located((By.ID, "correct"))):
            print("Correct answer.")
        else:
            print("Uncorrect answer.")

    finally:
        time.sleep(1)
        # close browser
        # browser.close()
        # print("Close browser.")

    return browser


if __name__ == '__main__':
    main()
