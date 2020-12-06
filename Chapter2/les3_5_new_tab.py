"""

создать новую вкладку
browser.execute_script("window.open('');")

метод window_handles возвращает массив имён всех вкладок,
нумеруются с 0
first_window = browser.window_handles[0]
new_window = browser.window_handles[1]

переключение на новую вкладку
browser.switch_to.window(window_name)
"""

import time
from selenium import webdriver

# Define the URL's we will open and a few other variables
main_url = 'http://www.ya.ru'  # URL A
tab_url = 'http://www.ru'  # URL B

browser = webdriver.Firefox()
# Open main window with URL A
browser.get(main_url)
print("Current Page Title is : %s" %browser.title)

# Open a new window
browser.execute_script("window.open('');")
# Switch to the new window and open URL B
browser.switch_to.window(browser.window_handles[1])
browser.get(tab_url)
time.sleep(3)
# …Do something here
print("Current Page Title is : %s" %browser.title)
# Close the tab with URL B
browser.close()

# Switch back to the first tab with URL A
browser.switch_to.window(browser.window_handles[0])
print("Current Page Title is : %s" %browser.title)
time.sleep(3)
# close browser
browser.close()
