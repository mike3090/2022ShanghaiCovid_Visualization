import requests
import orjson
import json
headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

def get_link(date):
    return "http://apihot.gsdata.cn/news/index/hot-list?type=2&news_type=4&date=2022-05-"+date+"&province=上海市&perpage=1000&page=1&news_emotion="


session = requests.Session()
session.post("https://u2.gsdata.cn/member/login", headers = headers, data = {"username": 19974727415, "password": 123456, "remember": 1})
for i in range(13):
    if i<10:
        request = session.get(get_link('0'+str(i)), headers = headers)
    else:
        request = session.get(get_link(str(i)), headers = headers)
    result = request.json()
    re_json=json.dumps(result["data"]["list"],ensure_ascii=False)
    if i<10:
        with open('2022-05-'+'0'+str(i)+'.json', 'w', encoding='utf-8') as f:
            f.write(re_json)
    else:
        with open('2022-05-'+str(i)+'.json', 'w', encoding='utf-8') as f:
            f.write(re_json)