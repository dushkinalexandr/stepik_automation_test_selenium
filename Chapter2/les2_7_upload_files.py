#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# получаем путь к директории текущего исполняемого файла.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# добавляем к этому пути имя файла.txt
file_path = os.path.join(current_dir, 'les2_7_upload_file_example.txt')
# указывая директорию, в конце должен быть /
file_path1 = os.path.join("//Chapter2/", 'les2_7_upload_file_example.txt')

# upload file
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
# Элемент в форме, который выглядит, как кнопка добавления файла, имеет атрибут type="file".
# Мы должны сначала найти этот элемент с помощью селектора, а затем применить к нему метод send_keys(file_path)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
# element.send_keys("/home/ku/Python/stepik/stepik_automation_test/Chapter2/les2_7_upload_file_example.txt")


# полный путь к файлу.py, включая имя файла
print(os.path.abspath(__file__))

# путь к каталогу
print(os.path.abspath(os.path.dirname(__file__)))

# путь к каталогу
print(os.path.dirname(__file__))

# путь к upload_файлу.txt
print(file_path)

"""
методы модуля os:
https://docs.python.org/3/library/os.path.html


Для работы с путями в python присмотритесь к pathlib:
https://docs.python.org/3/library/os.path.html
https://docs.python.org/3/library/pathlib.html
https://habr.com/ru/post/453862/
https://python-scripts.com/pathlib
"""

"""
-------------------
Предложение:
https://stepik.org/lesson/228249/step/7?discussion=3191171&unit=200781
-------------------
@Юлия Лях, читаю комменты и понимаю, что довольно много людей не сразу понимают что это за конструктор такой. Есть предложение внести дополнение, немного разжевать.
Надеюсь будет полезно.

Для загрузки файла на веб-страницу, используем метод send_keys("путь к файлу")
Три способа задать путь к файлу:

1. вбить руками
element.send_keys("/home/user/stepik/Chapter2/file_example.txt")


2. задать с помощью переменных
# указывая директорию,где лежит файлу.txt
# в конце должен быть /
directory = "/home/user/stepik/Chapter2/"

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# собираем путь к файлу
file_path = os.path.join(directory, file_name)
# отправляем файл
element.send_keys(file_path)

3.путь автоматизатора.
если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге
# импортируем модуль
import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
current_dir = os.path.abspath(os.path.dirname(__file__))

# имя файла, который будем загружать на сайт
file_name = "file_example.txt"

# получаем путь к file_example.txt
file_path = os.path.join(current_dir, file_name)
# отправляем файл
element.send_keys(file_path)

итоговый код:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
"""


"""
-------------------
os.getcwd()
-------------------
в данном случае разницы никакой. Но попробуйте запустить модуль с этими командами из другой дирректории.
Например, у Вас есть структура:


Project
  |--sources
      |--dir
          |--task.py
А в файле task.py следующий код:


import os

print(os.getcwd())
print(os.path.abspath(os.path.dirname(__file__)))
А теперь попробуйте запустить этот скрипт двумя способами 


path/to/Project: & python sources/dir/task.py
и 
path/to/Project/sources/dir: & python task.py
Результаты будут разными
"""