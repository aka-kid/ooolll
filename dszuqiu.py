import requests
from datetime import datetime

def sign():
    resp = requests.get(url=sign_url, headers=header).json()
    print(f'签到结果:' + str(resp['result']) + f'，本次新增积分:' + str(resp['jifen_added']) )
    resp2 =requests.get(url=sign_url2, headers=header).json()
    print(f'累计签到:' + str(resp2['total'])  + "天")

def share():
    resp = requests.get(url=share_url, headers=header).json()
    if resp['status'] == 200:
        print(f'\n分享结果:' + str(resp['result']))
        print(f'分享新增积分:' + str(resp['jifen_added']))
    else:
        print(f'\n分享结果: 已分享')

def add():
    resp = requests.get(url=add_url, headers=header).json()
    print(f'\n累计奖励积分:' + str(resp['jifen_added'])  + "分")

def main():
    sign()
    share()
    add()

if __name__ == '__main__':
    # 当前日期和时间
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    # 通用token和header
    token = "358152-a1425d73234aff52f5335de03de36f8f"
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
        "Connection": "keep-alive",
        "Host": "api.dszuqiu.com",
        "User-Agent": "DSZuQiu/1.0.2 (iPhone; iOS 14.8.1; Scale/3.00)",
        "X-APP-BRANCH": "1",
        "X-APP-DEVICE": "60FD608D-05C5-440D-9A27-A8A9E4547C2F",
        "X-APP-PUSH": "2","X-APP-TYPE": "1",
        "X-APP-VERSION": "102",
        "X-DEVICE-ID": ""
        }
    # 签到url（获取积分）
    sign_url = f"https://api.dszuqiu.com/v9/user/qiandao?request_time={timestamp}&token={token}"
    # 签到url（获取累计签到天数）
    sign_url2 = f"https://api.dszuqiu.com/v9/user/qiandao_days?request_time={timestamp}&token={token}"
    # 分享任务url
    share_url = f"https://api.dszuqiu.com/v6/user/get_jifen_by_task_share_sns?request_time={timestamp}&token={token}"
    # 累计签到url
    add_url = f"https://api.dszuqiu.com/v9/user/qiandao_reward?request_time={timestamp}8&token={token}&type=1"
    main()
