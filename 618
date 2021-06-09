import requests
import re
import json
import urllib
import time
import timeit
import math
import sys
from datetime import datetime
from dateutil import tz
import os
import dateutil.parser

osenviron={}
djj_djj_cookie=''
Card_telegram=''
Card_num=0
github=1#判断是否在远程运行

#618入口https://carnivalcity.m.jd.com/#/home
#通知telegram格式,机器人id@自己的id




userNameList = []
cookiesList = []
pinNameList = []
shareIdlist=[]#互助码

#=============
questionTask={}
meetingTask= []
shopTask= []
skuTask= []
brandList=[]


      
shareId=''
result=''
bean=0
jifen=0
ispartin=False
result_all=''

def getUserInfo(ck, pinName):
    url = 'https://me-api.jd.com/user_new/info/GetJDUserInfoUnion?orgFlag=JD_PinGou_New&callSource=mainorder&channel=4&isHomewhite=0&sceneval=2&sceneval=2&callback=GetJDUserInfoUnion'
    headers = {
        'Cookie': ck,
        'Accept': '*/*',
        'Connection': 'close',
        'Referer': 'https://home.m.jd.com/myJd/home.action',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': 'me-api.jd.com',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
        'Accept-Language': 'zh-cn'
    }
    try:
        resp = requests.get(url=url, headers=headers, timeout=60).text
        r = re.compile(r'GetJDUserInfoUnion.*?\((.*?)\)')
        result = r.findall(resp)
        userInfo = json.loads(result[0])
        nickname = userInfo['data']['userInfo']['baseInfo']['nickname']
        return ck, nickname
    except Exception:
        pushmsg(f"用户【{pinName}】Cookie 已失效！",'请重新获取。')
        
        return ck, False


def iscookie():
    
    cookies = djj_djj_cookie
    
    if 'pt_key=' in cookies and 'pt_pin=' in cookies:
        r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
        result = r.findall(cookies)
        if len(result) >= 1:
            print("您已配置{}个账号".format(len(result)))
            for i in re
