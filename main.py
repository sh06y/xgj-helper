# -*- coding:UTF-8-*-
from teacherDetail import getTeacherDetail
from teacherInfo import getTeacherInfo
from userInfo import getUserInfo
import sys
import json
import os

teacherDict = {
    '崔涵': 'oWRkU0aFPaVRKtGpuh0pMtowgtXM',
    '曹春嫒': 'oWRkU0XFQmnxgZlQd_Hah4uEuYw0',
    '席天泽': 'oWRkU0ckJAbRMWQCivA-5Kg9l5Wg',
    '田雨': 'oWRkU0TFZ-LTT7TgUhQCGHvpjsNg',
    '魏霞': 'oWRkU0Qm8Cc7pHX1yn442hgDEh48',
    '张冰': 'oWRkU0Ssmriy2ovAWdAUEzfxvuik',
    '胡宇玲': 'oWRkU0YVGLxLJHAXKosFle5V2dCU',
    '隗华': 'oWRkU0dZAuJx_cZfTLYD-qQHj2aw',
    '田立华': 'oWRkU0e7w2gtsJc_fbZQtu31Cc-o',
    '屈程斌': 'oWRkU0fWcVxUwZB9Y_jwpna9P6XI',
    '王珂': 'oWRkU0WlUOgGhBLf9q2rTJTHn2-4',
    '刘晓芸': 'oWRkU0b5TnhSY5kPHz9Z80vTDTr0',
    '果杰': 'oWRkU0YsbeyB1JQ69o_QAerG4e5Y',
    '王向阳': 'oWRkU0SzdIgA6Y-nrofz0I_gNw88',
    '于秀齐': 'oWRkU0bMG_qJtV66LjpueRjFdp9M',
    '张悦': 'oWRkU0cTJcXzfrWgG1XCnNxWZG8E',
    '刘德斌': 'oWRkU0YIgbfbnKwNIWqCN3tJ571A',
    '赵敬东': 'oWRkU0XpatFnNVvmqDqnYQmmKERk',
    '成桂文': 'oWRkU0Sx6E2ednPpfq15WbTaUIJc',
    '张璟琳': 'oWRkU0b_mqqvgBL2Z6RGe8bev5Uk',
    '姜涵': 'oWRkU0SojLeoC2q79xUqCzmz9OJA',
    '刘悦奇': 'oWRkU0QvjZtnWtjxoi-1b5h0H120',
    '张艾': 'oWRkU0ZDBvPBqzgdH0KN1bEfY1aM',
    '朵朵媛': 'oWRkU0RdTvrSh23lMxEx6otniTvs',
    '武思远': 'oWRkU0dj8z37k2F1V9yPwZKezaTM',
    '唐雯竹': 'oWRkU0Tk1KMxoS01J60PXTy6wCOE',
    '李任宏': 'oWRkU0XWvYQdbhB41eu8Yv7vqbyk',
    '王苒苒': 'oWRkU0aIubjleiS6CPLQFvQaFDas',
    '陶昌书': 'oWRkU0fxtJK6eGbOCBSD0a_RngU0',
    '马征': 'oWRkU0UyOJPiFrtWlAIctzy3cddo'
}

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
    ret = input("请输入教师姓名: ")
    if ret in teacherDict:
        return teacherDict[ret]
    else:
        print("您输入的教师在数据库中不存在, 请选择 1: 继续使用教师姓名检索 2: 使用教师openID检索 3: 退出程序")
        choose = int(input("输入您的选择: "))
        if choose == 1:
            return getTeacherOpenIdByTeacherName()
        elif choose == 2:
            return getTeacherOpenIdByOpenId()
        elif choose == 3:
            return "__exit"


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
            with open(txt_name+'.txt', 'w', encoding='utf-8') as f:
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
