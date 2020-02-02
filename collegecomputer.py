import bs4
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r=requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[1].string,tds[4].string,tds[7].string])

def printUnivList(ulist,num):
#    tplt =
    print("{:10}\t{:6}\t{:10}".format("排名","名称","分数"))
    for i in range(num):
        u=ulist[i]
        print("{:10}\t{:6}\t{:10}".format(u[1],u[4],u[7]))

def main():
    uinfo = []
    url='http://www.zuihaodaxue.com/BCSR/jisuanjikexueyujishu2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #20 univs
main()