# -*- coding:UTF-8-*-

# 代码对应的 URL: /notify/check4teacher

import time
import json
import requests
from requests.packages import urllib3

openId = "oWRkU0XpatFnNVvmqDqnYQmmKERk"

"""
对应关系

tid = notify 下的 _id
cid = cls
"""
tid = ""
cid = ""


ts = int(round(time.time() * 1000))

post = json.dumps({
    "_id":tid,
    "cid":cid,
    "daka_day":"",
    "teacher_cate":"teach_class_list",
    "member_id":"",
    "cls_ts":ts})

headers = {
    "Host": "a.welife001.com",
    "Connection": "keep-alive",
    "Content-Length": "153",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type": "application/json",
    "imprint": openId,
    "Referer": "https://servicewechat.com/wx23d8d7ea22039466/378/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
}

urllib3.disable_warnings()
r = requests.post("https://a.welife001.com/notify/check4teacher",headers=headers,data=post,verify=False)
print(r.text)