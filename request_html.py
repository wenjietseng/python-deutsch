from urllib.request import urlopen
from bs4 import BeautifulSoup

# handle url connection error
try:
    html = urlopen("http://www.ard.de/home/ard/ARD_Startseite/21920/index.html")
    if html is None:
        print("URL is not found")
except HTTPError as e:
    print(e)
    # return NULL, jump out, do some plan B
else:
    pass
    # continue your code, if you have return or break in except part
    # not need to do else

bsObj = BeautifulSoup(html, "lxml")
# check bs4 labeling
try:
    # replace nonExistingTag into the label in bs4
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent == None:
        print("Tag was not found")
    else:
        print(badContent)


print(bsObj.h1)

