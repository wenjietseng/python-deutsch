import requests
from bs4 import BeautifulSoup
import re


response = requests.get("https://jimmy15923.github.io/518")
soup = BeautifulSoup(response.text, "lxml")

all_phone_text = [tag.text for tag in soup.find_all("li", {"class":"comp_tel"})]
all_phone_text = "".join(all_phone_text)

print(all_phone_text)
phone_number = re.findall("0[1-9]-[0-9]+", all_phone_text)

print(phone_number)


# exec
# os.getwd
# os.chdir