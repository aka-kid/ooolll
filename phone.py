#-- coding: utf-8 --
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
import requests

# pushplus推送
token = '3b160e2b7e3c462daeb2e7f344202da9' #在pushplus网站中可以找到
# title= '测试' #改成你要的标题内容
# content ='哈哈哈哈或' #改成你要的正文内容
# msg_url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
# requests.get(url)

url = "https://wx.10086.cn/website/nrapigate/businessOnline/api/normData?id=20220616094547826201049"
header = {
    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE4MDAsInRpbWVTcGFuIjoxNjU4NDYzOTA5NTE2LCJhdXRoVG9rZW4iOiJiZjgyMDY0Ny05ZWUyLTRiNTctOTU4Yy04OWEwYWViNTZmOGYifQ.zrxbx7GN7MSrKI8y5GwAAuoKsa9sYt2RStakYjgHckA",
    "Content-Type": "application/json; charset=utf-8",
    "Cookie": "d.sid=YUfZhP2aQo2v1cRmsGDYFcJa-_kf-rC5; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22dQBujss%22%2C%22first_id%22%3A%22175307bfbae2c9-0068d7a95d916d8-7e652e12-304704-175307bfbafac8%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22175307bfbae2c9-0068d7a95d916d8-7e652e12-304704-175307bfbafac8%22%7D; TY_SESSION_ID=4285a06e-d4ea-4896-95fc-aa92730a5ecd; grayscale=huaian;",
    "Referer": "https://wx.10086.cn/website/businessOnline/shopDetail?productCode=20220616094547826201049&fromRecommend=3&pageSource=100&pageid=ad2bb7dc62bf4cc98d5b2380a0bc2b84&shopP=100",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    }
resp = requests.get(url=url, headers=header)
dic = resp.json()
stock = int(dic['bean']['normList'][0]['stock'])
if stock != 11:
    title= '库存变化' #改成你要的标题内容
    content ='库存变化！' #改成你要的正文内容
    msg_url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
    requests.get(msg_url)
    print("库存变化!!!")
else:
    title= '库存无变化' #改成你要的标题内容
    content ='库存无变化！' #改成你要的正文内容
    msg_url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
    requests.get(msg_url)
    print("库存无变化!!!")

