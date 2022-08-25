#-- coding: utf-8 --
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests
import json
import random
import time
from datetime import datetime
from random import choice

"""
7.27 优企莹
抓取 api.yqypt.com 域名下的 clientId 和 token，分别填写在140和143行

7.28 增加每日使用时长任务

7.31 修正登录任务逻辑

8.11 加入可兑换列表
"""

# 登录任务
def login():
    global token
    url = 'https://api.yqypt.com/v2/auth'
    hd = {
        'Host': 'api.yqypt.com',
        'Accept': '*/*',
        'clientId': 'ed18359b98454ea8aefbe5948a174d32',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-Hans-CN;q=1',
        'versionName': '2.4.5',
        'token': '',
        'clientType': 'iOS',
        'User-Agent': 'shapedPolicy/2.4.5 (iPhone; iOS 14.8.1; Scale/3.00)',
        'Content-Length': '71',
        'ua': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/611.4.2.0.3 (KHTML, like Gecko) Mobile/18H107',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',   
    }
    body = {
        "phone" : "13436925810",    # 输入登录手机号
        "authWay" : "PHONE_PASSWORD",
        "password" : "asd1234"      #输入密码
    }
    resp = requests.post(url=url, headers=hd, data=json.dumps(body)).json()
    token = resp['data']['token']       # 获取到账号token
    print(f'\n登录结果:' + resp['message'])
    t = random.randint(1,3)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    sign_in()
    

# 签到任务
def sign_in():
    global header
    url = 'https://api.yqypt.com/v2/integral/sign_in'
    header = {
        'Host': 'api.yqypt.com',
        'clientId': 'ed18359b98454ea8aefbe5948a174d32', 
        'User-Agent': 'shapedPolicy/2.4.2 (iPhone; iOS 14.8.1; Scale/3.00)',
        'token': f'{token}'
    }
    resp = requests.post(url=url, headers=header).json()
    print(f'\n签到结果:' + resp['message'])
    t = random.randint(2,6)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    share()
    
    
# 分享任务
def share():
    url = 'https://api.yqypt.com/v2/share?resourceId=1&resourceType=APP'
    resp = requests.get(url=url, headers=header).json()
    print(f'\n分享结果:' + resp['message'])
    t = random.randint(3,5)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    read()
    
# 阅读文章任务
def read():
    # 当前日期和时间
    now = datetime.now()
    timestamp = int(datetime.timestamp(now)*1000)
    pageId = [-1,6,11,13,16]    # 页面id
    categoryId = random.choice(pageId)
    url = f'https://api.yqypt.com/v2/information/list?categoryId={categoryId}&pageNum=1&pageSize=3&timestamp={timestamp}'
    resp = requests.get(url=url, headers=header).json()
    for i in resp['data']:
        informationId = i['informationId']
        titleId = i['title']
        read_url = f'https://api.yqypt.com/v2/information/details?informationId={informationId}'
        read_resp = requests.get(url=read_url, headers=header).json()
        print(f'\n随机抽取文章，标题为：' + titleId + f'\n阅读结果：' + read_resp['message'])
        t = random.randint(2,7)  # 随机时间操作
        print("随机等待->>" + str(t) + "秒\n")
        time.sleep(t)
    use()

# 使用时长任务
def use():
    url = 'https://api.yqypt.com/v2/count/cumulative_use'
    resp = requests.get(url=url, headers=header).json()
    print(f'App使用时长结果：' + resp['message'])
    user_info()

# 个人情况
def user_info():
    global userInfo
    url = 'https://api.yqypt.com/v2/integral/info'
    resp = requests.get(url=url, headers=header).json()
    userInfo = resp['data']['integralNum']
    print(f'\n账户积分：' + str(userInfo))
    # 发送结果至tg bot
    send_url = f'https://dianbao.vercel.app/send/3AD32DBFDDD71\/' + '优企莹账户积分：' + str(userInfo)
    send_resp = requests.get(send_url)
    task_list()

# 任务完成情况
def task_list():
    url = 'https://api.yqypt.com/v2/integral/task/list'
    resp = requests.get(url=url, headers=header).json()
    # 每日首次登录进度
    login_result = resp['data'][0]['taskName'] + f'完成情况：' + str(resp['data'][0]['isComplete']) + f'\n'
    # 每日首次分享进度
    share_result = resp['data'][1]['taskName'] + f'完成情况：' + str(resp['data'][1]['isComplete']) + f'\n'
    # 每日累计使用进度
    use_result = resp['data'][2]['taskName'] + f'完成情况：' + str(resp['data'][2]['isComplete']) + f'\n'
    # 每日累计阅读进度
    read_result = resp['data'][3]['taskName'] + f'完成情况：' + str(resp['data'][3]['isComplete']) + f'\n'
    # 首次填写个人信息
    complete_result = resp['data'][4]['taskName'] + f'完成情况：' + str(resp['data'][4]['isComplete']) + f'\n'
    # 首次学生认证
    student_result = resp['data'][5]['taskName'] + f'完成情况：' + str(resp['data'][5]['isComplete']) + f'\n'
    # 新用户首次注册
    register_result = resp['data'][6]['taskName'] + f'完成情况：' + str(resp['data'][6]['isComplete']) + f'\n'
    # 技能认证
    skill_result = resp['data'][7]['taskName'] + f'完成情况：' + str(resp['data'][7]['isComplete']) + f'\n'
    print(f'\n【任务列表】\n' + login_result + share_result + use_result + read_result + complete_result + student_result + register_result + skill_result)
    list()

# 奖品列表
def list():
    url = 'https://api.yqypt.com/v2/integral/prize/list'
    resp = requests.get(url=url, headers=header).json()
    print('\n【可兑换列表】')
    for i in resp['data']:
        integralNum = i['integralNum']
        prizeName = i['prizeName']
        if integralNum < userInfo:
            print(str(integralNum) + ' ' + str(prizeName))
        else:
            pass
        

def main() :
    login()
    
def main_handler(event, context):
    return main()

if __name__ == '__main__':
    main()
