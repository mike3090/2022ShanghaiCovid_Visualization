import eel
import requests
import orjson
import json
import flask
import pandas as pd

app = flask.Flask(__name__)
@app.after_request
def cors(environ):
    environ.headers['Access-Control-Allow-Origin']='*'
    environ.headers['Access-Control-Allow-Method']='*'
    environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
    return environ


headers = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

def get_link(str):
    return "http://apihot.gsdata.cn/news/index/spread-number?search="+str

@app.route('/clawer_hot', methods=['POST'])
def a():
    dat = flask.request.get_data()
    dat = json.loads(dat)
    dat = dat["district"]
    session = requests.Session()
    session.post("https://u2.gsdata.cn/member/login", headers = headers, data = {"username": 19974727415, "password": 123456, "remember": 1})
    request = session.get(get_link(dat), headers = headers)
    result = request.json()
    #print(result)
    print(result)
    re_json=json.dumps(result["data"]["data"][0]["data"]["index"],ensure_ascii=False)

    return re_json

def main():
    print("aaaa")
    return a()

if __name__ == '__main__':
    app.run(port=8700)