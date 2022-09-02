#-- coding: utf-8 --
from email import header
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
7.27 长安深蓝
抓取 app-api.deepal.com.cn 域名下的 Authorization 和 UA
7.28 增加每日使用时长任务
7.31 修正登录任务逻辑
8.11 加入可兑换列表
8.25 新增评论、发帖任务
"""

# # 登录任务
# def login():
#     global Authorization, User_Agent
#     # 填写自己的Authorization，UA
#     Authorization = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjoxNTY1Mjk4Mjg1NzkwMjI0Mzg2LCJybiI6IlZGamkwWm05MlVPbW5wUkVveXl0OEtJT281WGlBNEVFIn0.mhmNFLWYF-yPPKXx8ykmMxJZogd4lYutZlpR5PyGVYM'
#     User-Agent = "CAQC/1.1.2 (iPhone; iOS 14.8.1; Scale/3.00)"
#     url = 'https://app-api.deepal.com.cn/appapi/auth/wxlogin?code=081sJi000xlItO1UMb400zmRWf0sJi0V&appId=wx0c0217402bdf4059&refereeId=1565290440666365953'
#     header = {
#         'Authorization': f'{Authorization}', 
#         'User-Agent': f'{User-Agent}',
#     }
#     resp = requests.get(url=url, headers=header).json()
#     print(resp)
#     t = random.randint(1,3)  # 随机时间操作
#     print("随机等待->>" + str(t) + "秒\n")
#     time.sleep(t)
#     sign_in()

# 浏览资讯任务
def view_dynamic():
    url = 'https://app-api.deepal.com.cn/appapi/v1/m_app/article/query'
    header = {
        "Host": "app-api.deepal.com.cn",
        "appId": "sl_ios",
        "Content-Type": "application/json",
        "version": "1.1.2",
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjoxNTY1Mjk4Mjg1NzkwMjI0Mzg2LCJybiI6IlZGamkwWm05MlVPbW5wUkVveXl0OEtJT281WGlBNEVFIn0.mhmNFLWYF-yPPKXx8ykmMxJZogd4lYutZlpR5PyGVYM",
        "Application-Version-Secret": "1661530310.000000",
        "Accept": "*/*",
        "appVersion": "1.1.2",
        "Accept-Language": "zh-Hans-CN;q=1",
        "packageName": "deepal.com.cn.app",
        "Accept-Encoding": "gzip, deflate, br",
        "appType": "ios",
        "deviceId": "deviceId",
        "User-Agent": "CAQC/1.1.2 (iPhone; iOS 14.8.1; Scale/3.00)",
        "Content-Length": "61",
        "Connection": "keep-alive",
        "environment": "dev",
    }
    body = {
        "body" : {
        "isRecommend" : "1"
        },
        "size" : 10,
        "lastId" : "0",
        "index" : 1
    }
    resp = requests.post(url=url, headers=header, data=json.dumps(body)).json()
    for i in resp['data']['commentList']:
        

# # 评论任务
# def comment():
#     url = 'https://api.yqypt.com/v2/information/comment/add'
#     hd = {
#         "Accept": "application/json, text/plain, */*",
#         "token": f"{token}",
#         "Content-Type": "application/json;charset=utf-8",
#         "User-Agent": f'{User_Agent}',
#     }
#     body = {
#         "content" : f"{word1}",
#         "informationId" : f'{id}'
#     }
#     resp = requests.post(url=url, headers=hd, data=json.dumps(body)).json()
#     print(f'\n评论任务结果：' + resp['message'])
#     pulish()

# # 点赞任务
# def fabulous():
#     url = f"https://ranlv.lvfacn.com/api.php/Ranlv/checkPraise?access_token={access_token}&like_ran=1&member_id=1408390&user_token={user_token}&video_id={video_id}"
#     resp = requests.get(url=url, headers=header).json()
#     print(f'\n点赞结果:' + resp['msg'])
#     t = random.randint(1,3)  # 随机时间操作
#     print("随机等待->>" + str(t) + "秒\n")
#     time.sleep(t)
#     comment()
    
# # 收藏任务
# def shoucang():
#     pass

# # 分享任务
# def share():
#     url = 'https://api.yqypt.com/v2/share?resourceId=1&resourceType=APP'
#     resp = requests.get(url=url, headers=header).json()
#     print(f'\n分享结果:' + resp['message'])
#     t = random.randint(3,5)  # 随机时间操作
#     print("随机等待->>" + str(t) + "秒\n")
#     time.sleep(t)
#     read()
    
# # 浏览动态
# def dongtai():
#     pass

# # 评论动态
# def pinglundongtai():
#     pass

# # 收藏动态
# def shoucangdongtai():
#     pass

# # 分享动态
# def shoucangdongtai():
#     pass

# # 大家发帖
# def shoucangdongtai():
#     pass

# # 阅读文章任务
# def read():
#     global id
#     # 当前日期和时间
#     now = datetime.now()
#     timestamp = int(datetime.timestamp(now)*1000)
#     pageId = [-1,6,11,13,16]    # 页面id
#     categoryId = random.choice(pageId)
#     url = f'https://api.yqypt.com/v2/information/list?categoryId={categoryId}&pageNum=1&pageSize=3&timestamp={timestamp}'
#     resp = requests.get(url=url, headers=header).json()
#     ids = []
#     for i in resp['data']:
#         informationId = i['informationId']
#         titleId = i['title']
#         ids.append(informationId)
#         read_url = f'https://api.yqypt.com/v2/information/details?informationId={informationId}'
#         read_resp = requests.get(url=read_url, headers=header).json()
#         print(f'\n随机抽取文章，标题为：' + titleId + f'\n阅读结果：' + read_resp['message'])
#         t = random.randint(2,7)  # 随机时间操作
#         print("随机等待->>" + str(t) + "秒\n")
#         time.sleep(t)
#     id = random.choice(ids)     # 随机得出文章ID
#     use()

# # 使用时长任务
# def use():
#     url = 'https://api.yqypt.com/v2/count/cumulative_use'
#     resp = requests.get(url=url, headers=header).json()
#     print(f'App使用时长结果：' + resp['message'])
#     word()

# # 随机获取发言及评论内容
# def word():
#     global word1, word2
#     # 天行api的key
#     key = '1db4a5affbd4487a92c1f6ec399410fa'
#     word_url1 = f'http://api.tianapi.com/zmsc/index?key={key}'  # 最美宋词
#     word_url2 = f'http://api.tianapi.com/lzmy/index?key={key}'  # 励志古言
#     header = {
#         'Content-Type': 'application/x-www-form-urlencoded',
#     }
#     resp1 = requests.get(url=word_url1, headers=header).json()
#     word1 = resp1['newslist'][0]['content']  # 最美宋词
#     resp2 = requests.get(url=word_url2, headers=header).json()
#     word2 = resp2['newslist'][0]['saying']   # 励志古言
#     comment()


# # 发帖任务
# def pulish():
#     id_url = 'https://api.yqypt.com/v2/topic/list?pageNum=1&pageSize=50'    # 帖子ID的url
#     id_resp = requests.get(url=id_url, headers=header).json()
#     ids = []
#     for i in id_resp['data']:
#         Ida = i['topicId']   # 获取帖子ID
#         ids.append(Ida)  # 将帖子ID存入列表
#     topicId = random.choice(ids) 
#     url = 'https://api.yqypt.com/v2/posting/publish'
#     hd = {
#         "token": f"{token}",
#         "User-Agent": f'{User_Agent}',
#         "ua": f'{ua}',
#         "Content-Type": "application/json",
#     }
#     body = {
#         "content" : f"{word2}",
#         "attachments" : [

#         ],
#         "topicId" : f"{topicId}"
#     }
#     resp = requests.post(url=url, headers=hd, data=json.dumps(body)).json()
#     print(f'\n发帖任务结果：' + resp['message'])
#     user_info()

# # 个人情况
# def user_info():
#     global user_integralNum, nickname
#     url = 'https://api.yqypt.com/v2/integral/info'
#     resp = requests.get(url=url, headers=header).json()
#     user_integralNum = resp['data']['integralNum']      # 账户积分
#     user_url = 'https://api.yqypt.com/v2/users/basic_info'
#     user_resp = requests.get(url=user_url, headers=header).json()
#     nickname = user_resp['data']['nickname']     # 账户名称
#     print(f'\n账户：' + str(nickname) + f'，账户积分：' + str(user_integralNum))
#     # # 发送结果至tg bot
#     # send_url = f'https://dianbao.vercel.app/send/3AD32DBFDDD71\/' + '优企莹账户：' + str(nickname) + '，积分：' + str(user_integralNum)
#     # send_resp = requests.get(send_url)
#     task_list()

# 任务完成情况
def task_list():
    url = 'https://app-api.deepal.com.cn/appapi/v1/member/member/ms/point/task'
    header = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJsb2dpbklkIjoxNTY1Mjk4Mjg1NzkwMjI0Mzg2LCJybiI6IlZGamkwWm05MlVPbW5wUkVveXl0OEtJT281WGlBNEVFIn0.mhmNFLWYF-yPPKXx8ykmMxJZogd4lYutZlpR5PyGVYM",
        "User-Agent": "CAQC/1.1.2 (iPhone; iOS 14.8.1; Scale/3.00)",
    }
    resp = requests.get(url=url, headers=header).json()
    # 每日首次登录进度
    login_result = resp['data'][0]['ruleName'] + f'完成情况：' + str(resp['data'][0]['rulePointNum']) + f'\n'
    print(login_result)
    # 每日首次分享进度
    share_result = resp['data'][1]['ruleName'] + f'完成情况：' + str(resp['data'][1]['rulePointNum']) + f'\n'
    # # 每日累计使用进度
    # use_result = resp['data'][2]['taskName'] + f'完成情况：' + str(resp['data'][2]['isComplete']) + f'\n'
    # # 每日累计阅读进度
    # read_result = resp['data'][3]['taskName'] + f'完成情况：' + str(resp['data'][3]['isComplete']) + f'\n'
    # # 首次填写个人信息
    # complete_result = resp['data'][4]['taskName'] + f'完成情况：' + str(resp['data'][4]['isComplete']) + f'\n'
    # # 首次学生认证
    # student_result = resp['data'][5]['taskName'] + f'完成情况：' + str(resp['data'][5]['isComplete']) + f'\n'
    # # 新用户首次注册
    # register_result = resp['data'][6]['taskName'] + f'完成情况：' + str(resp['data'][6]['isComplete']) + f'\n'
    # # 技能认证
    # skill_result = resp['data'][7]['taskName'] + f'完成情况：' + str(resp['data'][7]['isComplete']) + f'\n'
    # # 每日发帖
    # post_result = resp['data'][8]['taskName'] + f'完成情况：' + str(resp['data'][8]['isComplete']) + f'\n'
    # # 每日评论
    # comment_result = resp['data'][9]['taskName'] + f'完成情况：' + str(resp['data'][9]['isComplete']) + f'\n'
    # # 意见采纳
    # feedback_result = resp['data'][10]['taskName'] + f'完成情况：' + str(resp['data'][10]['isComplete']) + f'\n'
    # print(f'\n【任务列表】\n' + login_result + share_result + use_result + read_result + complete_result + student_result + register_result + skill_result + post_result + comment_result + feedback_result)
    # list()

# # 奖品列表
# def list():
#     url = 'https://api.yqypt.com/v2/integral/prize/list'
#     resp = requests.get(url=url, headers=header).json()
#     print(str(nickname) + '\n【可兑换商品】')
#     lsts = []   # 用于存放兑换商品的列表
#     for i in resp['data']:
#         integralNum = i['integralNum']
#         prizeName = i['prizeName']
#         if integralNum < user_integralNum:
#             lst = str(prizeName) + f'，'+ str(integralNum) 
#             lsts.append(lst)
#             print(lst)
#     # # 发送结果至tg bot
#     # send_url = f'https://dianbao.vercel.app/send/3AD32DBFDDD71\/' + f'可兑换商品为：' + str(lsts)
#     # send_resp = requests.get(send_url)
        
def main() :
    view_dynamic()

if __name__ == '__main__':
    main()
