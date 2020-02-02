import requests
from bs4 import BeautifulSoup
import re
r=requests.get("https://python123.io/ws/demo.html")
demo=r.text
soup = BeautifulSoup(demo,"html.parser")
soup.prettify()
# print(soup.find_all(['a','b']))
# for tag in soup.find_all(re.compile('b')):
for tag in soup.find_all(String='Python'):
    print(tag.name)