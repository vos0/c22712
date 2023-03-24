Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
s = Service('C:\Users\rusta\OneDrive\Рабочий стол\драйвер\chromedriver.exe')
SyntaxError: incomplete input
s = Service('C:/Users/rusta/OneDrive/Рабочий стол/драйвер/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://1whis.pro/bets/prematch/18/117/4406/11187162')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
stavka=soup.find_all('span', class_='odd-coefficient')
print (films[0].text)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print (films[0].text)
NameError: name 'films' is not defined
print (stavka[0].text)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print (stavka[0].text)
IndexError: list index out of range
stavka=soup.find_all('span data-v-490bec7b', class_='odd-coefficient')
print (stavka[0].text)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print (stavka[0].text)
IndexError: list index out of range
print(stavka[0])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print(stavka[0])
IndexError: list index out of range
print(stavka)
[]
stavka=soup.find_all('li data-v-f9d6adfa', class_='odds-item')
print(stavka)
[]
print(stavka.text)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(stavka.text)
  File "C:\Users\rusta\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2308, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
stavki=soup.find_all('span', class_='odd-coefficient')
print(stavki.text)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(stavki.text)
  File "C:\Users\rusta\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2308, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
sstavki = bs.find('span', 'odd-coefficient')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    sstavki = bs.find('span', 'odd-coefficient')
NameError: name 'bs' is not defined. Did you mean: 's'?
stavki=soup.find_all('span', class_='odd-coefficient')
print (stavki[0].text)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print (stavki[0].text)
IndexError: list index out of range
print(stavki.text)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    print(stavki.text)
  File "C:\Users\rusta\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2308, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
browser.get('https://1whis.pro/bets/prematch/18/512/3370/11177828')
browser.get('https://1whis.pro/bets/prematch/18/144/1000/10973252')
html_text = browser.page_source
soup = BeautifulSoup(html_text, 'lxml')
stavki=soup.find_all('span', class_='odd-coefficient')
print(stavki.text)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(stavki.text)
  File "C:\Users\rusta\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2308, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
