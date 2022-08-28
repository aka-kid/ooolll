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
抓取 api.yqypt.com 域名下的 clientId 和 token
7.28 增加每日使用时长任务
7.31 修正登录任务逻辑
8.11 加入可兑换列表
8.25 新增评论、发帖任务
8.28 新增pushplus通知方式
"""

# 登录任务
def login():
    global token, header, User_Agent, ua
    # 填写自己的token,User-Agent,ua
    token = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxOTY0NiIsImlhdCI6MTY1OTMyNzk1MCwiZXhwIjoxNjYxOTE5OTUwfQ.EvuJKrbjU1Zgq4Dr3MIVZ5el1YNusgHM3Q1fbTxZb8E'
    User_Agent = "shapedPolicy/2.4.5 (iPhone; iOS 14.8.1; Scale/3.00)"
    ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/611.4.2.0.3 (KHTML, like Gecko) Mobile/18H107"
    url = 'https://api.yqypt.com/v2/app/info'
    header = {
        'Host': 'api.yqypt.com',
        # 填写自己的clientId
        'clientId': 'ed18359b98454ea8aefbe5948a174d32', 
        # 填写自己的UA
        'User-Agent': f'{User_Agent}',
        'token': f'{token}'
    }
    resp = requests.get(url=url, headers=header).json()
    print(f'\n登录结果:' + resp['message'])
    t = random.randint(1,3)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    sign_in()

# 签到任务
def sign_in():
    url = 'https://api.yqypt.com/v2/integral/sign_in'
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
    global id
    # 当前日期和时间
    now = datetime.now()
    timestamp = int(datetime.timestamp(now)*1000)
    pageId = [-1,6,11,13,16]    # 页面id
    categoryId = random.choice(pageId)
    url = f'https://api.yqypt.com/v2/information/list?categoryId={categoryId}&pageNum=1&pageSize=3&timestamp={timestamp}'
    resp = requests.get(url=url, headers=header).json()
    ids = []
    for i in resp['data']:
        informationId = i['informationId']
        titleId = i['title']
        ids.append(informationId)
        read_url = f'https://api.yqypt.com/v2/information/details?informationId={informationId}'
        read_resp = requests.get(url=read_url, headers=header).json()
        print(f'\n随机抽取文章，标题为：' + titleId + f'\n阅读结果：' + read_resp['message'])
        t = random.randint(2,7)  # 随机时间操作
        print("随机等待->>" + str(t) + "秒\n")
        time.sleep(t)
    id = random.choice(ids)     # 随机得出文章ID
    use()

# 使用时长任务
def use():
    url = 'https://api.yqypt.com/v2/count/cumulative_use'
    resp = requests.get(url=url, headers=header).json()
    print(f'App使用时长结果：' + resp['message'])
    word()

# 随机获取发言及评论内容
def word():
    global word1, word2
    # 天行api的key
    key = '1db4a5affbd4487a92c1f6ec399410fa'
    word_url1 = f'http://api.tianapi.com/zmsc/index?key={key}'  # 最美宋词
    word_url2 = f'http://api.tianapi.com/lzmy/index?key={key}'  # 励志古言
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    resp1 = requests.get(url=word_url1, headers=header).json()
    word1 = resp1['newslist'][0]['content']  # 最美宋词
    resp2 = requests.get(url=word_url2, headers=header).json()
    word2 = resp2['newslist'][0]['saying']   # 励志古言
    comment()

# 评论任务
def comment():
    url = 'https://api.yqypt.com/v2/information/comment/add'
    hd = {
        "Accept": "application/json, text/plain, */*",
        "token": f"{token}",
        "Content-Type": "application/json;charset=utf-8",
        "User-Agent": f'{User_Agent}',
    }
    body = {
        "content" : f"{word1}",
        "informationId" : f'{id}'
    }
    resp = requests.post(url=url, headers=hd, data=json.dumps(body)).json()
    print(f'\n评论任务结果：' + resp['message'])
    pulish()
    
# 发帖任务
def pulish():
    id_url = 'https://api.yqypt.com/v2/topic/list?pageNum=1&pageSize=50'    # 帖子ID的url
    id_resp = requests.get(url=id_url, headers=header).json()
    ids = []
    for i in id_resp['data']:
        Ida = i['topicId']   # 获取帖子ID
        ids.append(Ida)  # 将帖子ID存入列表
    topicId = random.choice(ids) 
    url = 'https://api.yqypt.com/v2/posting/publish'
    hd = {
        "token": f"{token}",
        "User-Agent": f'{User_Agent}',
        "ua": f'{ua}',
        "Content-Type": "application/json",
    }
    body = {
        "content" : f"{word2}",
        "attachments" : [

        ],
        "topicId" : f"{topicId}"
    }
    resp = requests.post(url=url, headers=hd, data=json.dumps(body)).json()
    print(f'\n发帖任务结果：' + resp['message'])
    user_info()

# 个人情况
def user_info():
    global user_integralNum, nickname
    url = 'https://api.yqypt.com/v2/integral/info'
    resp = requests.get(url=url, headers=header).json()
    user_integralNum = resp['data']['integralNum']      # 账户积分
    user_url = 'https://api.yqypt.com/v2/users/basic_info'
    user_resp = requests.get(url=user_url, headers=header).json()
    nickname = user_resp['data']['nickname']     # 账户名称
    print('\n账户：' + str(nickname) + '，账户积分：' + str(user_integralNum))
    # # 发送结果至tg bot
    # send_url = f'https://dianbao.vercel.app/send/3AD32DBFDDD71\/' + '优企莹账户：' + str(nickname) + '，积分：' + str(user_integralNum)
    # requests.get(send_url)
    # pushplus推送
    token_pushplus = '3b160e2b7e3c462daeb2e7f344202da9' #在pushplus网站中可以找到
    title= '账户：' + str(nickname) #改成你要的标题内容
    content = '账户积分：' + str(user_integralNum) #改成你要的正文内容
    send_url = 'http://www.pushplus.plus/send?token='+token_pushplus+'&title='+title+'&content='+content
    requests.get(send_url)
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
    # 每日发帖
    post_result = resp['data'][8]['taskName'] + f'完成情况：' + str(resp['data'][8]['isComplete']) + f'\n'
    # 每日评论
    comment_result = resp['data'][9]['taskName'] + f'完成情况：' + str(resp['data'][9]['isComplete']) + f'\n'
    # 意见采纳
    feedback_result = resp['data'][10]['taskName'] + f'完成情况：' + str(resp['data'][10]['isComplete']) + f'\n'
    print(f'\n【任务列表】\n' + login_result + share_result + use_result + read_result + complete_result + student_result + register_result + skill_result + post_result + comment_result + feedback_result)
    list()

# 奖品列表
def list():
    url = 'https://api.yqypt.com/v2/integral/prize/list'
    resp = requests.get(url=url, headers=header).json()
    print(str(nickname) + '\n【可兑换商品】')
    lsts = []   # 用于存放兑换商品的列表
    for i in resp['data']:
        integralNum = i['integralNum']
        prizeName = i['prizeName']
        if integralNum < user_integralNum:
            lst = str(prizeName) + f'，'+ str(integralNum) 
            lsts.append(lst)
            print(lst)
    # # 发送结果至tg bot
    # send_url = f'https://dianbao.vercel.app/send/3AD32DBFDDD71\/' + str(nickname) + '可兑换商品为：' + str(lsts)
    # requests.get(send_url)
    # pushplus推送
    token_pushplus = '3b160e2b7e3c462daeb2e7f344202da9' #在pushplus网站中可以找到
    title= str(nickname) + '兑换商品列表' #改成你要的标题内容
    content = str(lsts) #改成你要的正文内容
    send_url = 'http://www.pushplus.plus/send?token='+token_pushplus+'&title='+title+'&content='+content
    requests.get(send_url)
        
def main() :
    login()

if __name__ == '__main__':
    main()
