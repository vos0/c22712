from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service("chromedriver")
brow = webdriver.Chrome(service=s)

brow.get("https://www.revshells.com/")
html = brow.page_source

soup = BS(html, "lxml")

buttons = soup.find_all(attrs={"class": "list-group-item list-group-item-action"})
name = soup.find_all(attrs={"class": "rainbow"})

print(f"name: {name.text}")

for button in buttons:
    print(button.text)

