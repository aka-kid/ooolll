#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
项目名称: JD-Script / jd_qjd
Author: Curtin
功能：全民抢京豆（7.2-7.15）：https://h5.m.jd.com/rn/3MQXMdRUTeat9xqBSZDSCCAE9Eqz/index.html?has_native=0
    满160豆需要20人助力，每个用户目前只能助力2次不同的用户。
Date: 2021/7/3 上午10:02
TG交流 https://t.me/topstyle996
TG频道 https://t.me/TopStyle2021
update: 2021.7.3 15:41
'''

#ck 优先读取【JDCookies.txt】 文件内的ck  再到 ENV的 变量 JD_COOKIE='ck1&ck2' 最后才到脚本内 cookies=ck
cookies = ''
qjd_zlzh = ['Your JD_User', '买买买', '东哥']

# 建议调整一下的参数
# UA 可自定义你的，注意格式
UserAgent = 'jdappiPhone10.0.413.7ca6eb91a888be488f194b9d9216cf711dd1b221anetwork/wifiADID/8679C062-A41A-4A25-88F1-50A7A3EEF34Amodel/iPhone8,1addressid/3723896896appBuild/167707jdSupportDarkMode/0Mozilla/5.0 (iPhone CPU iPhone OS 13_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148supportJDSHWK/1'
# 限制速度 （秒）
sleepNum = 0.1


import os, re
import random, string
try:
    import requests
except Exception as e:
    print(e, "\n缺少requests 模块，请执行命令安装：python3 -m pip install requests")
    exit(3)
from urllib.parse import unquote, quote
import json
import time
requests.packages.urllib3.disable_warnings()

ss = requests.session()

pwd = os.path.dirname(os.path.abspath(__file__)) + os.sep
t = time.time()
aNum = 0
beanCount = 0
userCount = {}

class getJDCookie(object):
    # 适配各种平台环境ck
    def getckfile(self):
        if os.path.exists(pwd + 'JDCookies.txt'):
            return pwd + 'JDCookies.txt'
        elif os.path.exists('/ql/config/env.sh'):
            print("当前环境青龙面板新版")
            return '/ql/config/env.sh'
        elif os.path.exists('/ql/config/cookie.sh'):
            print("当前环境青龙面板旧版")
            return '/ql/config/env.sh'
        elif os.path.exists('/jd/config/config.sh'):
            print("当前环境V4")
            return '/jd/config/config.sh'
        elif os.path.exists(pwd + 'JDCookies.txt'):
            return pwd + 'JDCookies.txt'
        return pwd + 'JDCookies.txt'

    # 获取cookie
    def getCookie(self):
        global cookies
        ckfile = self.getckfile()
        try:
            if os.path.exists(ckfile):
                with open(ckfile, "r", encoding="utf-8") as f:
                    cks = f.read()
                    f.close()
                if 'pt_key=' in cks and 'pt_pin=' in cks:
                    r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
                    cks = r.findall(cks)
                    if len(cks) > 0:
                        if 'JDCookies.txt' in ckfile:
                            print("当前获取使用 JDCookies.txt 的cookie")
                        cookies = ''
                        for i in cks:
                            cookies += i
                        return
            else:
                with open(pwd + 'JDCookies.txt', "w", encoding="utf-8") as f:
                    cks = "#多账号换行，以下示例：（通过正则获取此文件的ck，理论上可以自定义名字标记ck，也可以随意摆放ck）\n账号1【Curtinlv】cookie1;\n账号2【TopStyle】cookie2;"
                    f.write(cks)
                    f.close()
            if "JD_COOKIE" in os.environ:
                if len(os.environ["JD_COOKIE"]) > 10:
                    cookies = os.environ["JD_COOKIE"]
                    print("已获取并使用Env环境 Cookie")
        except Exception as e:
            print(f"【getCookie Error】{e}")

    # 检测cookie格式是否正确
    def getUserInfo(self, ck, pinName, userNum):
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
            resp = requests.get(url=url, verify=False, headers=headers, timeout=60).text
            r = re.compile(r'GetJDUserInfoUnion.*?\((.*?)\)')
            result = r.findall(resp)
            userInfo = json.loads(result[0])
            nickname = userInfo['data']['userInfo']['baseInfo']['nickname']
            return ck, nickname
        except Exception:
            context = f"账号{userNum}【{pinName}】Cookie 已失效！请重新获取。"
            print(context)
            return ck, False

    def iscookie(self):
        """
        :return: cookiesList,userNameList,pinNameList
        """
        cookiesList = []
        userNameList = []
        pinNameList = []
        if 'pt_key=' in cookies and 'pt_pin=' in cookies:
            r = re.compile(r"pt_key=.*?pt_pin=.*?;", re.M | re.S | re.I)
            result = r.findall(cookies)
            if len(result) >= 1:
                print("您已配置{}个账号".format(len(result)))
                u = 1
                for i in result:
                    r = re.compile(r"pt_pin=(.*?);")
                    pinName = r.findall(i)
                    pinName = unquote(pinName[0])
                    # 获取账号名
                    ck, nickname = self.getUserInfo(i, pinName, u)
                    if nickname != False:
                        cookiesList.append(ck)
                        userNameList.append(nickname)
                        pinNameList.append(pinName)
                    else:
                        u += 1
                        continue
                    u += 1
                if len(cookiesList) > 0 and len(userNameList) > 0:
                    return cookiesList, userNameList, pinNameList
                else:
                    print("没有可用Cookie，已退出")
                    exit(3)
            else:
                print("cookie 格式错误！...本次操作已退出")
                exit(4)
        else:
            print("cookie 格式错误！...本次操作已退出")
            exit(4)
getCk = getJDCookie()
getCk.getCookie()

if "qjd_zlzh" in os.environ:
    if len(os.environ["qjd_zlzh"]) > 1:
        qjd_zlzh = os.environ["qjd_zlzh"]
        qjd_zlzh = qjd_zlzh.replace('[', '').replace(']', '').replace('\'', '').replace(' ', '').split(',')
        print("已获取并使用Env环境 qjd_zlzh:", qjd_zlzh)


def getShareCode(ck):
    global aNum
    try:
        v_num1 = ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)) + ''.join(random.sample(string.digits, 4))
        url = 'https://api.m.jd.com/client.action?functionId=signBeanGroupStageIndex&body=%7B%22monitor_refer%22%3A%22%22%2C%22rnVersion%22%3A%223.9%22%2C%22fp%22%3A%22-1%22%2C%22shshshfp%22%3A%22-1%22%2C%22shshshfpa%22%3A%22-1%22%2C%22referUrl%22%3A%22-1%22%2C%22userAgent%22%3A%22-1%22%2C%22jda%22%3A%22-1%22%2C%22monitor_source%22%3A%22bean_m_bean_index%22%7D&appid=ld&client=apple&clientVersion=null&networkType=&osVersion=&uuid=&jsonp=jsonp_' + str(int(round(t * 1000))) + '_' + v_num1
        head = {
            'Cookie': ck,
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Referer': 'https://h5.m.jd.com/rn/3MQXMdRUTeat9xqBSZDSCCAE9Eqz/index.html?has_native=0',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'api.m.jd.com',
            'User-Agent': 'Mozilla/5.0 (iPhone CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
            'Accept-Language': 'zh-cn'
        }
        resp = requests.get(url=url, headers=head, verify=False, timeout=30).text
        r = re.compile(r'jsonp_.*?\((.*?)\)\;', re.M | re.S | re.I)
        result = r.findall(resp)
        jsonp = json.loads(result[0])
        try:
            groupCode = jsonp['data']['groupCode']
            shareCode = jsonp['data']['shareCode']
            sumBeanNumStr = int(jsonp['data']['sumBeanNumStr'])
        except:
            if aNum < 5:
                aNum += 1
                return getShareCode(ck)
            else:
                groupCode = 0
                shareCode = 0
                sumBeanNumStr = 0
                aNum = 0
        aNum = 0
        return groupCode, shareCode, sumBeanNumStr
    except Exception as e:
        print(f"getShareCode Error", e)

def helpCode(ck, groupCode, shareCode,u, unum, user):
    try:
        v_num1 = ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1)) + ''.join(random.sample(string.digits, 4))
        headers = {
            'Cookie': ck,
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Referer': f'https://h5.m.jd.com/rn/42yjy8na6pFsq1cx9MJQ5aTgu3kX/index.html?jklActivityId=115&source=SignSuccess&jklGroupCode={groupCode}&ad_od=1&jklShareCode={shareCode}',
            'Accept-Encoding': 'gzip, deflate, br',
            'Host': 'api.m.jd.com',
            'User-Agent': UserAgent,
            'Accept-Language': 'zh-cn'
        }
        url = 'https://api.m.jd.com/client.action?functionId=signGroupHelp&body=%7B%22activeType%22%3A2%2C%22groupCode%22%3A%22' + str(groupCode) + '%22%2C%22shareCode%22%3A%22' + shareCode + f'%22%2C%22activeId%22%3A%22115%22%2C%22source%22%3A%22guest%22%7D&appid=ld&client=apple&clientVersion=10.0.4&networkType=wifi&osVersion=13.7&uuid=&openudid=&jsonp=jsonp_{int(round(t * 1000))}_{v_num1}'
        resp = requests.get(url=url, headers=headers, verify=False, timeout=30).text
        r = re.compile(r'jsonp_.*?\((.*?)\)\;', re.M | re.S | re.I)
        result = r.findall(resp)
        jsonp = json.loads(result[0])
        helpToast = jsonp['data']['helpToast']
        pageFlag = jsonp['data']['pageFlag']
        if pageFlag == 0:
            print(f"账号{unum}【{u}】助力失败! 原因：{helpToast}")
            if '满' in helpToast:
                print(f"## 恭喜账号【{user}】团已满，今日累计获得160豆")
                return True
            return False
        else:
            if '火' in helpToast:
                print(f"账号{unum}【{u}】助力失败! 原因：{helpToast}")
            else:
                print(f"账号{unum}【{u}】{helpToast} , 您也获得1豆哦~")
            return False
    except Exception as e:
        print(f"helpCode Error ", e)

def start():
    print("### 全民抢京豆-助力 ###")
    global cookiesList, userNameList, pinNameList, ckNum, beanCount, userCount
    cookiesList, userNameList, pinNameList = getCk.iscookie()
    for ckname in qjd_zlzh:
        try:
            ckNum = userNameList.index(ckname)
        except Exception as e:
            try:
                ckNum = pinNameList.index(ckname)
            except:
                print(f"请检查被助力账号【{ckname}】名称是否正确？提示：助力名字可填pt_pin的值、也可以填账号名。")
                continue

        print(f"### 开始助力账号【{userNameList[int(ckNum)]}】###")
        groupCode, shareCode, sumBeanNumStr = getShareCode(cookiesList[ckNum])
        if groupCode == 0:
            print(f"## {userNameList[int(ckNum)]}  黑号？？？？")
            continue
        u = 0
        for i in cookiesList:
            result = helpCode(i, groupCode, shareCode,userNameList[u], u+1, userNameList[int(ckNum)])
            time.sleep(sleepNum)
            if result:
                break
            u += 1
        groupCode, shareCode, sumBeanNumStr = getShareCode(cookiesList[ckNum])
        userCount[f'{userNameList[ckNum]}'] = sumBeanNumStr
        beanCount += sumBeanNumStr
    print("\n-------------------------")
    for i in userCount.keys():
        print(f"账号【{i}】已抢京豆: {userCount[i]}")
    print(f"## 今日累计获得 {beanCount} 京豆")


if __name__ == '__main__':
    start()