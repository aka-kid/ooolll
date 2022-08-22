#-- coding: utf-8 --#
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

"""
咪咕阅读
8.22 加入随机获取书籍ID逻辑
"""

# header 固定数据
header = {XXX}  修改为自己的数据

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
    global ebookId, ebookName
    url = 'https://bmigucitic.cmread.com:8517/migu-bportal/book/bookwall/getEBookCategoryInfoList?MmEwMD=3MhlCLhfOiBwz0JW4OCRuQ6E7wLbb73g67vrVRweJRj24_U8FWfk3vvRvcQzxBlRutSlLClDFy.NY419FwZbld4bPSHYmWWSD46VXEXH8dos5Irs2814heWqiLG4GMVy0ukpyzw3_GufPADphnDPYadZ2fuiGigI6yc2RReLBDbRUGEp375YRY7YcLeFDmzd7QMNxEz4HOmxiYcjsFbJnRN2jHgCiKqU8DHHekWHKtY.kUEbCIpih6fQKGESrfk3xlaWwoUymSxRiBwtQbjDzVwTjKEvQPN75jf2nAWcJqrdQi0Q9dJfKy1ZamUhtUWfHkHo'
    shoppeIds = ['590610026', '590610027', '590610028', '590610029']    # 店铺页面的四个ID
    shoppeId = random.choice(shoppeIds) # 随机获取一个店铺ID
    # 随机获取店铺ID后，将参数传入body中，之后获取该分类下的书籍ID
    body = {
        "shoppeId" : f"{shoppeId}",
        "pageIndex" : 1,
        "type" : 1,
        "count" : 1
    }
    resp = requests.post(url=url, headers=header, data=json.dumps(body)).json()
    for i in resp['data']['ebookList']:
        ebookId = i['ebookId']  # 书籍ID
        ebookName = i['ebookName']  # 书籍名称
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
                "bookId": f"{ebookId}",
                "endTime": f"{eTime}",
                "type": "1"
            }
        ]
    }
    resp = requests.post(url, headers=header, data=json.dumps(body)).json()
    print(f'阅读任务结果：' + str(resp['msg']) + f'\n已阅读书籍名称：' + str(ebookName) + f'，已阅读书籍ID：' +str(ebookId) )
    t = random.randint(1,7)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)
    ebookid()

# 获取听书电子书id
def ebookid():
    global smuBookId, listenBookName
    url = 'https://bmigucitic.cmread.com:8517/migu-bportal/book/listenBook/getCatalogInfoAndListenBookListByCatalogId?MmEwMD=3zPjIXukom5LQYS8lY11FQ3YZUw_KMMj2ZnTAwfyEHKM48JX8FZlGtmQgGZjvH3nW3en_PcvshtKoNpWi86VV..I.oL3Ap02P8uXHsZWlnmmWxf7xFgp1PqfGO_uOa4E7vrGA9haiab26XlCWenwtRCkjN3fcBTZIrJqW0FeZDbTrJoPfLEjLfKvxUecPIsafVokM6gK51Pdi49K3rPekBoWbawAmubT3ZG0V4PKAXlKhr8N_eGnuOn1OCcR46w_EmgQVl7E1A1vc9sHbCmNh2R.gGq.Kskrnc6b4cW_pct8Ewz.xXcaPKRtq3n7JbNj7fuO'
    catalogIds = ['590610022', '590610021']    # 店铺页面的四个ID
    catalogId = random.choice(catalogIds)    # 随机获取一个店铺ID
    # 随机获取店铺ID后，将参数传入body中，之后获取该分类下的书籍ID
    body = {
        "catalogId" : f"{catalogId}",
        "pageIndex" : 1,
        "type" : 2,
        "pageSize" : 1
    }
    resp = requests.post(url=url, headers=header, data=json.dumps(body)).json()
    for i in resp['data']['listenBookList']:
        smuBookId = i['smuBookId']      # 书籍ID
        listenBookName = i['listenBookName']    # 书籍名称
    listen()

#  听书&看视频任务
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
                    "bookId": f"{smuBookId}",
                    "endTime": f"{eTime}",
                    "type": "2"
                }
            ]
        }
    resp = requests.post(url, headers=header, data=json.dumps(body)).json()
    print(f'听书任务结果：' + str(resp['msg']) + f'\n已阅读书籍名称：' + str(listenBookName)+ f'，已阅读书籍ID:'+str(smuBookId))
    t = random.randint(4,17)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)

def main():
    share()

if __name__ == '__main__':
    main()
