from bs4 import BeautifulSoup
import requests
import re

# Q1: find all elements, whose href has http://foundation.datasci.tw/ in example webpage
response_ex = requests.get("https://jimmy15923.github.io/example_page")
soup_ex = BeautifulSoup(response_ex.text, "lxml")
print(soup_ex.find_all("", attrs = {"href":re.compile("http://foundation.datasci.tw/")}))

# Q2:
response_518 = requests.get("https://jimmy15923.github.io/518")
soup_518 = BeautifulSoup(response_518.text, "lxml") 
# print(soup_518) # city information is in <li class="comp_loca">
print(soup_518.find_all("li", attrs = {"class":"comp_loca"}, text = re.compile("新北")))