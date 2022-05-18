Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@aka-kid 
aka-kid
/
ooolll
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
ooolll/migu.py /
@aka-kid
aka-kid Add files via upload
Latest commit 497b3be 5 days ago
 History
 1 contributor
36 lines (29 sloc)  1.54 KB
   
# -*- coding: utf8 -*-
import requests
import json
import random
import time

'''
    咪咕音乐
'''

##要刷的次数
second = 10

def share():
    url = 'https://app.u.nf.migu.cn/MIGUM2.0/v1.0/user/share_report.do?bgUrl=https%3A//d.musicapp.migu.cn/prod/file-service/file-down/8121e8df41a5c12f48b69aea89b71dab/ab4e83ef6af4a3e12bc6c1a95a44d30e/5a8534959a19b6c19aaceefa50894be2&des=%E8%94%A1%E4%BE%9D%E6%9E%97&ownerId=99&ownerName=%E8%94%A1%E4%BE%9D%E6%9E%97&platform=3&resourceId=600919000005351409&resourceName=%E6%97%A5%E4%B8%8D%E8%90%BD%28%E7%94%B5%E5%BD%B1%E3%80%8A%E8%AE%B0%E5%BF%86%E7%9A%84%E8%A3%82%E7%97%95%E3%80%8B%E6%8F%92%E6%9B%B2%29&shareUrl=http%3A//c.migu.cn/00dlnc?ifrom%3D8979ed0a69879b200d011c86dcb8d574&type=2'
    header = {
        'bversionid': 'DF94879092A1A28A6B9A89A0D0ADA076989C8890979DD891629784A1B6AF9B6EC4C8888F8ED6D48C6A91B8D08D7C9EA29BDFD0D3DDA5A58967A28CB38776A985A8A8818D93A0B48578A59DA6817FA974939B898793B1AA9B66DD879D847997719393818791A0A2856291879D817997719390848791A0A2886291879D8479E3729998858C97A0A48B63978D9F',
        'User-Agent': 'MGMobileMusic/7.9.1 (iPhone; iOS 14.8.1; Scale/3.00)'}
    n = 0
    while n < second :
        n += 1
        res = requests.post(url=url, headers=header).json()
        print(f'第{n}分享结果:' + str(res['info']))
        t = random.randint(1,2)  # 随机时间操作
        print("随机等待->>" + str(t) + "秒\n")
        time.sleep(t)

def main():
    share()

def main_handler(event, context):
    return main()


if __name__ == '__main__':
    main()
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete
