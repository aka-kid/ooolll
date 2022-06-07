import requests
import json
import random
import time

"""
咪咕阅读
"""

# header 固定数据
data = {"Accept": "*/*","Accept-Encoding": "gzip,deflate","Accept-Language": "zh-CN,zh;q=0.8","Action": "putReadBookInfo","Cache-Control": "no-cache","Client-Agent": "CMREADBC_iPhone_WH_Zhongxin_V7.4.0_220506/640*960/Viva_MEB","Client_Agent": "CMREADBC_iPhone_WH_Zhongxin_V7.4.0_220506/640*960/Viva_MEB","Connection": "close","Content-Length": "104","Content-Type": "application/json","Cookie": "JSESSIONID=27E31F397714C6E80F46E827DCFA90C9; _at=UTdKSPEoUcmDxtceeeweJki69OGXqbFb4WT5e5Ewkq0=; _clientid=2fa75f307e7266c313b11dfec716b013; _ts=1654219246929","CpID": "1","Dev-Resolution": "390*844","Host": "cmigucitic.cmread.com:8511","IP": "192.168.1.4","Pragma": "no-cache","TokenID": "3f899d6cbb5c2ffc4d12d704d9504074","User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148_CMREAD_iPhone_Appstore_Zhongxin_1170*2532_7.4.0(1170*2532;Apple;iPhone13,2;iOS 14.8.1;zh_CN;)","UserID": "325ef7f0a499cfac77ccffeb52514107","X-Channel-Code": "00000000","appVersion": "7.4.0","brand": "iOS","cltk": "D2ubBTQvZoqZaUhoW0YEDlwGuX4uN6z6nRLnMf3tj5amOqUu6aNbcoVp/NVk6eW+","model": "iPhone 12","osVersion": "IOS14.80","terminalUniqueId": "-1","version": "7.4.0","x-api-version": "1","x-cmread-login-type": "3","x-cmread-msisdn": "RpNbjKu7uFhpmICuze31xA==","x-random": "8829","x-tptoken": "haVH1BpkcCKsQbTXJt3ZBhQZSmeNGXtCOsjezSnUlMiCbzACJMgJgjg18rvVAhfo","x-up-bear-type": "WLAN","x-user-id": "325ef7f0a499cfac77ccffeb52514107","zx-client-token": "A5COHczRvoPqAgKWbO3IMxiiHyi85wktPXGIVGLCYMAbU6ID7U35FKymSxxOWhiP"}

# 阅读分享任务
def share():
    url = "https://cmigucitic.cmread.com:8511/v1/interaction-facade/happiness/shareCallBack"
    body = {
        "shareType":"29"
    }
    resp1 = requests.post(url, headers=data, data=json.dumps(body)).json()
    if resp1['code'] == '200':
        print(f'分享任务结果:' + str(resp1['msg']))
    else:
        print(f'分享任务结果:' + str(resp1['msg']))
    t = random.randint(1,7)  # 随机时间操作
    print("随机等待->>" + str(t) + "秒\n")
    time.sleep(t)

# 阅读电子书3次任务
def readEbook():
    url = "https://cmigucitic.cmread.com:8511/v1/interaction-facade/bookRead/putReadBookInfo"
    # 阅读开始时间
    sTime = "20220603072049"
    # 阅读结束时间
    eTime = "20220603092049"
    # 遍历阅读3本书
    bid = ['590492214','513296696','568930594','590610029','568930594','589390549','591468596','591727483','538928559'] 
    for b_id in bid:
        body = {
                "readList": [
                    {
                        "startTime": f"{sTime}",
                        "bookId": f"{b_id}",
                        "endTime": f"{eTime}",
                        "type": "1"
                    }
                ]
            }
        resp2 = requests.post(url, headers=data, data=json.dumps(body))
        resp = resp2.json()
        print(f'阅读任务结果:' + str(resp['msg']))
        t = random.randint(1,7)  # 随机时间操作
        print("随机等待->>" + str(t) + "秒\n")
        time.sleep(t)

#  听书任务
def listen():
    url = "https://cmigucitic.cmread.com:8511/migu-cportal/book/listenBook/putListenBookPlayInfo"
    body ={
        "smuListenBookId": "662952654",    # 662952654   662953387
        "smuChapterId": "662952666",    #  662952666   662953399
        "startTime": "1653961690395",
        "endTime": "1653968890395", #1653819510620   1653800611408
        "listenType": "1"
    }
    resp3 = requests.post(url, headers=data, data=json.dumps(body)).json()
    print(f'听书任务结果:' + str(resp3['msg']))

def main():
    share()
    readEbook()
    listen()

if __name__ == '__main__':
    main()
