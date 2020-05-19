# -*- coding:UTF-8-*-

import requests
import time
import json
from requests.packages import urllib3

# 教师 openID
openId = "oWRkU0cTJcXzfrWgG1XCnNxWZG8E"


headers = {
    "Host": "a.welife001.com",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
    "content-type": "application/json",
    "imprint": openId,
    "Accept-Encoding": "gzip, deflate, br"
}
page = 0
while True:
    urllib3.disable_warnings()
    r = requests.get("https://a.welife001.com/info/getTeacherInfo?openid="+openId+"&type=-1&onlyMe=false&page="+str(page)+"&time=-1&lookAll=true&cls=-1&size=10&teacher_cate=teach_class_list&role_detail_id=undefined&nv=1",headers=headers,verify=False)
    data = r.text
    data = json.loads(data)
    if len(data['result']) == 0:
        break
    print(data['result'])
    page = page + 1




