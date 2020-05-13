import requests
from requests.packages import urllib3

openId = ""

headers = {
    "Host": "a.welife001.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type": "application/json",
    "imprint": openId,
    "Referer": "https://servicewechat.com/wx23d8d7ea22039466/378/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
    
}

urllib3.disable_warnings()
r = requests.get("https://a.welife001.com/getUser",headers=headers,verify=False)

print(r.text)