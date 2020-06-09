# -*- coding:UTF-8-*-
from teacherDetail import getTeacherDetail
from teacherInfo import getTeacherInfo
from userInfo import getUserInfo
import sys
import json
import os
import requests

# openId = input("请输入教师openId（任意一个）:")
# openId = ""
print('''
1: 获取作业内容
''')

n = input("您想做什么: ")


def getTeacherOpenIdByOpenId():
    ret = input("请输入教师openID: ")
    return ret


def getTeacherOpenIdByTeacherName():
    name = input("请输入教师姓名: ")
    # if ret in teacherDict:
    #     return teacherDict[ret]
    # else:
    #     print("您输入的教师在数据库中不存在, 请选择 1: 继续使用教师姓名检索 2: 使用教师openID检索 3: 退出程序")
    #     choose = int(input("输入您的选择: "))
    #     if choose == 1:
    #         return getTeacherOpenIdByTeacherName()
    #     elif choose == 2:
    #         return getTeacherOpenIdByOpenId()
    #     elif choose == 3:
    #         return "__exit"
    url = 'http://148.70.30.208:5000/searchTeacherByName'
    data = {
        "name": name
    }
    try:
        request = requests.post(url, data=data)
    except:
        print("network error")
    openid = request.text
    openid = json.loads(openid)
    openid = openid['data']['openId']
    return openid


if n == "1":
    print("是否使用教师姓名检索 1:是 2:否\n")
    teacherInfoGetType = int(input("输入您的选择: "))
    openId = ""
    if (teacherInfoGetType == 1):
        openId = getTeacherOpenIdByTeacherName()
        if (openId == "__exit"):
            os.system("clear")
            sys.exit()
    elif (teacherInfoGetType == 2):
        openId = getTeacherOpenIdByOpenId()
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
            projectList[i] = project["notify"][0]["title"] + \
                             "\n" + project["notify"][0]["text_content"]
            tidList.append(project["notify"][0]["_id"])
            cidList.append(project["cls"])

            i = i + 1

    print("项目列表: ")
    print("-----------------------------------------------")
    for key, value in projectList.items():
        print('{key}.{value}'.format(key=key, value=value))
        print("-----------------------------------------------")

    while True:
        choose = int(input("请选择作业项目: (若要停止请输入666)"))
        if (choose == 666):
            os.system("clear")
            break
        tid = tidList[choose]
        cid = cidList[choose]

        teacherDetail = getTeacherDetail(openId, tid, cid)
        # print(teacherDetail)
        teacherDetail = json.loads(teacherDetail)
        membersMap = teacherDetail['membersMap']
        feedBacks = teacherDetail['accepts']

        # print('\n\n作业提交列表：\n')
        txt_choose = int(input("请选择是否创建txt文档:(若要创建请输入1，不创建请输入2)"))
        if txt_choose == 1:
            txt_name = input("请输入txt文档名称:")
            with open(txt_name + '.txt', 'w', encoding='utf-8') as f:
                for eachFeedback in feedBacks:
                    f.write('\n')
                    studentId = eachFeedback['member']

                    # studentName = membersMap[studentId]['name']
                    # print(studentName)

                    # studentPhone = membersMap[studentId]['phone']

                    # feedBackText = eachFeedback['feedback_text']
                    # print('文字：', feedBackText)

                    feedBackPhoto = eachFeedback['feedback_photo']
                    # print("图片：")
                    # for photo in feedBackPhoto:
                    #     url = "http://img.welife001.com/"
                    #     photoUrl = url + photo
                    #     print(photoUrl)

                    ret = membersMap[studentId]['name'] + '\n' + \
                          '文字: ' + eachFeedback['feedback_text'] + \
                          '\n' + '图片: ' + '\n'
                    f.write(ret)
                    for photo in feedBackPhoto:
                        url = "http://img.welife001.com/"
                        photoUrl = url + photo
                        f.write(photoUrl + '\n')
                    f.write('\n')
                    f.write("-----------------------------------------------\n")
        elif txt_choose == 2:
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
                print("-----------------------------------------------\n")
