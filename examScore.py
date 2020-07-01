# -*- coding:UTF-8-*-
# ************************************************************
#   Copyright (C),2020, sy
#   FileName: examScore.py
#   Author: sy        Date: 2020.5-6
#   Description: Get exam score
#   函数列表:
#   1.getScores
#       功能：获取作业（考试）分数
#       输入：teacherDetail.py 中输出的json
#       输出：list，格式为 姓名-作业分数-答题卡分数（如果有）
#
# ***********************************************************

import json
import requests
from requests.packages import urllib3


def getScores(teacherDetailData):
    # print(teacherDetailData)
    students = json.loads(teacherDetailData, strict=False)

    memberMap = students['membersMap']
    return_list = []
    for student in students['accepts']:
        # print(student)
        # student = json.loads(student)
        id = student['member']
        name = memberMap[id]['name']
        homeworkScore = student['reply_rate']
        answersheetScore = student['examdetail']['rate']
        return_dict = {
            "name": name,
            "homeworkScore": homeworkScore,
            "answersheetScore": answersheetScore,
            "score": homeworkScore + answersheetScore
        }
        return_list.append(return_dict)
        # print(name, homeworkScore, answersheetScore, sep=',')

    # print(return_list)
    return return_list


if __name__ == '__main__':
    a = input()
    getScores(a)
