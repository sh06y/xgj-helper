# 班级小管家辅助系统

原文在这里：[https://mp.weixin.qq.com/s/x3gExnAU6Cylrlkurjs-9Q](https://mp.weixin.qq.com/s/x3gExnAU6Cylrlkurjs-9Q)

| 文件名 | 说明 |
| - | - |
| userInfo.py | 获取用户个人信息 |
| teacherDetail.py | 以教师身份获取课程信息 |
| teacherInfo.py | 获取教师信息 |
| daka.py | 还没完工的自动打卡 |
| main.py | 全自动脚本 |

## 安装

```bash
git clone https://github.com/sh06y/class.git
```

### 安装依赖库

```bash
pip install -r requirements.txt
```

## 使用方法

### 自动获取他人作业

运行`main.py`

### 手动获取他人作业（方法不唯一）

1. 小程序抓包，找到 `getParentInfo`（应该是），在response里找到项目创建者的openID（creator_wx_openid），复制

2. 打开`teacherInfo.py`，在变量`openId`中粘贴刚才复制的教师openId，运行

3. 在返回的 json 中找到项目，复制 `cls` 和 `notify` 下的 `_id`

4. 打开`teacherDetail.py`，按照注释在变量中分别粘贴刚才复制的内容

5. 运行，在返回的 json 中即可找到作业内容

## 班级小管家api（部分）

| URL | 说明 |
| - | - |
| <http://img.welife001.com/> | 高清大图 |
