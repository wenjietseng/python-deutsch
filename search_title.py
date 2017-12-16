from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.ard.de/home/ard/ARD_Startseite/21920/index.html")
bsObj = BeautifulSoup(html, "lxml")

titleList = bsObj.findAll("div", {"class":"teaser"})
print(titleList)
