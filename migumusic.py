# -*- coding: utf8 -*-
import requests
import json
import random
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import datetime
'''
2022.6.7
咪咕音乐
'''

# 程序开始时间
begin_time = time.time()

#   分享任务
def share():
    url = 'https://app.u.nf.migu.cn/MIGUM2.0/v1.0/user/share_report.do?bgUrl=https%3A//d.musicapp.migu.cn/prod/file-service/file-down/8121e8df41a5c12f48b69aea89b71dab/98a3767b8e9ca36349e7c2fbcaf8d96f/c2b9d39fa1788a56380118ef30867a6d&des=%E5%BC%A0%E5%9B%BD%E8%8D%A3&ownerId=267&ownerName=%E5%BC%A0%E5%9B%BD%E8%8D%A3&platform=3&resourceId=600919000003994882&resourceName=%E6%88%91%28%E5%9B%BD%E8%AF%AD%29&shareUrl=http%3A//c.migu.cn/00aO7g?ifrom%3D3abf826a07403d19f4ae0f562088ee39&type=2'
    header = {
        'bversionid': 'DF94879092A1A38D629789A5D07F9F759A97BABB939DAABA989684A1B97B9D6EC49788878ED6D88D69C48ED3887A98A39BDFD0D3DDA5A58967A28CB38776A985A8A8818D93A0B48578A59DA6817FA974939B898793B1AA9B66DD879D847997719393818791A0A2856291879D817997719390848791A0A2886291879D8479E3729998888796A4A88C659A8FA2',
        'User-Agent': 'MGMobileMusic/7.9.1 (iPhone; iOS 14.8.1; Scale/3.00)'}
    # proxies_ = {
    #     "http": "http://27.188.19.138:8118"  #  https://uu-proxy.com/api/free
    # }
    n = 0
    while n < second :
        n += 1
        res = requests.post(url=url, headers=header).json()
        print(f'第{n}次分享结果:' + str(res['info']))
        t = random.random()  # 随机时间操作
        print("随机等待->>" + str(t) + "秒\n")
        time.sleep(t)

# #   听歌任务
# def listen():
#     url = "http://app.log.nf.migu.cn/log/tokafka/old_download"
#     # hd = {"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9","Connection": "close","Content-Type": "application/x-www-form-urlencoded","Cookie": "gr_user_id=fcb3d189-2473-4ba6-bf75-f521eccdbaea; mgAppH5CookieId=2051312708-0h94my996af747abd41bc8fc3caebe-1651456186","Host": "app.log.nf.migu.cn","User-Agent": "MGMobileMusic/7.12.0 (iPhone; iOS 14.8.1; Scale/3.00)","bversionid": "DF94879092A1A38D629789A5D07F9F759A97BABB939DAABA989684A1B97B9D6EC49788878ED6D88D69C48ED3887A98A39BDFD0D3DDA5A58967A28CB38776A985A8A8818D93A0B48578A59DA6817FA974939B898793B1AA9B66DD879D847997719393818791A0A2856291879D817997719390848791A0A2886291879D8479E3729998888993A5A38964918F9E","did": "a1122d37caed5cb8930ec2bb61181443","msisdn": "","osVersion": "14.8.1","pkgName": "iOSMigu","sign": "CABDDB38004D1A7267514B5D695972D3","signVersion": "V004","timestamp": "1654225111358","ua": "Ios_migu","uid": "68474fd2-8bf5-4e26-a440-ff57c7f411b8","version": "7.12.0"}
#     # body = {"mgm-network-operators":"01","version":"7.12.0","channel":"0140070","uid":"68474fd2-8bf5-4e26-a440-ff57c7f411b8","brand":"iPhone8Plus","osVersion":"14.8.1","appId":"3DB1BD8559E54390B14A071E9181FD4A","mgm-Network-type":"04","os":"iOS","subchannel":"0140070","platform":"iOS","bversionid":"DF94879092A1A38D629789A5D07F9F759A97BABB939DAABA989684A1B97B9D6EC49788878ED6D88D69C48ED3887A98A39BDFD0D3DDA5A58967A28CB38776A985A8A8818D93A0B48578A59DA6817FA974939B898793B1AA9B66DD879D847997719393818791A0A2856291879D817997719390848791A0A2886291879D8479E3729998888993A5A38964918E9F","language":"zh-Hans-CN","logId":"1654225111.348000","mgm-Network-standard":"01","ua":"Ios_migu"}
#     n = 0
#     while n < second :
#         n += 1
#         resp = requests.post(url=url, headers=header, data=json.dumps(body)).json()
#         print(f'第{n}次听歌结果:' + str(resp['info']))
#         # t = random.random()  # 随机时间操作
#         # print("随机等待->>" + str(t) + "秒\n")
#         # time.sleep(t)

def main():
    share()
    # listen()

def main_handler(event, context):
    return main()

if __name__ == '__main__':
    # 要刷的次数
    second = 200
    # # 用户数据
    # header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate","Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9","Connection": "close","Content-Type": "application/x-www-form-urlencoded","Cookie": "gr_user_id=fcb3d189-2473-4ba6-bf75-f521eccdbaea; mgAppH5CookieId=2051312708-0h94my996af747abd41bc8fc3caebe-1651456186","Host": "app.log.nf.migu.cn","User-Agent": "MGMobileMusic/7.12.0 (iPhone; iOS 14.8.1; Scale/3.00)","bversionid": "DF94879092A1A38D629789A5D07F9F759A97BABB939DAABA989684A1B97B9D6EC49788878ED6D88D69C48ED3887A98A39BDFD0D3DDA5A58967A28CB38776A985A8A8818D93A0B48578A59DA6817FA974939B898793B1AA9B66DD879D847997719393818791A0A2856291879D817997719390848791A0A2886291879D8479E3729998888993A5A38964918F9E","did": "a1122d37caed5cb8930ec2bb61181443","msisdn": "","osVersion": "14.8.1","pkgName": "iOSMigu","sign": "CABDDB38004D1A7267514B5D695972D3","signVersion": "V004","timestamp": "1654225111358","ua": "Ios_migu","uid": "68474fd2-8bf5-4e26-a440-ff57c7f411b8","version": "7.12.0"}
    # body = {"mgm-network-operators":"01","version":"7.12.0","channel":"0140070","uid":"68474fd2-8bf5-4e26-a440-ff57c7f411b8","brand":"iPhone8Plus","osVersion":"14.8.1","appId":"3DB1BD8559E54390B14A071E9181FD4A","mgm-Network-type":"04","os":"iOS","subchannel":"0140070","platform":"iOS","bversionid":"DF94879092A1A38D629789A5D07F9F759A97BABB939DAABA989684A1B97B9D6EC49788878ED6D88D69C48ED3887A98A39BDFD0D3DDA5A58967A28CB38776A985A8A8818D93A0B48578A59DA6817FA974939B898793B1AA9B66DD879D847997719393818791A0A2856291879D817997719390848791A0A2886291879D8479E3729998888993A5A38964918E9F","language":"zh-Hans-CN","logId":"1654225111.348000","mgm-Network-standard":"01","ua":"Ios_migu"}
    # 创建线程池
    with ThreadPoolExecutor(500) as t:
        for i in range(second):
            t.submit(share)
    main()

# 程序结束时间
end_time = time.time()

# 运行时间run_time。round()函数取整
run_time = round(end_time-begin_time)

# 计算时分秒
hour = run_time//3600
minute = (run_time-3600*hour)//60
second = run_time-3600*hour-60*minute

# 输出
print (f'该程序运行时间：{hour}小时{minute}分钟{second}秒')
