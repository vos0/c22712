# установи python, pip

# выполни эту команду: pip install selenium bs4 lxml
# если ты используешь pycharm, то надо библиотеки ставить не в консоли(терминале), а в самом pycharm
# для этого нажми "view" > "tool windows" > "python packages"
# внизу в окне поиска ищи нужные библиотеки
# когда найдешь, нажимай на нее, справа будет кнопка "install package", устанавливай, потом перезапусти pycharm

# найди версию своего браузера
# напиши в гугле "скачать драйвер для <название и версия твоего браузера> selenium" 
# теперь все готово для запуска этого
# помните, что сам сайт(который вы хотите парсить) может вас блокировать или заставлять проходить capture, из-за чего этот код ничего не выведет

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# импортируем всё нужное

s = Service("путь_до_драйвера") # в ковычках указываем полный путь до скаченного ранее драйвера
# если ты на винде, то вместо знака "\" пиши "\\"

brow = webdriver.Chrome(service=s) # как будто создаем виртуальный браузер

brow.get("https://www.revshells.com/") # получаем html код сайта и другую информацию(она нам не нужна сейчас)

html = brow.page_source # копируем html код в переменную

soup = BeautifulSoup(html, "lxml") # создаем специальный парсер

buttons = soup.find_all(attrs={"class": "list-group-item list-group-item-action"})
# получаем список всех html тегов, в которых есть атрибут "class", равный: "list-group-item list-group-item-action"

for button in buttons:
    # выводим текст каждого тега
    print(button.text)

# от сердца и почек
# дарю вам питончик
# made by perfecto

