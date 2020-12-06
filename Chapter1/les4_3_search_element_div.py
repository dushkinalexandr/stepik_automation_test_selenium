import requests
from bs4 import BeautifulSoup


print(len(BeautifulSoup(requests.get('http://suninjuly.github.io/blog_example.html').text, 'html.parser').find_all('div')))
