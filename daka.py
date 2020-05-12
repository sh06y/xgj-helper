# -*- coding:UTF-8 -*-
import time
import json
import requests

# 设定打卡时间 h:m:s
time = ""

postHeaders = {
    "Host": "a.welife001.com",
    "Connection": "keep-alive",
    "Content-Length": "256",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type": "application/json",
    "imprint": "oWRkU0WLmoPWWQvrIJxthLKQ70Y8",
    "Referer": "https://servicewechat.com/wx23d8d7ea22039466/378/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br"
}

postData = json.dumps({
    "feedback_text": "正常",
    "id": "5eb88a62049ea7552c388f10",
    "daka_day": "",
    "files": [],
    "file_type": "any",
    "form_id": "e82320aa0a964c0ea37da2d5436618b5",
    "submit_type": "submit",
    "networkType": "wifi",
    "member_id": "5eb7fd2cdced4b07522c0637",
    "examdetail": "",
    "op": "add"
})