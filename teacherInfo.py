# -*- coding:UTF-8-*-

import requests
import time
import json
from requests.packages import urllib3

# 教师 openID
openId = "oWRkU0YIgbfbnKwNIWqCN3tJ571A"

def getTeacherInfo(openId):
    headers = {
        "Host": "a.welife001.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "content-type": "application/json",
        "imprint": openId,
        "Accept-Encoding": "gzip, deflate, br"
    }

    # f = open('data.txt','a+',encoding='utf-8')
    page = 0
    datas = []
    while True:
        urllib3.disable_warnings()
        r = requests.get("https://a.welife001.com/info/getTeacherInfo?openid="+openId+"&type=-1&onlyMe=false&page="+str(page)+"&time=-1&lookAll=true&cls=-1&size=10&teacher_cate=teach_class_list&role_detail_id=undefined&nv=1",headers=headers,verify=False)
        data = r.text
        data = json.loads(data)
        if len(data['result']) == 0:
            break
        # f.write(str(data))
        datas.append(data)
        page = page + 1

    # f.close()
    return datas


if __name__ == "__main__":
    with open('data.txt','w',encoding='utf-8') as f:
        f.write(getTeacherInfo(openId))