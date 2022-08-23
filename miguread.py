#-- coding: utf-8 --#
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests
import json
import random
import time
from datetime import datetime

"""
咪咕阅读
8.22 加入随机获取书籍逻辑
8.23 修正随机获取书籍逻辑
"""

# header 固定数据
header = {"Accept": "*/*","Accept-Encoding": "gzip,deflate","Accept-Language": "zh-CN,zh;q=0.8","Action": "putListenBookPlayInfo","Cache-Control": "no-cache","Client-Agent": "CMREADBC_iPhone_WH_Zhongxin_V7.4.0_220506/640*960/Viva_MEB","Client_Agent": "CMREADBC_iPhone_WH_Zhongxin_V7.4.0_220506/640*960/Viva_MEB","Connection": "close","Content-Length": "123","Content-Type": "application/json","Cookie": "JSESSIONID=570990A1CE81F90DCFBE6DE89E282790; JSESSIONID=4DCB21A484E27B3DE1AA1C3643B3A5EF; JSESSIONID=E965B589CEBEDBF6ED55C064510B930B; _at=pSYjd8tojEnn4XRP0Lx8RjN4WZo1YYgTl216ZCY2ltM=; _clientid=dd9b9651784554b5c186f6555ac763dc; _ts=1656334237841","CpID": "1","Dev-Resolution": "390*844","Host": "cmigucitic.cmread.com:8511","IP": "192.168.1.4","Pragma": "no-cache","TokenID": "3f899d6cbb5c2ffc4d12d704d9504074","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148_CMREAD_iPhone_Appstore_Zhongxin_1170*2532_7.4.0(1170*2532;Apple;iPhone13,2;iOS 14.8.1;zh_CN;)","UserID": "325ef7f0a499cfac77ccffeb52514107","X-Channel-Code": "00000000","appVersion": "7.4.0","brand": "iOS","cltk": "D2ubBTQvZoqZaUhoW0YEDlwGuX4uN6z6nRLnMf3tj5amOqUu6aNbcoVp/NVk6eW+","model": "iPhone 12","osVersion": "IOS14.80","terminalUniqueId": "-1","version": "7.4.0","x-api-version": "1","x-cmread-login-type": "3","x-cmread-msisdn": "RpNbjKu7uFhpmICuze31xA==","x-random": "8829","x-tptoken": "haVH1BpkcCKsQbTXJt3ZBi4DmEJncIZqdHrQ333MjpdrU3HiVvNOiDONADuQhw7L","x-up-bear-type": "WLAN","x-user-id": "325ef7f0a499cfac77ccffeb52514107","zx-client-token": "A5COHczRvoPqAgKWbO3IMxiiHyi85wktPXGIVGLCYMAbU6ID7U35FKymSxxOWhiP"}

# 阅读分享任务
def share():
    url = "https://cmigucitic.cmread.com:8511/v1/interaction-facade/happiness/shareCallBack"
    body = {
        "shareType":"29"
    }
    resp1 = requests.post(url, headers=header, data=json.dumps(body)).json()
    if resp1['code'] == '200':
        print(f'分享任务结果:' + str(resp1['msg']))
    else:
        print(f'分享任务结果:' + str(resp1['msg']))
    t = random.randint(1,11)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    bookid()

# 获取阅读电子书id
def bookid():
    global idlsit, namelist
    url = 'https://bmigucitic.cmread.com:8517/migu-bportal/book/bookwall/getEBookCategoryInfoList?MmEwMD=3MhlCLhfOiBwz0JW4OCRuQ6E7wLbb73g67vrVRweJRj24_U8FWfk3vvRvcQzxBlRutSlLClDFy.NY419FwZbld4bPSHYmWWSD46VXEXH8dos5Irs2814heWqiLG4GMVy0ukpyzw3_GufPADphnDPYadZ2fuiGigI6yc2RReLBDbRUGEp375YRY7YcLeFDmzd7QMNxEz4HOmxiYcjsFbJnRN2jHgCiKqU8DHHekWHKtY.kUEbCIpih6fQKGESrfk3xlaWwoUymSxRiBwtQbjDzVwTjKEvQPN75jf2nAWcJqrdQi0Q9dJfKy1ZamUhtUWfHkHo'
    shoppeIds = ['590610026', '590610027', '590610028', '590610029']    # 店铺页面的四个ID
    shoppeId = random.choice(shoppeIds) # 随机获取3个店铺ID
    # 随机获取店铺ID后，将参数传入body中，之后获取该分类下的书籍ID
    body = {
        "shoppeId" : f"{shoppeId}",
        "pageIndex" : 1,
        "type" : 1,
        "count" : 100
    }
    resp = requests.post(url=url, headers=header, data=json.dumps(body)).json()
    idlists = []
    namelists = []
    for i in resp['data']['ebookList']:
        ebookId = i['ebookId']  # 书籍ID
        ebookName = i['ebookName']  # 书籍名称
        idlists.append(ebookId)      # 将书籍ID加入列表
        namelists.append(ebookName)      # 将书籍名称加入列表
    idlsit = random.choice(idlists)  # 随机选择一个ID
    namelist = random.choice(namelists)    # 随机选择一个书名
    readEbook()

