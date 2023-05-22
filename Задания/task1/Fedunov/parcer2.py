from bs4 import BeautifulSoup as BS
import requests

url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
response = requests.get(url)
BS = BeautifulSoup(response.text,"lxml")
temp = BS.find('span', 'temp__value temp__value_with-unit')

print(temp.text)