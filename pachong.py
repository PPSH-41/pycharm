import requests
keyword = 'Python'
try:
    kv={'wd':'keyword'}
    r=requests.get("https://www.baidu.com/s",headers='Mozilla/5.0',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
