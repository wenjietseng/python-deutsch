from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html, "lxml")
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.ard.de/home/ard/ARD_Startseite/21920/index.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
