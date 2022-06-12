import eel
import requests
import orjson
import json
eel.init('a.html')


headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
@eel.expose
def get_link(str):
    return "http://apihot.gsdata.cn/news/index/spread-number?search="+str

session = requests.Session()
session.post("https://u2.gsdata.cn/member/login", headers = headers, data = {"username": 19974727415, "password": 123456, "remember": 1})
request = session.get(get_link("枪击"), headers = headers)
result = request.json()
#print(result)
re_json=json.dumps(result["data"]["data"][0]["data"]["index"],ensure_ascii=False)
print(re_json)

with open('new_json_hot.json', 'w', encoding='utf-8') as f:
    f.write(re_json)
