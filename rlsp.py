#-- coding: utf-8 --
import io
import sys
from h11 import Data
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests
import json
import random
import time
from datetime import datetime

# 获取ck及视频id
def get_cookie():
    global access_token, user_token, video_id, header
    # 填写access_token和user_token
    access_token = "f2e1d57418bb3d6a0439b494f3468a75"
    user_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJSYW5sdiBKV1QiLCJpYXQiOjE2NDg2MDE5NTcsImV4cCI6MzI5NzIwMzkxNCwiYXVkIjoiUmFubHYiLCJzdWIiOiJSYW5sdiIsImRhdGEiOnsibWVtYmVyX2lkIjoxNDA4MzkwLCJhdmF0YXIiOiJodHRwOlwvXC9yYW5sdi5sdmZhY24uY29tXC9zdGF0aWNcL21vZHVsZVwvYWRtaW5cL2ltZ1wvZGVmYXVsdF9oZWFkLmpwZyIsIm5pY2tuYW1lIjoiXHU3OTVlXHU5YTZjXHU2MGM1XHU1MWI1IiwibW9iaWxlIjoiMTM5MTEwMjk5MjMiLCJpc19jb3JwIjowfX0.mptkcU-dY6r1vUPKM7mC8hl4OgorPp9GSfZ_3x9u2jQ"
    # 获取视频id
    page = str(random.randint(0,5499))      # 页码范围为随机数，因为指定了行数（list_rows）为1，所以生成随机页码后，即可获得随机视频id
    url = f"https://ranlv.lvfacn.com/api.php/Ranlv/index?access_token={access_token}&category=19&list_rows=1&member_id=1408390&page="+ page +f"&user_token={user_token}"
    header = {
        'Referer': "https://ran.lvfacn.com/pages/rank/prizeapp?",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    resp = requests.post(url=url, headers=header)
    dic = resp.json()
    # 获取一个视频id
    for i in dic['data']['data']:
        video_id = i['id']
        title = i['title']
        print(f'\n随机获取视频id成功！' + f'视频名称：' + str(title))
    t = random.randint(1,5)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    video()
    
# 观看视频任务
def video():
    url = f"https://ranlv.lvfacn.com/api.php/Common/pvlog?access_token={access_token}&client=1&member_id=1408390&redouble=1&user_token={user_token}&uuid=29FBFDCB-79D9-4A2C-A0A7-85E952D396B3&video_id={video_id}"
    resp = requests.get(url=url, headers=header).json()
    print(f'\n视频观看结果:' + resp['msg'])
    t = random.randint(1,8)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    fabulous()

# 点赞任务
def fabulous():
    url = f"https://ranlv.lvfacn.com/api.php/Ranlv/checkPraise?access_token={access_token}&like_ran=1&member_id=1408390&user_token={user_token}&video_id={video_id}"
    resp = requests.get(url=url, headers=header).json()
    print(f'\n点赞结果:' + resp['msg'])
    t = random.randint(1,3)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    comment()

# 评论任务
def comment():
    url = f"https://ranlv.lvfacn.com/api.php/Ranlv/addComments?access_token={access_token}&content=%E5%A5%BD%E7%9A%84%E5%91%80&member_id=1408390&to_user_id=1278212&user_token={user_token}&video_id={video_id}"
    resp = requests.get(url=url, headers=header).json()
    print(f'\n评论结果:' + resp['msg'])
    t = random.randint(1,15)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    goVote()

# 投票任务
def goVote():
    global charts_id
    # 获取榜单信息
    title_id = str(random.randint(0,100))
    list_url = f"https://ranlv.lvfacn.com/api.php/Rcharts/getRank?access_token={access_token}&basis=0&id={title_id}&list_rows=1&member_id=1408390&page=1&ran=1&user_token={user_token}"
    resp = requests.post(url=list_url, headers=header)
    dic = resp.json()
    # 获取榜单id
    for i in dic['data']['data']:
        list_id = i['id']
    # 获取投票id
    charts_id = str(random.randint(0,100))
    vote_url = f"https://ranlv.lvfacn.com/api.php/Rcharts/goVote?access_token={access_token}&charts_id={charts_id}&is_act=1&member_id=1408390&num=1&user_token={user_token}&video_id={list_id}"
    resp = requests.get(url=vote_url, headers=header).json()
    t = random.randint(3,11)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    print(f'\n投票结果:' + resp['msg'])
    share()

# 分享任务
def share():
    url = f'https://ranlv.lvfacn.com/api.php/Rcharts/shareVideo?access_token={access_token}&member_id=1408390&user_token={user_token}&video_id={charts_id}'
    headers = {
        'User-Agent': 'ran lu shi pin/1.0.79 (iPhone; iOS 14.8.1; Scale/3.00)'
    }
    resp = requests.post(url=url, headers=headers).json()
    user_info()

# # 榜单任务
# def myVote():
#     url = 'https://ranlv.lvfacn.com/api.php/Rcharts/myVotes'
#     data = "{\"access_token\":\"f2e1d57418bb3d6a0439b494f3468a75\",\"user_token\":\"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJSYW5sdiBKV1QiLCJpYXQiOjE2NDg2MDE5NTcsImV4cCI6MzI5NzIwMzkxNCwiYXVkIjoiUmFubHYiLCJzdWIiOiJSYW5sdiIsImRhdGEiOnsibWVtYmVyX2lkIjoxNDA4MzkwLCJhdmF0YXIiOiJodHRwOlwvXC9yYW5sdi5sdmZhY24uY29tXC9zdGF0aWNcL21vZHVsZVwvYWRtaW5cL2ltZ1wvZGVmYXVsdF9oZWFkLmpwZyIsIm5pY2tuYW1lIjoiXHU3OTVlXHU5YTZjXHU2MGM1XHU1MWI1IiwibW9iaWxlIjoiMTM5MTEwMjk5MjMiLCJpc19jb3JwIjowfX0.mptkcU-dY6r1vUPKM7mC8hl4OgorPp9GSfZ_3x9u2jQ\"}"
#     resp = requests.post(url=url, headers=header, data=data)
#     print(resp.json())

#  账号信息
def user_info():
    url = f'https://ranlv.lvfacn.com/api.php/Member/mine?access_token={access_token}&member_id=1408390&user_id=1408390&user_token={user_token}'
    resp = requests.get(url=url, headers=header)
    dic = resp.json()
    # 昵称
    nickname = str(dic['user']['nickname'])
    # 账户余额
    balance = str(dic['user']['balance'])  
    print(f'\n账号名称：' + nickname + f'\n余额：' + balance)
    time.sleep(1)
    money_rank()

# 获取赚钱任务进度
def money_rank():
    url = f"https://ranlv.lvfacn.com/api.php/Share/wiTask?access_token={access_token}&member_id=1408390&user_token={user_token}"
    resp = requests.get(url=url, headers=header)
    dic = resp.json()
    # 发布作品任务进度
    release_result = str(dic['data'][0]['title']) + f'进度:' + str(dic['data'][0]['to_num']) + f'/' + str(dic['data'][0]['num'])
    # 点赞任务进度
    fabulous_result = str(dic['data'][1]['title']) + f'进度:' + str(dic['data'][1]['to_num']) + f'/' + str(dic['data'][1]['num'])
    # 评论任务进度
    comment_result = str(dic['data'][2]['title']) + f'进度:' + str(dic['data'][2]['to_num']) + f'/' + str(dic['data'][2]['num'])
    # 完善资料任务进度
    data_result = str(dic['data'][3]['title']) + f'进度:' + str(dic['data'][3]['to_num']) + f'/' + str(dic['data'][3]['num'])
    # 看视频任务进度
    video_result = str(dic['data'][4]['title']) + f'进度:' + str(dic['data'][4]['to_num']) + f'/' + str(dic['data'][4]['num'])
    # 投票任务进度
    goVote_result = str(dic['data'][5]['title']) + f'进度:' + str(dic['data'][5]['to_num']) + f'/' + str(dic['data'][5]['num'])
    print(f"\n任务进度列表：" + "\n" + release_result + "\n" + fabulous_result + "\n" + comment_result + "\n" + data_result + "\n" + video_result + "\n" + goVote_result)

def main() :
    get_cookie()

if __name__ == '__main__':
    main()