# 阅读电子书任务
def readEbook():
    url = "https://cmigucitic.cmread.com:8511/v1/interaction-facade/bookRead/putReadBookInfo"
    # 阅读开始时间
    now_time = datetime.now()
    # datetime转字符串
    sTime = now_time.strftime('%Y%m%d%H%M%S') 
    t = random.randint(5,17)  # 随机时间操作
    time.sleep(t)
    now_time = datetime.now()
    # 阅读结束时间
    eTime = now_time.strftime('%Y%m%d%H%M%S') 
    t = random.randint(2,11)  # 随机时间操作
    time.sleep(t)
    body = {
        "readList": [
            {
                "startTime": f"{sTime}",
                "bookId": f"{idlsit}",
                "endTime": f"{eTime}",
                "type": "1"
            }
        ]
    }
    resp = requests.post(url, headers=header, data=json.dumps(body)).json()
    print(f'阅读任务结果：' + str(resp['msg']) + f'\n已阅读书籍名称：' + str(namelist) + f'，已阅读书籍ID：' +str(idlsit) )
    t = random.randint(1,7)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    ebookid()

# 获取听书电子书id
def ebookid():
    global idlst, namelst
    url = 'https://bmigucitic.cmread.com:8517/migu-bportal/book/listenBook/getCatalogInfoAndListenBookListByCatalogId?MmEwMD=3zPjIXukom5LQYS8lY11FQ3YZUw_KMMj2ZnTAwfyEHKM48JX8FZlGtmQgGZjvH3nW3en_PcvshtKoNpWi86VV..I.oL3Ap02P8uXHsZWlnmmWxf7xFgp1PqfGO_uOa4E7vrGA9haiab26XlCWenwtRCkjN3fcBTZIrJqW0FeZDbTrJoPfLEjLfKvxUecPIsafVokM6gK51Pdi49K3rPekBoWbawAmubT3ZG0V4PKAXlKhr8N_eGnuOn1OCcR46w_EmgQVl7E1A1vc9sHbCmNh2R.gGq.Kskrnc6b4cW_pct8Ewz.xXcaPKRtq3n7JbNj7fuO'
    # catalogIds = ['590610021']    # 店铺页面的四个ID
    # catalogId = random.choice(catalogIds)    # 随机获取一个店铺ID
    # # 随机获取店铺ID后，将参数传入body中，之后获取该分类下的书籍ID
    body = {
        "catalogId" : 590610021,
        "pageIndex" : 1,
        "type" : 2,
        "pageSize" : 100
    }
    resp = requests.post(url=url, headers=header, data=json.dumps(body)).json()
    idlsts = []
    namelsts = []
    for i in resp['data']['listenBookList']:
        smuBookId = i['smuBookId']      # 书籍ID
        listenBookName = i['listenBookName']    # 书籍名称
        idlsts.append(i['smuBookId'])      # 将书籍ID加入列表
        namelsts.append(i['listenBookName'])    # 将书籍名称加入列表
    idlst = random.choice(idlsts)  # 随机选择一个ID
    namelst = random.choice(namelsts)  # 随机选择一个书名
    listen()

#  听书任务
def listen():
    url = "https://cmigucitic.cmread.com:8511/v1/interaction-facade/bookRead/putReadBookInfo"
    # 阅读开始时间
    now_time = datetime.now()
    # datetime转字符串
    sTime = now_time.strftime('%Y%m%d%H%M%S') 
    t = random.randint(1,11)  # 随机时间操作
    time.sleep(t)
    # 阅读结束时间
    eTime = now_time.strftime('%Y%m%d%H%M%S') 
    t = random.randint(7,18)  # 随机时间操作
    time.sleep(t)
    body = {
            "readList": [
                {
                    "startTime": f"{sTime}",
                    "bookId": f"{idlst}",
                    "endTime": f"{eTime}",
                    "type": "2"
                }
            ]
        }
    resp = requests.post(url, headers=header, data=json.dumps(body)).json()
    print(f'听书任务结果：' + str(resp['msg']) + f'\n已听书籍名称：' + str(namelst)+ f'，已听书籍ID：'+str(idlst))
    t = random.randint(4,17)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)

def main():
    share()

if __name__ == '__main__':
    main()
