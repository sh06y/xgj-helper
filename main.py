# -*- coding:UTF-8-*-
from teacherDetail import getTeacherDetail
from teacherInfo import getTeacherInfo
from userInfo import getUserInfo
import json
import demjson

# openId = input("请输入教师openId（任意一个）:")
openId = "oWRkU0YIgbfbnKwNIWqCN3tJ571A"
print('''
1.获取作业内容
2.
''')

# n = input("你想做什么：")
n = "1"

if n == "1":
    teacherInfo = getTeacherInfo(openId)

    i = 0
    projectList = {}
    tidList = []
    cidList = []
    for eachPage in teacherInfo:
        for project in eachPage["result"]:
            # 如果不是作业则跳过
            if project["type"] != 0:
                continue

            # print(project["type"])
            projectList[i] = project["notify"][0]["title"] + "\n" +project["notify"][0]["text_content"] + "\n\n"
            tidList.append(project["notify"][0]["_id"])
            cidList.append(project["cls"])

            i = i + 1

    print("项目列表：")
    for key,value in projectList.items():
        print('{key}.{value}'.format(key = key, value = value))

    choose = int(input("请选择作业项目："))

    tid = tidList[choose]
    cid = cidList[choose]

    teacherDetail = getTeacherDetail(openId, tid, cid)
    teacherDetail = json.loads(teacherDetail)
    membersMap = teacherDetail['membersMap']
    feedBacks = teacherDetail['accepts']

    print('\n\n作业提交列表：\n')

    for eachFeedback in feedBacks:
        studentId = eachFeedback['member']

        studentName = membersMap[studentId]['name']
        print(studentName)

        studentPhone = membersMap[studentId]['phone']

        feedBackText = eachFeedback['feedback_text']
        print('文字：', feedBackText)

        feedBackPhoto = eachFeedback['feedback_photo']
        print("图片：")
        for photo in feedBackPhoto:
            url = "http://img.welife001.com/"
            photoUrl = url + photo
            print(photoUrl)
        
        print("\n")