print(stavki)
[<span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">5.12</span>, <span class="odd-coefficient" data-v-490bec7b="">9.99</span>, <span class="odd-coefficient" data-v-490bec7b="">7.4</span>, <span class="odd-coefficient" data-v-490bec7b="">2.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">1.59</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.15</span>, <span class="odd-coefficient" data-v-490bec7b="">1.31</span>, <span class="odd-coefficient" data-v-490bec7b="">1.6</span>, <span class="odd-coefficient" data-v-490bec7b="">2.02</span>, <span class="odd-coefficient" data-v-490bec7b="">2.69</span>, <span class="odd-coefficient" data-v-490bec7b="">3.58</span>, <span class="odd-coefficient" data-v-490bec7b="">5.49</span>, <span class="odd-coefficient" data-v-490bec7b="">11.17</span>, <span class="odd-coefficient" data-v-490bec7b="">4.83</span>, <span class="odd-coefficient" data-v-490bec7b="">3.15</span>, <span class="odd-coefficient" data-v-490bec7b="">2.2</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">1.41</span>, <span class="odd-coefficient" data-v-490bec7b="">1.25</span>, <span class="odd-coefficient" data-v-490bec7b="">1.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.19</span>, <span class="odd-coefficient" data-v-490bec7b="">1.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.73</span>, <span class="odd-coefficient" data-v-490bec7b="">2.24</span>, <span class="odd-coefficient" data-v-490bec7b="">3.1</span>, <span class="odd-coefficient" data-v-490bec7b="">4.24</span>, <span class="odd-coefficient" data-v-490bec7b="">6.64</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">7.74</span>, <span class="odd-coefficient" data-v-490bec7b="">4.23</span>, <span class="odd-coefficient" data-v-490bec7b="">2.83</span>, <span class="odd-coefficient" data-v-490bec7b="">1.99</span>, <span class="odd-coefficient" data-v-490bec7b="">1.58</span>, <span class="odd-coefficient" data-v-490bec7b="">1.32</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">1.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.66</span>, <span class="odd-coefficient" data-v-490bec7b="">2.24</span>, <span class="odd-coefficient" data-v-490bec7b="">3.11</span>, <span class="odd-coefficient" data-v-490bec7b="">3.17</span>, <span class="odd-coefficient" data-v-490bec7b="">2.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.6</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">2.62</span>, <span class="odd-coefficient" data-v-490bec7b="">5.59</span>, <span class="odd-coefficient" data-v-490bec7b="">9.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.12</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">5.94</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">5.45</span>, <span class="odd-coefficient" data-v-490bec7b="">7.92</span>, <span class="odd-coefficient" data-v-490bec7b="">7.92</span>, <span class="odd-coefficient" data-v-490bec7b="">10.89</span>, <span class="odd-coefficient" data-v-490bec7b="">22.77</span>, <span class="odd-coefficient" data-v-490bec7b="">13.86</span>, <span class="odd-coefficient" data-v-490bec7b="">17.82</span>, <span class="odd-coefficient" data-v-490bec7b="">50.49</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">30.69</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">9.7</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">9.4</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">25.74</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">174.24</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">22.77</span>, <span class="odd-coefficient" data-v-490bec7b="">90.09</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">90.09</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">10.96</span>, <span class="odd-coefficient" data-v-490bec7b="">9.8</span>, <span class="odd-coefficient" data-v-490bec7b="">7.62</span>, <span class="odd-coefficient" data-v-490bec7b="">5</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">8.5</span>, <span class="odd-coefficient" data-v-490bec7b="">14.36</span>, <span class="odd-coefficient" data-v-490bec7b="">4.15</span>, <span class="odd-coefficient" data-v-490bec7b="">9.8</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">7.51</span>, <span class="odd-coefficient" data-v-490bec7b="">29.7</span>, <span class="odd-coefficient" data-v-490bec7b="">3.88</span>, <span class="odd-coefficient" data-v-490bec7b="">13.37</span>, <span class="odd-coefficient" data-v-490bec7b="">1.23</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">7.22</span>, <span class="odd-coefficient" data-v-490bec7b="">37.62</span>, <span class="odd-coefficient" data-v-490bec7b="">3.46</span>, <span class="odd-coefficient" data-v-490bec7b="">26.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.28</span>, <span class="odd-coefficient" data-v-490bec7b="">8.05</span>, <span class="odd-coefficient" data-v-490bec7b="">52.47</span>, <span class="odd-coefficient" data-v-490bec7b="">3.27</span>, <span class="odd-coefficient" data-v-490bec7b="">33.66</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">8.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">3.08</span>, <span class="odd-coefficient" data-v-490bec7b="">3.6</span>, <span class="odd-coefficient" data-v-490bec7b="">2.08</span>, <span class="odd-coefficient" data-v-490bec7b="">2.04</span>, <span class="odd-coefficient" data-v-490bec7b="">3.44</span>, <span class="odd-coefficient" data-v-490bec7b="">6.55</span>, <span class="odd-coefficient" data-v-490bec7b="">15</span>, <span class="odd-coefficient" data-v-490bec7b="">23</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">3.44</span>, <span class="odd-coefficient" data-v-490bec7b="">3.98</span>, <span class="odd-coefficient" data-v-490bec7b="">5.9</span>, <span class="odd-coefficient" data-v-490bec7b="">10</span>, <span class="odd-coefficient" data-v-490bec7b="">17</span>, <span class="odd-coefficient" data-v-490bec7b="">10</span>, <span class="odd-coefficient" data-v-490bec7b="">19.96</span>, <span class="odd-coefficient" data-v-490bec7b="">3.34</span>, <span class="odd-coefficient" data-v-490bec7b="">1.84</span>, <span class="odd-coefficient" data-v-490bec7b="">1.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">19</span>, <span class="odd-coefficient" data-v-490bec7b="">32.29</span>, <span class="odd-coefficient" data-v-490bec7b="">4.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">63.36</span>, <span class="odd-coefficient" data-v-490bec7b="">1.58</span>, <span class="odd-coefficient" data-v-490bec7b="">2.6</span>, <span class="odd-coefficient" data-v-490bec7b="">5.31</span>, <span class="odd-coefficient" data-v-490bec7b="">10.47</span>, <span class="odd-coefficient" data-v-490bec7b="">29.87</span>, <span class="odd-coefficient" data-v-490bec7b="">50.54</span>, <span class="odd-coefficient" data-v-490bec7b="">2.77</span>, <span class="odd-coefficient" data-v-490bec7b="">1.49</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.26</span>, <span class="odd-coefficient" data-v-490bec7b="">1.88</span>, <span class="odd-coefficient" data-v-490bec7b="">2.95</span>, <span class="odd-coefficient" data-v-490bec7b="">5.5</span>, <span class="odd-coefficient" data-v-490bec7b="">4.92</span>, <span class="odd-coefficient" data-v-490bec7b="">3.61</span>, <span class="odd-coefficient" data-v-490bec7b="">3.91</span>, <span class="odd-coefficient" data-v-490bec7b="">5.8</span>, <span class="odd-coefficient" data-v-490bec7b="">9.77</span>, <span class="odd-coefficient" data-v-490bec7b="">3.44</span>, <span class="odd-coefficient" data-v-490bec7b="">1.98</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">6.5</span>, <span class="odd-coefficient" data-v-490bec7b="">2.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.33</span>, <span class="odd-coefficient" data-v-490bec7b="">4.27</span>, <span class="odd-coefficient" data-v-490bec7b="">9.72</span>, <span class="odd-coefficient" data-v-490bec7b="">2.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.38</span>, <span class="odd-coefficient" data-v-490bec7b="">7.4</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">1.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.96</span>, <span class="odd-coefficient" data-v-490bec7b="">10.55</span>, <span class="odd-coefficient" data-v-490bec7b="">3.18</span>, <span class="odd-coefficient" data-v-490bec7b="">3.08</span>, <span class="odd-coefficient" data-v-490bec7b="">2.22</span>, <span class="odd-coefficient" data-v-490bec7b="">2.5</span>, <span class="odd-coefficient" data-v-490bec7b="">1.43</span>, <span class="odd-coefficient" data-v-490bec7b="">7.66</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">3.68</span>, <span class="odd-coefficient" data-v-490bec7b="">1.21</span>, <span class="odd-coefficient" data-v-490bec7b="">3.91</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">6.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">2.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.36</span>, <span class="odd-coefficient" data-v-490bec7b="">10.35</span>, <span class="odd-coefficient" data-v-490bec7b="">2.32</span>, <span class="odd-coefficient" data-v-490bec7b="">1.5</span>, <span class="odd-coefficient" data-v-490bec7b="">13.86</span>, <span class="odd-coefficient" data-v-490bec7b="">8.72</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">6.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">5.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.11</span>, <span class="odd-coefficient" data-v-490bec7b="">11.61</span>, <span class="odd-coefficient" data-v-490bec7b="">5.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.11</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">4.75</span>, <span class="odd-coefficient" data-v-490bec7b="">1.16</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">11.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.9</span>, <span class="odd-coefficient" data-v-490bec7b="">5.59</span>, <span class="odd-coefficient" data-v-490bec7b="">2.65</span>, <span class="odd-coefficient" data-v-490bec7b="">5.77</span>, <span class="odd-coefficient" data-v-490bec7b="">11.6</span>, <span class="odd-coefficient" data-v-490bec7b="">5.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.7</span>, <span class="odd-coefficient" data-v-490bec7b="">1.09</span>, <span class="odd-coefficient" data-v-490bec7b="">1.39</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">8.18</span>, <span class="odd-coefficient" data-v-490bec7b="">56.43</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.54</span>, <span class="odd-coefficient" data-v-490bec7b="">3.37</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">2.38</span>, <span class="odd-coefficient" data-v-490bec7b="">7.03</span>, <span class="odd-coefficient" data-v-490bec7b="">2.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.62</span>, <span class="odd-coefficient" data-v-490bec7b="">1.3</span>, <span class="odd-coefficient" data-v-490bec7b="">2.87</span>, <span class="odd-coefficient" data-v-490bec7b="">5.75</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.59</span>, <span class="odd-coefficient" data-v-490bec7b="">2.03</span>, <span class="odd-coefficient" data-v-490bec7b="">2.43</span>, <span class="odd-coefficient" data-v-490bec7b="">1.41</span>, <span class="odd-coefficient" data-v-490bec7b="">2.41</span>, <span class="odd-coefficient" data-v-490bec7b="">1.42</span>, <span class="odd-coefficient" data-v-490bec7b="">2.44</span>, <span class="odd-coefficient" data-v-490bec7b="">6.93</span>, <span class="odd-coefficient" data-v-490bec7b="">3.46</span>, <span class="odd-coefficient" data-v-490bec7b="">3.33</span>, <span class="odd-coefficient" data-v-490bec7b="">4.26</span>, <span class="odd-coefficient" data-v-490bec7b="">2.54</span>, <span class="odd-coefficient" data-v-490bec7b="">5.54</span>, <span class="odd-coefficient" data-v-490bec7b="">9.7</span>, <span class="odd-coefficient" data-v-490bec7b="">4.89</span>, <span class="odd-coefficient" data-v-490bec7b="">3.68</span>, <span class="odd-coefficient" data-v-490bec7b="">4</span>, <span class="odd-coefficient" data-v-490bec7b="">5.74</span>, <span class="odd-coefficient" data-v-490bec7b="">9.6</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.26</span>, <span class="odd-coefficient" data-v-490bec7b="">2.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.92</span>, <span class="odd-coefficient" data-v-490bec7b="">3.86</span>, <span class="odd-coefficient" data-v-490bec7b="">3.37</span>, <span class="odd-coefficient" data-v-490bec7b="">1.6</span>, <span class="odd-coefficient" data-v-490bec7b="">1.7</span>, <span class="odd-coefficient" data-v-490bec7b="">3.01</span>, <span class="odd-coefficient" data-v-490bec7b="">5.45</span>, <span class="odd-coefficient" data-v-490bec7b="">11.88</span>, <span class="odd-coefficient" data-v-490bec7b="">39.6</span>, <span class="odd-coefficient" data-v-490bec7b="">1.36</span>, <span class="odd-coefficient" data-v-490bec7b="">3.76</span>, <span class="odd-coefficient" data-v-490bec7b="">1.19</span>, <span class="odd-coefficient" data-v-490bec7b="">1.24</span>, <span class="odd-coefficient" data-v-490bec7b="">4.32</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">3.39</span>, <span class="odd-coefficient" data-v-490bec7b="">9.8</span>, <span class="odd-coefficient" data-v-490bec7b="">8.8</span>, <span class="odd-coefficient" data-v-490bec7b="">3.54</span>, <span class="odd-coefficient" data-v-490bec7b="">2.82</span>, <span class="odd-coefficient" data-v-490bec7b="">1.96</span>, <span class="odd-coefficient" data-v-490bec7b="">1.53</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">1.26</span>, <span class="odd-coefficient" data-v-490bec7b="">1.41</span>, <span class="odd-coefficient" data-v-490bec7b="">1.85</span>, <span class="odd-coefficient" data-v-490bec7b="">2.44</span>, <span class="odd-coefficient" data-v-490bec7b="">3.04</span>, <span class="odd-coefficient" data-v-490bec7b="">4.9</span>, <span class="odd-coefficient" data-v-490bec7b="">5.5</span>, <span class="odd-coefficient" data-v-490bec7b="">9.7</span>, <span class="odd-coefficient" data-v-490bec7b="">12</span>, <span class="odd-coefficient" data-v-490bec7b="">19.35</span>, <span class="odd-coefficient" data-v-490bec7b="">28.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.51</span>, <span class="odd-coefficient" data-v-490bec7b="">1.99</span>, <span class="odd-coefficient" data-v-490bec7b="">2.82</span>, <span class="odd-coefficient" data-v-490bec7b="">3.44</span>, <span class="odd-coefficient" data-v-490bec7b="">6</span>, <span class="odd-coefficient" data-v-490bec7b="">6.55</span>, <span class="odd-coefficient" data-v-490bec7b="">14.64</span>, <span class="odd-coefficient" data-v-490bec7b="">15.11</span>, <span class="odd-coefficient" data-v-490bec7b="">7.2</span>, <span class="odd-coefficient" data-v-490bec7b="">2.52</span>, <span class="odd-coefficient" data-v-490bec7b="">1.79</span>, <span class="odd-coefficient" data-v-490bec7b="">1.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.09</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.09</span>, <span class="odd-coefficient" data-v-490bec7b="">1.53</span>, <span class="odd-coefficient" data-v-490bec7b="">1.98</span>, <span class="odd-coefficient" data-v-490bec7b="">2.67</span>, <span class="odd-coefficient" data-v-490bec7b="">5.42</span>, <span class="odd-coefficient" data-v-490bec7b="">11.83</span>, <span class="odd-coefficient" data-v-490bec7b="">6.86</span>, <span class="odd-coefficient" data-v-490bec7b="">2.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.8</span>, <span class="odd-coefficient" data-v-490bec7b="">1.46</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">1.96</span>, <span class="odd-coefficient" data-v-490bec7b="">3.9</span>, <span class="odd-coefficient" data-v-490bec7b="">5.58</span>, <span class="odd-coefficient" data-v-490bec7b="">1.82</span>, <span class="odd-coefficient" data-v-490bec7b="">1.23</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.57</span>, <span class="odd-coefficient" data-v-490bec7b="">2.28</span>, <span class="odd-coefficient" data-v-490bec7b="">3.74</span>, <span class="odd-coefficient" data-v-490bec7b="">7</span>, <span class="odd-coefficient" data-v-490bec7b="">4.3</span>, <span class="odd-coefficient" data-v-490bec7b="">4.8</span>, <span class="odd-coefficient" data-v-490bec7b="">6.91</span>, <span class="odd-coefficient" data-v-490bec7b="">11</span>, <span class="odd-coefficient" data-v-490bec7b="">17</span>, <span class="odd-coefficient" data-v-490bec7b="">9.8</span>, <span class="odd-coefficient" data-v-490bec7b="">3.54</span>, <span class="odd-coefficient" data-v-490bec7b="">2.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">1.1</span>, <span class="odd-coefficient" data-v-490bec7b="">5.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.55</span>, <span class="odd-coefficient" data-v-490bec7b="">3.76</span>, <span class="odd-coefficient" data-v-490bec7b="">1.31</span>, <span class="odd-coefficient" data-v-490bec7b="">1.09</span>, <span class="odd-coefficient" data-v-490bec7b="">2.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.17</span>, <span class="odd-coefficient" data-v-490bec7b="">2.8</span>, <span class="odd-coefficient" data-v-490bec7b="">2.89</span>, <span class="odd-coefficient" data-v-490bec7b="">1.98</span>, <span class="odd-coefficient" data-v-490bec7b="">2</span>, <span class="odd-coefficient" data-v-490bec7b="">1.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.62</span>, <span class="odd-coefficient" data-v-490bec7b="">1.61</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">1.85</span>, <span class="odd-coefficient" data-v-490bec7b="">3.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.45</span>, <span class="odd-coefficient" data-v-490bec7b="">2.94</span>, <span class="odd-coefficient" data-v-490bec7b="">1.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.23</span>, <span class="odd-coefficient" data-v-490bec7b="">2.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.52</span>, <span class="odd-coefficient" data-v-490bec7b="">5.36</span>, <span class="odd-coefficient" data-v-490bec7b="">1.19</span>, <span class="odd-coefficient" data-v-490bec7b="">5.26</span>, <span class="odd-coefficient" data-v-490bec7b="">2.16</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">3.58</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">1.32</span>, <span class="odd-coefficient" data-v-490bec7b="">9.48</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">9.53</span>, <span class="odd-coefficient" data-v-490bec7b="">2.74</span>, <span class="odd-coefficient" data-v-490bec7b="">5.41</span>, <span class="odd-coefficient" data-v-490bec7b="">4.04</span>, <span class="odd-coefficient" data-v-490bec7b="">1.17</span>, <span class="odd-coefficient" data-v-490bec7b="">1.8</span>, <span class="odd-coefficient" data-v-490bec7b="">21.78</span>, <span class="odd-coefficient" data-v-490bec7b="">66.33</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">9.9</span>, <span class="odd-coefficient" data-v-490bec7b="">3.8</span>, <span class="odd-coefficient" data-v-490bec7b="">6.83</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">25.74</span>, <span class="odd-coefficient" data-v-490bec7b="">23.76</span>, <span class="odd-coefficient" data-v-490bec7b="">16.83</span>, <span class="odd-coefficient" data-v-490bec7b="">1.68</span>, <span class="odd-coefficient" data-v-490bec7b="">2.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">4.25</span>, <span class="odd-coefficient" data-v-490bec7b="">2.8</span>, <span class="odd-coefficient" data-v-490bec7b="">1.37</span>, <span class="odd-coefficient" data-v-490bec7b="">1.59</span>, <span class="odd-coefficient" data-v-490bec7b="">2.12</span>, <span class="odd-coefficient" data-v-490bec7b="">13.86</span>, <span class="odd-coefficient" data-v-490bec7b="">5.1</span>, <span class="odd-coefficient" data-v-490bec7b="">2.87</span>, <span class="odd-coefficient" data-v-490bec7b="">6.83</span>, <span class="odd-coefficient" data-v-490bec7b="">3.8</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">55.44</span>, <span class="odd-coefficient" data-v-490bec7b="">12.87</span>, <span class="odd-coefficient" data-v-490bec7b="">24.75</span>, <span class="odd-coefficient" data-v-490bec7b="">2.55</span>, <span class="odd-coefficient" data-v-490bec7b="">5.09</span>, <span class="odd-coefficient" data-v-490bec7b="">3.34</span>, <span class="odd-coefficient" data-v-490bec7b="">4.45</span>, <span class="odd-coefficient" data-v-490bec7b="">2.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.47</span>, <span class="odd-coefficient" data-v-490bec7b="">2.47</span>, <span class="odd-coefficient" data-v-490bec7b="">1.81</span>, <span class="odd-coefficient" data-v-490bec7b="">8.91</span>, <span class="odd-coefficient" data-v-490bec7b="">1.84</span>, <span class="odd-coefficient" data-v-490bec7b="">6.68</span>, <span class="odd-coefficient" data-v-490bec7b="">2.28</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">3.27</span>, <span class="odd-coefficient" data-v-490bec7b="">20.79</span>, <span class="odd-coefficient" data-v-490bec7b="">6.43</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">9.4</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">6.93</span>, <span class="odd-coefficient" data-v-490bec7b="">6.5</span>, <span class="odd-coefficient" data-v-490bec7b="">6.43</span>, <span class="odd-coefficient" data-v-490bec7b="">7.92</span>, <span class="odd-coefficient" data-v-490bec7b="">10.89</span>, <span class="odd-coefficient" data-v-490bec7b="">10.89</span>, <span class="odd-coefficient" data-v-490bec7b="">8.91</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">33.66</span>, <span class="odd-coefficient" data-v-490bec7b="">7.42</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">2.5</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">8.91</span>, <span class="odd-coefficient" data-v-490bec7b="">6</span>, <span class="odd-coefficient" data-v-490bec7b="">9.9</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">6.5</span>, <span class="odd-coefficient" data-v-490bec7b="">6.5</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">6.43</span>, <span class="odd-coefficient" data-v-490bec7b="">4.5</span>, <span class="odd-coefficient" data-v-490bec7b="">2.4</span>, <span class="odd-coefficient" data-v-490bec7b="">7.5</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">20.79</span>, <span class="odd-coefficient" data-v-490bec7b="">22.77</span>, <span class="odd-coefficient" data-v-490bec7b="">9.4</span>, <span class="odd-coefficient" data-v-490bec7b="">28.71</span>, <span class="odd-coefficient" data-v-490bec7b="">7.5</span>, <span class="odd-coefficient" data-v-490bec7b="">25.74</span>, <span class="odd-coefficient" data-v-490bec7b="">11.88</span>, <span class="odd-coefficient" data-v-490bec7b="">6</span>, <span class="odd-coefficient" data-v-490bec7b="">28.71</span>, <span class="odd-coefficient" data-v-490bec7b="">7.92</span>, <span class="odd-coefficient" data-v-490bec7b="">9.4</span>, <span class="odd-coefficient" data-v-490bec7b="">28.71</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">1.47</span>, <span class="odd-coefficient" data-v-490bec7b="">1.09</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">1.16</span>, <span class="odd-coefficient" data-v-490bec7b="">1.51</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.09</span>, <span class="odd-coefficient" data-v-490bec7b="">2.68</span>, <span class="odd-coefficient" data-v-490bec7b="">3.61</span>, <span class="odd-coefficient" data-v-490bec7b="">5.43</span>, <span class="odd-coefficient" data-v-490bec7b="">3.35</span>, <span class="odd-coefficient" data-v-490bec7b="">1.39</span>, <span class="odd-coefficient" data-v-490bec7b="">1.23</span>, <span class="odd-coefficient" data-v-490bec7b="">1.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.26</span>, <span class="odd-coefficient" data-v-490bec7b="">2.69</span>, <span class="odd-coefficient" data-v-490bec7b="">1.37</span>, <span class="odd-coefficient" data-v-490bec7b="">21.78</span>, <span class="odd-coefficient" data-v-490bec7b="">3.46</span>, <span class="odd-coefficient" data-v-490bec7b="">3.72</span>, <span class="odd-coefficient" data-v-490bec7b="">5.84</span>, <span class="odd-coefficient" data-v-490bec7b="">1.94</span>, <span class="odd-coefficient" data-v-490bec7b="">2.6</span>, <span class="odd-coefficient" data-v-490bec7b="">3.66</span>, <span class="odd-coefficient" data-v-490bec7b="">8.91</span>, <span class="odd-coefficient" data-v-490bec7b="">27.72</span>, <span class="odd-coefficient" data-v-490bec7b="">59.4</span>, <span class="odd-coefficient" data-v-490bec7b="">7.06</span>, <span class="odd-coefficient" data-v-490bec7b="">20.79</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.2</span>, <span class="odd-coefficient" data-v-490bec7b="">1.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">1.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">5.35</span>, <span class="odd-coefficient" data-v-490bec7b="">5.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.57</span>, <span class="odd-coefficient" data-v-490bec7b="">3.89</span>, <span class="odd-coefficient" data-v-490bec7b="">8.5</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">297.99</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">50.49</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">60.39</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">347.49</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">9.4</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">70.29</span>, <span class="odd-coefficient" data-v-490bec7b="">50.49</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">33.66</span>, <span class="odd-coefficient" data-v-490bec7b="">16.83</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">8.7</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">297.99</span>, <span class="odd-coefficient" data-v-490bec7b="">297.99</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">396.99</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">396.99</span>, <span class="odd-coefficient" data-v-490bec7b="">297.99</span>, <span class="odd-coefficient" data-v-490bec7b="">50.49</span>, <span class="odd-coefficient" data-v-490bec7b="">396.99</span>, <span class="odd-coefficient" data-v-490bec7b="">60.39</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">396.99</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">28.71</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">70.29</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">297.99</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">396.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">396.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">25.74</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">297.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">198.99</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">248.49</span>, <span class="odd-coefficient" data-v-490bec7b="">70.29</span>, <span class="odd-coefficient" data-v-490bec7b="">24.75</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">297.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">396.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495.99</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">6.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.92</span>, <span class="odd-coefficient" data-v-490bec7b="">1.79</span>, <span class="odd-coefficient" data-v-490bec7b="">4.51</span>, <span class="odd-coefficient" data-v-490bec7b="">2.35</span>, <span class="odd-coefficient" data-v-490bec7b="">1.6</span>, <span class="odd-coefficient" data-v-490bec7b="">1.86</span>, <span class="odd-coefficient" data-v-490bec7b="">3.16</span>, <span class="odd-coefficient" data-v-490bec7b="">3.24</span>, <span class="odd-coefficient" data-v-490bec7b="">4.12</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.48</span>, <span class="odd-coefficient" data-v-490bec7b="">1.92</span>, <span class="odd-coefficient" data-v-490bec7b="">1.68</span>, <span class="odd-coefficient" data-v-490bec7b="">1.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.26</span>, <span class="odd-coefficient" data-v-490bec7b="">1.17</span>, <span class="odd-coefficient" data-v-490bec7b="">1.6</span>, <span class="odd-coefficient" data-v-490bec7b="">2.88</span>, <span class="odd-coefficient" data-v-490bec7b="">5.83</span>, <span class="odd-coefficient" data-v-490bec7b="">2.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">5.35</span>, <span class="odd-coefficient" data-v-490bec7b="">1.12</span>, <span class="odd-coefficient" data-v-490bec7b="">2.48</span>, <span class="odd-coefficient" data-v-490bec7b="">1.48</span>, <span class="odd-coefficient" data-v-490bec7b="">3.37</span>, <span class="odd-coefficient" data-v-490bec7b="">3.69</span>, <span class="odd-coefficient" data-v-490bec7b="">1.21</span>, <span class="odd-coefficient" data-v-490bec7b="">1.22</span>, <span class="odd-coefficient" data-v-490bec7b="">1.81</span>, <span class="odd-coefficient" data-v-490bec7b="">9.25</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">6.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">1.72</span>, <span class="odd-coefficient" data-v-490bec7b="">2.73</span>, <span class="odd-coefficient" data-v-490bec7b="">8.41</span>, <span class="odd-coefficient" data-v-490bec7b="">32.67</span>, <span class="odd-coefficient" data-v-490bec7b="">6.53</span>, <span class="odd-coefficient" data-v-490bec7b="">25.74</span>, <span class="odd-coefficient" data-v-490bec7b="">47.52</span>, <span class="odd-coefficient" data-v-490bec7b="">2.25</span>, <span class="odd-coefficient" data-v-490bec7b="">1.48</span>, <span class="odd-coefficient" data-v-490bec7b="">1.23</span>, <span class="odd-coefficient" data-v-490bec7b="">3.27</span>, <span class="odd-coefficient" data-v-490bec7b="">2.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.4</span>, <span class="odd-coefficient" data-v-490bec7b="">10.08</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">5.29</span>, <span class="odd-coefficient" data-v-490bec7b="">4.22</span>, <span class="odd-coefficient" data-v-490bec7b="">1.23</span>, <span class="odd-coefficient" data-v-490bec7b="">1.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.7</span>, <span class="odd-coefficient" data-v-490bec7b="">2.09</span>, <span class="odd-coefficient" data-v-490bec7b="">2.62</span>, <span class="odd-coefficient" data-v-490bec7b="">3.31</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">3.25</span>, <span class="odd-coefficient" data-v-490bec7b="">2.39</span>, <span class="odd-coefficient" data-v-490bec7b="">1.88</span>, <span class="odd-coefficient" data-v-490bec7b="">1.56</span>, <span class="odd-coefficient" data-v-490bec7b="">1.35</span>, <span class="odd-coefficient" data-v-490bec7b="">1.22</span>, <span class="odd-coefficient" data-v-490bec7b="">4.19</span>, <span class="odd-coefficient" data-v-490bec7b="">4.39</span>, <span class="odd-coefficient" data-v-490bec7b="">1.53</span>, <span class="odd-coefficient" data-v-490bec7b="">8.21</span>, <span class="odd-coefficient" data-v-490bec7b="">7.63</span>, <span class="odd-coefficient" data-v-490bec7b="">4.06</span>, <span class="odd-coefficient" data-v-490bec7b="">3.47</span>, <span class="odd-coefficient" data-v-490bec7b="">2.37</span>, <span class="odd-coefficient" data-v-490bec7b="">1.96</span>, <span class="odd-coefficient" data-v-490bec7b="">1.63</span>, <span class="odd-coefficient" data-v-490bec7b="">1.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.2</span>, <span class="odd-coefficient" data-v-490bec7b="">1.43</span>, <span class="odd-coefficient" data-v-490bec7b="">1.64</span>, <span class="odd-coefficient" data-v-490bec7b="">1.98</span>, <span class="odd-coefficient" data-v-490bec7b="">2.51</span>, <span class="odd-coefficient" data-v-490bec7b="">2.96</span>, <span class="odd-coefficient" data-v-490bec7b="">1.21</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">2.74</span>, <span class="odd-coefficient" data-v-490bec7b="">5.94</span>, <span class="odd-coefficient" data-v-490bec7b="">3.39</span>, <span class="odd-coefficient" data-v-490bec7b="">1.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.32</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.48</span>, <span class="odd-coefficient" data-v-490bec7b="">1.86</span>, <span class="odd-coefficient" data-v-490bec7b="">3.03</span>, <span class="odd-coefficient" data-v-490bec7b="">2</span>, <span class="odd-coefficient" data-v-490bec7b="">1.44</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.37</span>, <span class="odd-coefficient" data-v-490bec7b="">1.79</span>, <span class="odd-coefficient" data-v-490bec7b="">2.73</span>, <span class="odd-coefficient" data-v-490bec7b="">5.55</span>, <span class="odd-coefficient" data-v-490bec7b="">6.79</span>, <span class="odd-coefficient" data-v-490bec7b="">12.78</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">3.07</span>, <span class="odd-coefficient" data-v-490bec7b="">4.34</span>, <span class="odd-coefficient" data-v-490bec7b="">10.09</span>, <span class="odd-coefficient" data-v-490bec7b="">11.05</span>, <span class="odd-coefficient" data-v-490bec7b="">5.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.56</span>, <span class="odd-coefficient" data-v-490bec7b="">2.42</span>, <span class="odd-coefficient" data-v-490bec7b="">3.7</span>, <span class="odd-coefficient" data-v-490bec7b="">9</span>, <span class="odd-coefficient" data-v-490bec7b="">11</span>, <span class="odd-coefficient" data-v-490bec7b="">2.33</span>, <span class="odd-coefficient" data-v-490bec7b="">1.52</span>, <span class="odd-coefficient" data-v-490bec7b="">1.25</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">3.4</span>, <span class="odd-coefficient" data-v-490bec7b="">13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">5.67</span>, <span class="odd-coefficient" data-v-490bec7b="">3.03</span>, <span class="odd-coefficient" data-v-490bec7b="">7.53</span>, <span class="odd-coefficient" data-v-490bec7b="">11.77</span>, <span class="odd-coefficient" data-v-490bec7b="">2.28</span>, <span class="odd-coefficient" data-v-490bec7b="">6.19</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.47</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">6.97</span>, <span class="odd-coefficient" data-v-490bec7b="">1.9</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.68</span>, <span class="odd-coefficient" data-v-490bec7b="">6.52</span>, <span class="odd-coefficient" data-v-490bec7b="">1.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">3.68</span>, <span class="odd-coefficient" data-v-490bec7b="">2.46</span>, <span class="odd-coefficient" data-v-490bec7b="">2.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.74</span>, <span class="odd-coefficient" data-v-490bec7b="">1.94</span>, <span class="odd-coefficient" data-v-490bec7b="">3.01</span>, <span class="odd-coefficient" data-v-490bec7b="">4.16</span>, <span class="odd-coefficient" data-v-490bec7b="">8.91</span>, <span class="odd-coefficient" data-v-490bec7b="">1.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.22</span>, <span class="odd-coefficient" data-v-490bec7b="">1.63</span>, <span class="odd-coefficient" data-v-490bec7b="">2.87</span>, <span class="odd-coefficient" data-v-490bec7b="">2.08</span>, <span class="odd-coefficient" data-v-490bec7b="">1.39</span>, <span class="odd-coefficient" data-v-490bec7b="">2.7</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">1.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">6.73</span>, <span class="odd-coefficient" data-v-490bec7b="">2.51</span>, <span class="odd-coefficient" data-v-490bec7b="">7.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.24</span>, <span class="odd-coefficient" data-v-490bec7b="">4.3</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">20.79</span>, <span class="odd-coefficient" data-v-490bec7b="">40.59</span>, <span class="odd-coefficient" data-v-490bec7b="">7.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">9.7</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">2.11</span>, <span class="odd-coefficient" data-v-490bec7b="">3.96</span>, <span class="odd-coefficient" data-v-490bec7b="">2.77</span>, <span class="odd-coefficient" data-v-490bec7b="">1.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.3</span>, <span class="odd-coefficient" data-v-490bec7b="">1.19</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.22</span>, <span class="odd-coefficient" data-v-490bec7b="">1.41</span>, <span class="odd-coefficient" data-v-490bec7b="">2.04</span>, <span class="odd-coefficient" data-v-490bec7b="">3.31</span>, <span class="odd-coefficient" data-v-490bec7b="">4.31</span>, <span class="odd-coefficient" data-v-490bec7b="">7.4</span>, <span class="odd-coefficient" data-v-490bec7b="">8.74</span>, <span class="odd-coefficient" data-v-490bec7b="">1.12</span>, <span class="odd-coefficient" data-v-490bec7b="">2.32</span>, <span class="odd-coefficient" data-v-490bec7b="">3.24</span>, <span class="odd-coefficient" data-v-490bec7b="">6.79</span>, <span class="odd-coefficient" data-v-490bec7b="">7.78</span>, <span class="odd-coefficient" data-v-490bec7b="">5.29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.54</span>, <span class="odd-coefficient" data-v-490bec7b="">1.3</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.81</span>, <span class="odd-coefficient" data-v-490bec7b="">2.74</span>, <span class="odd-coefficient" data-v-490bec7b="">5.45</span>, <span class="odd-coefficient" data-v-490bec7b="">6.9</span>, <span class="odd-coefficient" data-v-490bec7b="">2.9</span>, <span class="odd-coefficient" data-v-490bec7b="">1.94</span>, <span class="odd-coefficient" data-v-490bec7b="">1.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.08</span>, <span class="odd-coefficient" data-v-490bec7b="">2.9</span>, <span class="odd-coefficient" data-v-490bec7b="">9.41</span>, <span class="odd-coefficient" data-v-490bec7b="">12.75</span>, <span class="odd-coefficient" data-v-490bec7b="">1.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.54</span>, <span class="odd-coefficient" data-v-490bec7b="">5.23</span>, <span class="odd-coefficient" data-v-490bec7b="">4.03</span>, <span class="odd-coefficient" data-v-490bec7b="">3.16</span>, <span class="odd-coefficient" data-v-490bec7b="">2.61</span>, <span class="odd-coefficient" data-v-490bec7b="">1.87</span>, <span class="odd-coefficient" data-v-490bec7b="">2.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.25</span>, <span class="odd-coefficient" data-v-490bec7b="">1.36</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">1.57</span>, <span class="odd-coefficient" data-v-490bec7b="">2.12</span>, <span class="odd-coefficient" data-v-490bec7b="">4.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">4.22</span>, <span class="odd-coefficient" data-v-490bec7b="">1.54</span>, <span class="odd-coefficient" data-v-490bec7b="">1.12</span>, <span class="odd-coefficient" data-v-490bec7b="">2.89</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.72</span>, <span class="odd-coefficient" data-v-490bec7b="">8.83</span>, <span class="odd-coefficient" data-v-490bec7b="">1.12</span>, <span class="odd-coefficient" data-v-490bec7b="">8.18</span>, <span class="odd-coefficient" data-v-490bec7b="">1.85</span>, <span class="odd-coefficient" data-v-490bec7b="">4.4</span>, <span class="odd-coefficient" data-v-490bec7b="">3.32</span>, <span class="odd-coefficient" data-v-490bec7b="">8.3</span>, <span class="odd-coefficient" data-v-490bec7b="">19</span>, <span class="odd-coefficient" data-v-490bec7b="">28.49</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">2.91</span>, <span class="odd-coefficient" data-v-490bec7b="">5.05</span>, <span class="odd-coefficient" data-v-490bec7b="">11</span>, <span class="odd-coefficient" data-v-490bec7b="">20.63</span>, <span class="odd-coefficient" data-v-490bec7b="">8.5</span>, <span class="odd-coefficient" data-v-490bec7b="">2.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.31</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">23</span>, <span class="odd-coefficient" data-v-490bec7b="">13.1</span>, <span class="odd-coefficient" data-v-490bec7b="">3.63</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">1.56</span>, <span class="odd-coefficient" data-v-490bec7b="">2.22</span>, <span class="odd-coefficient" data-v-490bec7b="">3.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.25</span>, <span class="odd-coefficient" data-v-490bec7b="">2.6</span>, <span class="odd-coefficient" data-v-490bec7b="">1.36</span>, <span class="odd-coefficient" data-v-490bec7b="">2.96</span>, <span class="odd-coefficient" data-v-490bec7b="">2.51</span>, <span class="odd-coefficient" data-v-490bec7b="">4.16</span>, <span class="odd-coefficient" data-v-490bec7b="">2.71</span>, <span class="odd-coefficient" data-v-490bec7b="">7.42</span>, <span class="odd-coefficient" data-v-490bec7b="">7.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">4</span>, <span class="odd-coefficient" data-v-490bec7b="">3.54</span>, <span class="odd-coefficient" data-v-490bec7b="">6.43</span>, <span class="odd-coefficient" data-v-490bec7b="">1.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.53</span>, <span class="odd-coefficient" data-v-490bec7b="">2.3</span>, <span class="odd-coefficient" data-v-490bec7b="">2.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.53</span>, <span class="odd-coefficient" data-v-490bec7b="">2.04</span>, <span class="odd-coefficient" data-v-490bec7b="">10.89</span>, <span class="odd-coefficient" data-v-490bec7b="">1.17</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">4.36</span>, <span class="odd-coefficient" data-v-490bec7b="">2.75</span>, <span class="odd-coefficient" data-v-490bec7b="">3.19</span>, <span class="odd-coefficient" data-v-490bec7b="">1.24</span>, <span class="odd-coefficient" data-v-490bec7b="">1.1</span>, <span class="odd-coefficient" data-v-490bec7b="">15.95</span>, <span class="odd-coefficient" data-v-490bec7b="">6.62</span>, <span class="odd-coefficient" data-v-490bec7b="">1.78</span>, <span class="odd-coefficient" data-v-490bec7b="">1.61</span>, <span class="odd-coefficient" data-v-490bec7b="">1.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.22</span>, <span class="odd-coefficient" data-v-490bec7b="">1.12</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">5.94</span>, <span class="odd-coefficient" data-v-490bec7b="">4.04</span>, <span class="odd-coefficient" data-v-490bec7b="">2.54</span>, <span class="odd-coefficient" data-v-490bec7b="">2.32</span>, <span class="odd-coefficient" data-v-490bec7b="">1.98</span>, <span class="odd-coefficient" data-v-490bec7b="">1.79</span>, <span class="odd-coefficient" data-v-490bec7b="">2.01</span>, <span class="odd-coefficient" data-v-490bec7b="">2.32</span>, <span class="odd-coefficient" data-v-490bec7b="">2.54</span>, <span class="odd-coefficient" data-v-490bec7b="">3.31</span>, <span class="odd-coefficient" data-v-490bec7b="">4.37</span>, <span class="odd-coefficient" data-v-490bec7b="">5.75</span>, <span class="odd-coefficient" data-v-490bec7b="">7.74</span>, <span class="odd-coefficient" data-v-490bec7b="">9.45</span>, <span class="odd-coefficient" data-v-490bec7b="">11.77</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.15</span>, <span class="odd-coefficient" data-v-490bec7b="">1.38</span>, <span class="odd-coefficient" data-v-490bec7b="">1.45</span>, <span class="odd-coefficient" data-v-490bec7b="">1.62</span>, <span class="odd-coefficient" data-v-490bec7b="">1.21</span>, <span class="odd-coefficient" data-v-490bec7b="">1.65</span>, <span class="odd-coefficient" data-v-490bec7b="">2.44</span>, <span class="odd-coefficient" data-v-490bec7b="">3.71</span>, <span class="odd-coefficient" data-v-490bec7b="">5.69</span>, <span class="odd-coefficient" data-v-490bec7b="">8.5</span>, <span class="odd-coefficient" data-v-490bec7b="">9.38</span>, <span class="odd-coefficient" data-v-490bec7b="">3.39</span>, <span class="odd-coefficient" data-v-490bec7b="">1.95</span>, <span class="odd-coefficient" data-v-490bec7b="">1.41</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">1.06</span>, <span class="odd-coefficient" data-v-490bec7b="">2.31</span>, <span class="odd-coefficient" data-v-490bec7b="">1.16</span>, <span class="odd-coefficient" data-v-490bec7b="">1.17</span>, <span class="odd-coefficient" data-v-490bec7b="">1.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.27</span>, <span class="odd-coefficient" data-v-490bec7b="">1.79</span>, <span class="odd-coefficient" data-v-490bec7b="">2.62</span>, <span class="odd-coefficient" data-v-490bec7b="">3.39</span>, <span class="odd-coefficient" data-v-490bec7b="">8.03</span>, <span class="odd-coefficient" data-v-490bec7b="">4.08</span>, <span class="odd-coefficient" data-v-490bec7b="">2.98</span>, <span class="odd-coefficient" data-v-490bec7b="">1.79</span>, <span class="odd-coefficient" data-v-490bec7b="">1.35</span>, <span class="odd-coefficient" data-v-490bec7b="">1.21</span>, <span class="odd-coefficient" data-v-490bec7b="">1.81</span>, <span class="odd-coefficient" data-v-490bec7b="">2.42</span>, <span class="odd-coefficient" data-v-490bec7b="">8.2</span>, <span class="odd-coefficient" data-v-490bec7b="">5.7</span>, <span class="odd-coefficient" data-v-490bec7b="">1.13</span>, <span class="odd-coefficient" data-v-490bec7b="">1.5</span>, <span class="odd-coefficient" data-v-490bec7b="">2.25</span>, <span class="odd-coefficient" data-v-490bec7b="">3.44</span>, <span class="odd-coefficient" data-v-490bec7b="">5.98</span>, <span class="odd-coefficient" data-v-490bec7b="">2.48</span>, <span class="odd-coefficient" data-v-490bec7b="">1.6</span>, <span class="odd-coefficient" data-v-490bec7b="">1.28</span>, <span class="odd-coefficient" data-v-490bec7b="">1.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.49</span>, <span class="odd-coefficient" data-v-490bec7b="">2.17</span>, <span class="odd-coefficient" data-v-490bec7b="">3.72</span>, <span class="odd-coefficient" data-v-490bec7b="">6.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.1</span>, <span class="odd-coefficient" data-v-490bec7b="">6.12</span>, <span class="odd-coefficient" data-v-490bec7b="">2.52</span>, <span class="odd-coefficient" data-v-490bec7b="">1.64</span>, <span class="odd-coefficient" data-v-490bec7b="">1.25</span>, <span class="odd-coefficient" data-v-490bec7b="">1.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.8</span>, <span class="odd-coefficient" data-v-490bec7b="">3.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.94</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">3.07</span>, <span class="odd-coefficient" data-v-490bec7b="">6.43</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">18.81</span>, <span class="odd-coefficient" data-v-490bec7b="">40.59</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">70.29</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">3.01</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">8.41</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">55.44</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">8.91</span>, <span class="odd-coefficient" data-v-490bec7b="">40.59</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">99.99</span>, <span class="odd-coefficient" data-v-490bec7b="">40.59</span>, <span class="odd-coefficient" data-v-490bec7b="">90.09</span>, <span class="odd-coefficient" data-v-490bec7b="">90.09</span>, <span class="odd-coefficient" data-v-490bec7b="">2.89</span>, <span class="odd-coefficient" data-v-490bec7b="">3.42</span>, <span class="odd-coefficient" data-v-490bec7b="">1.55</span>, <span class="odd-coefficient" data-v-490bec7b="">2.68</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.21</span>, <span class="odd-coefficient" data-v-490bec7b="">2.11</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">2.11</span>, <span class="odd-coefficient" data-v-490bec7b="">6.27</span>, <span class="odd-coefficient" data-v-490bec7b="">1.17</span>, <span class="odd-coefficient" data-v-490bec7b="">6.1</span>, <span class="odd-coefficient" data-v-490bec7b="">1.55</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">3.76</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.81</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.76</span>, <span class="odd-coefficient" data-v-490bec7b="">5.34</span>, <span class="odd-coefficient" data-v-490bec7b="">4.5</span>, <span class="odd-coefficient" data-v-490bec7b="">12</span>, <span class="odd-coefficient" data-v-490bec7b="">26</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">2.83</span>, <span class="odd-coefficient" data-v-490bec7b="">6.15</span>, <span class="odd-coefficient" data-v-490bec7b="">13</span>, <span class="odd-coefficient" data-v-490bec7b="">8.5</span>, <span class="odd-coefficient" data-v-490bec7b="">1.88</span>, <span class="odd-coefficient" data-v-490bec7b="">1.19</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.71</span>, <span class="odd-coefficient" data-v-490bec7b="">5.67</span>, <span class="odd-coefficient" data-v-490bec7b="">3.03</span>, <span class="odd-coefficient" data-v-490bec7b="">9.5</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">2.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.33</span>, <span class="odd-coefficient" data-v-490bec7b="">7.73</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">2.34</span>, <span class="odd-coefficient" data-v-490bec7b="">1.49</span>, <span class="odd-coefficient" data-v-490bec7b="">2.34</span>, <span class="odd-coefficient" data-v-490bec7b="">1.49</span>, <span class="odd-coefficient" data-v-490bec7b="">2.05</span>, <span class="odd-coefficient" data-v-490bec7b="">1.68</span>, <span class="odd-coefficient" data-v-490bec7b="">2.37</span>, <span class="odd-coefficient" data-v-490bec7b="">2.45</span>, <span class="odd-coefficient" data-v-490bec7b="">4.95</span>, <span class="odd-coefficient" data-v-490bec7b="">3.66</span>, <span class="odd-coefficient" data-v-490bec7b="">10.89</span>, <span class="odd-coefficient" data-v-490bec7b="">3.03</span>, <span class="odd-coefficient" data-v-490bec7b="">1.27</span>, <span class="odd-coefficient" data-v-490bec7b="">3.27</span>, <span class="odd-coefficient" data-v-490bec7b="">1.23</span>, <span class="odd-coefficient" data-v-490bec7b="">1.62</span>, <span class="odd-coefficient" data-v-490bec7b="">2.91</span>, <span class="odd-coefficient" data-v-490bec7b="">7.9</span>, <span class="odd-coefficient" data-v-490bec7b="">4.07</span>, <span class="odd-coefficient" data-v-490bec7b="">1.2</span>, <span class="odd-coefficient" data-v-490bec7b="">1.29</span>, <span class="odd-coefficient" data-v-490bec7b="">1.73</span>, <span class="odd-coefficient" data-v-490bec7b="">2.43</span>, <span class="odd-coefficient" data-v-490bec7b="">3.77</span>, <span class="odd-coefficient" data-v-490bec7b="">3.37</span>, <span class="odd-coefficient" data-v-490bec7b="">2.03</span>, <span class="odd-coefficient" data-v-490bec7b="">1.52</span>, <span class="odd-coefficient" data-v-490bec7b="">1.24</span>, <span class="odd-coefficient" data-v-490bec7b="">1.39</span>, <span class="odd-coefficient" data-v-490bec7b="">1.87</span>, <span class="odd-coefficient" data-v-490bec7b="">2.83</span>, <span class="odd-coefficient" data-v-490bec7b="">4.37</span>, <span class="odd-coefficient" data-v-490bec7b="">2.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.4</span>, <span class="odd-coefficient" data-v-490bec7b="">1.19</span>, <span class="odd-coefficient" data-v-490bec7b="">1.5</span>, <span class="odd-coefficient" data-v-490bec7b="">2.26</span>, <span class="odd-coefficient" data-v-490bec7b="">2.47</span>, <span class="odd-coefficient" data-v-490bec7b="">1.59</span>, <span class="odd-coefficient" data-v-490bec7b="">4.49</span>, <span class="odd-coefficient" data-v-490bec7b="">1.18</span>, <span class="odd-coefficient" data-v-490bec7b="">3.27</span>, <span class="odd-coefficient" data-v-490bec7b="">5.74</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">12.87</span>, <span class="odd-coefficient" data-v-490bec7b="">33.66</span>, <span class="odd-coefficient" data-v-490bec7b="">70.29</span>, <span class="odd-coefficient" data-v-490bec7b="">35.64</span>, <span class="odd-coefficient" data-v-490bec7b="">60.39</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">66.33</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">4</span>, <span class="odd-coefficient" data-v-490bec7b="">90.09</span>, <span class="odd-coefficient" data-v-490bec7b="">8.41</span>, <span class="odd-coefficient" data-v-490bec7b="">90.09</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">45.54</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">495</span>, <span class="odd-coefficient" data-v-490bec7b="">9.9</span>, <span class="odd-coefficient" data-v-490bec7b="">40.59</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">90.09</span>, <span class="odd-coefficient" data-v-490bec7b="">35.64</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">80.19</span>, <span class="odd-coefficient" data-v-490bec7b="">7.82</span>, <span class="odd-coefficient" data-v-490bec7b="">11.14</span>, <span class="odd-coefficient" data-v-490bec7b="">2.85</span>, <span class="odd-coefficient" data-v-490bec7b="">5.36</span>, <span class="odd-coefficient" data-v-490bec7b="">1.01</span>, <span class="odd-coefficient" data-v-490bec7b="">1.3</span>, <span class="odd-coefficient" data-v-490bec7b="">1.07</span>, <span class="odd-coefficient" data-v-490bec7b="">7.07</span>, <span class="odd-coefficient" data-v-490bec7b="">2.22</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.5</span>, <span class="odd-coefficient" data-v-490bec7b="">6.34</span>, <span class="odd-coefficient" data-v-490bec7b="">2.14</span>, <span class="odd-coefficient" data-v-490bec7b="">1.04</span>, <span class="odd-coefficient" data-v-490bec7b="">1.53</span>, <span class="odd-coefficient" data-v-490bec7b="">2.72</span>, <span class="odd-coefficient" data-v-490bec7b="">2.52</span>, <span class="odd-coefficient" data-v-490bec7b="">2.97</span>, <span class="odd-coefficient" data-v-490bec7b="">1.55</span>, <span class="odd-coefficient" data-v-490bec7b="">5.13</span>, <span class="odd-coefficient" data-v-490bec7b="">4.02</span>, <span class="odd-coefficient" data-v-490bec7b="">1.87</span>, <span class="odd-coefficient" data-v-490bec7b="">1.83</span>, <span class="odd-coefficient" data-v-490bec7b="">6.83</span>, <span class="odd-coefficient" data-v-490bec7b="">1.03</span>, <span class="odd-coefficient" data-v-490bec7b="">9.24</span>, <span class="odd-coefficient" data-v-490bec7b="">1.34</span>, <span class="odd-coefficient" data-v-490bec7b="">3.68</span>, <span class="odd-coefficient" data-v-490bec7b="">14.85</span>, <span class="odd-coefficient" data-v-490bec7b="">13.37</span>, <span class="odd-coefficient" data-v-490bec7b="">35.64</span>, <span class="odd-coefficient" data-v-490bec7b="">8.09</span>, <span class="odd-coefficient" data-v-490bec7b="">1.02</span>, <span class="odd-coefficient" data-v-490bec7b="">3.78</span>, <span class="odd-coefficient" data-v-490bec7b="">1.2</span>, <span class="odd-coefficient" data-v-490bec7b="">6.89</span>, <span class="odd-coefficient" data-v-490bec7b="">1.05</span>, <span class="odd-coefficient" data-v-490bec7b="">2.8</span>, <span class="odd-coefficient" data-v-490bec7b="">1.35</span>, <span class="odd-coefficient" data-v-490bec7b="">2.8</span>, <span class="odd-coefficient" data-v-490bec7b="">1.35</span>]
print(stavki.text)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(stavki.text)
  File "C:\Users\rusta\AppData\Local\Programs\Python\Python311\Lib\site-packages\bs4\element.py", line 2308, in __getattr__
    raise AttributeError(
AttributeError: ResultSet object has no attribute 'text'. You're probably treating a list of elements like a single element. Did you call find_all() when you meant to call find()?
print(stavki[0].text)
1.34
for i in (0, 735):
print(stavki[i].text)
SyntaxError: expected an indented block after 'for' statement on line 1
for i in (0, 735):
    print(stavki[i].text)

1.34
1.12
a = 0
while a <= 735:
...     a += 1
...     print(stavki[i].text)
... 
...     
1.12
1.12
1.12
1.12
1.12
1.12
1.12
1.12
1.12
1.12
1.12
Traceback (most recent call last):
  File "<pyshell#45>", line 3, in <module>
    print(stavki[i].text)
KeyboardInterrupt
>>> while a <= 735:
...     a += 1
...     print(stavki[a].text)
... 
...     
2.69
3.58
5.49
11.17
4.83
3.15
2.2
1.71
1.41
1.25
1.11
1.19
1.38
1.73
2.24
3.1
4.24
6.64
1.05
7.74
4.23
2.83
1.99
1.58
1.32
1.18
1.08
1.33
1.66
2.24
3.11
3.17
2.14
1.6
1.34
2.62
5.59
9.28
1.45
1.12
1.04
5.94
198.99
198.99
495
495
495
495
495
495
495
495
5.45
7.92
7.92
10.89
22.77
13.86
17.82
50.49
198.99
30.69
45.54
99.99
198.99
198.99
80.19
99.99
198.99
198.99
198.99
198.99
198.99
198.99
198.99
198.99
198.99
495
495
198.99
198.99
198.99
198.99
495
495
495
495
198.99
198.99
198.99
495
495
495
495
495
495
14.85
9.7
198.99
198.99
198.99
198.99
198.99
9.4
198.99
198.99
198.99
198.99
198.99
495
25.74
198.99
198.99
198.99
198.99
198.99
495
99.99
198.99
198.99
198.99
198.99
495
495
198.99
198.99
198.99
198.99
495
495
495
198.99
198.99
495
495
495
495
495
495
495
495
495
495
495
495
495
495
495
495
495
495
18.81
45.54
174.24
198.99
198.99
22.77
90.09
198.99
198.99
90.09
198.99
198.99
10.96
9.8
7.62
5
1.06
1.14
8.5
14.36
4.15
9.8
1.18
1.04
7.51
29.7
3.88
13.37
1.23
1.01
7.22
37.62
3.46
26.73
1.01
1.28
8.05
52.47
3.27
33.66
1.02
1.29
8.14
1.02
3.08
3.6
2.08
2.04
3.44
6.55
15
23
1.03
3.44
3.98
5.9
10
17
10
19.96
3.34
1.84
1.28
1.05
1.01
19
32.29
4.33
1.18
63.36
1.58
2.6
5.31
10.47
29.87
50.54
2.77
1.49
1.13
1.26
1.88
2.95
5.5
4.92
3.61
3.91
5.8
9.77
3.44
1.98
1.34
6.5
2.73
1.73
1.33
4.27
9.72
2.73
1.38
7.4
1.04
1.73
1.96
10.55
3.18
3.08
2.22
2.5
1.43
7.66
1.03
3.68
1.21
3.91
1.18
6.07
1.07
2.73
1.36
10.35
2.32
1.5
13.86
8.72
1.01
6.02
1.07
5.06
1.11
11.61
5.06
1.11
18.81
4.75
1.16
45.54
11.38
1.01
1.11
1.9
5.59
2.65
5.77
11.6
5.1
1.7
1.09
1.39
1.08
8.18
56.43
1.02
1.54
3.37
1.29
2.38
7.03
2.11
1.62
1.3
2.87
5.75
1.06
1.59
2.03
2.43
1.41
2.41
1.42
2.44
6.93
3.46
3.33
4.26
2.54
5.54
9.7
4.89
3.68
4
5.74
9.6
1.14
1.26
2.13
1.92
3.86
3.37
1.6
1.7
3.01
5.45
11.88
39.6
1.36
3.76
1.19
1.24
4.32
1.13
1.06
1.18
3.39
9.8
8.8
3.54
2.82
1.96
1.53
1.34
1.13
1.1
1.01
1.03
1.01
1.03
1.26
1.41
1.85
2.44
3.04
4.9
5.5
9.7
12
19.35
28.33
1.07
1.51
1.99
2.82
3.44
6
6.55
14.64
15.11
7.2
2.52
1.79
1.42
1.28
1.09
1.06
1.01
1.01
1.09
1.53
1.98
2.67
5.42
11.83
6.86
2.45
1.8
1.46
1.14
1.03
1.96
3.9
5.58
1.82
1.23
1.14
1.33
1.57
2.28
3.74
7
4.3
4.8
6.91
11
17
9.8
3.54
2.01
1.34
1.1
5.02
1.55
3.76
1.31
1.09
2.11
1.17
2.8
2.89
1.98
2
1.87
1.29
1.62
1.61
1.71
1.85
3.28
1.45
2.94
1.73
1.23
2.33
1.28
1.52
5.36
1.19
5.26
2.16
1.07
3.58
1.08
1.32
9.48
1.07
9.53
2.74
5.41
4.04
1.17
1.8
21.78
66.33
14.85
9.9
3.8
6.83
18.81
25.74
23.76
16.83
1.68
2.02
1.18
4.25
2.8
1.37
1.59
2.12
13.86
5.1
2.87
6.83
3.8
18.81
55.44
12.87
24.75
2.55
5.09
3.34
4.45
2.45
1.47
2.47
1.81
8.91
1.84
6.68
2.28
14.85
3.27
20.79
6.43
18.81
14.85
9.4
18.81
6.93
6.5
6.43
7.92
10.89
10.89
8.91
14.85
33.66
7.42
18.81
14.85
2.5
18.81
8.91
6
9.9
14.85
6.5
6.5
18.81
6.43
4.5
2.4
7.5
18.81
20.79
22.77
9.4
28.71
7.5
25.74
11.88
6
28.71
7.92
9.4
28.71
18.81
1.08
1.47
1.09
1.08
1.08
1.16
1.51
1.06
1.06
1.09
2.68
3.61
5.43
3.35
1.39
1.23
1.1
1.26
2.69
1.37
21.78
3.46
3.72
5.84
1.94
2.6
3.66
8.91
27.72
59.4
7.06
20.79
99.99
1.29
1.2
1.11
1.71
1.45
1.01
1.04
5.35
5.06
1.57
3.89
8.5
198.99
14.85
297.99
45.54
248.49
198.99
80.19
248.49
50.49
45.54
45.54
60.39
99.99
99.99
99.99
198.99
347.49
80.19
248.49
198.99
9.4
248.49
70.29
50.49
99.99
198.99
33.66
16.83
248.49
45.54
14.85
8.7
99.99
248.49
297.99
297.99
80.19
396.99
18.81
396.99
297.99
50.49
396.99
60.39
80.19
396.99
248.49
28.71
495.99
70.29
495.99
248.49
495.99
495.99
495.99
495.99
297.99
248.49
248.49
396.99
495.99
495.99
396.99
495.99
495.99
248.49
495.99
495.99
25.74
495.99
495.99
297.99
495.99
495.99
198.99
80.19
495.99
248.49
70.29
24.75
495.99
495.99
495.99
495.99
495.99
495.99
99.99
495.99
495.99
297.99
495.99
396.99
495.99
495.99
495.99
1.02
1.03
6.14
1.07
1.92
1.79
4.51
2.35
1.6
1.86
3.16
3.24
4.12
1.14
1.48
1.92
1.68
1.28
1.26
1.17
1.6
2.88
5.83
2.1
1.33
1.08
5.35
1.12
2.48
