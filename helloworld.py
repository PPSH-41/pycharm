import requests
def getHTMLText(url):
    try:
        kv={'user-agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text[:-500]
    except:
        return "产生异常"

if __name__=="__main__":
    url="https://www.amazon.cn/dp/B0719GSVJB/ref=sr_1_1?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=3T5DP65ZGNQRS&keywords=python%E7%BC%96%E7%A8%8B+%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E5%AE%9E%E8%B7%B5&qid=1580040752&sprefix=python%2Caps%2C174&sr=8-1"
    print(getHTMLText(url))
