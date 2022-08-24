from csv import list_dialects
import requests
import json
import random

url = 'https://bmigucitic.cmread.com:8517/migu-bportal/book/bookwall/getEBookCategoryInfoList?MmEwMD=3MhlCLhfOiBwz0JW4OCRuQ6E7wLbb73g67vrVRweJRj24_U8FWfk3vvRvcQzxBlRutSlLClDFy.NY419FwZbld4bPSHYmWWSD46VXEXH8dos5Irs2814heWqiLG4GMVy0ukpyzw3_GufPADphnDPYadZ2fuiGigI6yc2RReLBDbRUGEp375YRY7YcLeFDmzd7QMNxEz4HOmxiYcjsFbJnRN2jHgCiKqU8DHHekWHKtY.kUEbCIpih6fQKGESrfk3xlaWwoUymSxRiBwtQbjDzVwTjKEvQPN75jf2nAWcJqrdQi0Q9dJfKy1ZamUhtUWfHkHo'

header = {
    'Host': 'bmigucitic.cmread.com:8517',
    'clientVersion': '7.4.0',
    'IP': '192.168.31.165',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148_CMREAD_iPhone_Appstore_Zhongxin_1170*2532_7.4.0(1170*2532;Apple;iPhone13,2;iOS 14.8.1;zh_CN;)',
    'Referer': 'https://bmigucitic.cmread.com:8517/zxHtml/html/dist/index.html',
    'cltk': 'I35ydM4v5+nZzpZgFIZfyA7g0f0lFnfA5kFKSmEy8UBHAsFJCZuRAznjNJ6AOxPd',
    'Cookie': 'JSESSIONID=D79C2FD1A307E3730BC178B998D00D27; Client-Agent=CMREADBC_iPhone_WH_Zhongxin_V7.4.0_220506/640*960/Viva_MEB; FSSBBIl1UgzbN7N8517S=yo2ZfxDRhPqurnnKia4FDepUV82_fPRS0s8lkZx1QHoKDugfp6M8YXyNEvScWtFN; FSSBBIl1UgzbN7N8517T=3Rh95jhr.WBe2CJ7ufCy486L9ILDXX33dXvfQMwwmMjmugU51ifOA2vyBqQJrzly4ES9G0lb14.xwy1l1IZDWe4DjwpTHwQOmPbmeuYfW3aY0rVww.lhbZqAngz6K77qfUkSvUvR2tQgi2lEMNbR8nlHWswwT9rLPw9hWbda7HLz0nMlPTwnqss_kt9_xmLIClGVoCv3ARc8BdGEEtBCYXbN4Y_hgz.PN4n.r9aqgPzTmKCU9dB41PeTdjYDgUp3ER0Z; bearType=WLAN; cltk=I35ydM4v5+nZzpZgFIZfyA7g0f0lFnfA5kFKSmEy8UBHAsFJCZuRAznjNJ6AOxPd; cookieId=IoDhvdgGZ3h0YfgoHYEwGpfKHFyLiFz1660293780509; mobile_ip=192.168.31.165; msisdn=RpNbjKu7uFhpmICuze31xA==; terminalUniqueId=-1; tokenId=fae6a3d8c7e7fbe3da49214ac1243433; userID=325ef7f0a499cfac77ccffeb52514107; version=7.4.0; x-api-version=1; x-random=8752; x-tptoken=haVH1BpkcCKsQbTXJt3ZBgQFHlE5PDLmRY9CgJA3OxoaRENdb4e+OtB9tRduNZpO; x-user-id=325ef7f0a499cfac77ccffeb52514107; zxUserId=325ef7f0a499cfac77ccffeb52514107; JSESSIONID=878C1FF4572C2B4097A7CC1A1C825347; _at=frOFPTmPr8E6Wm8Huld0ADnKGHhF59UG5doqt/ezoSo=; _clientid=11f950fea63b85a5efbfe01ecf98f89a; _ts=1661084588588; mg_uem_user_id_3f0df028a2f04d65abb6a70f59abe00b=c4884838-fc2c-4301-949a-b90824b71a20; mg_uem_user_id_12138b841f624615ada047dae881a8d9=07b3a321-8fec-4042-9cde-6262187f0bff',
    'UserID': '325ef7f0a499cfac77ccffeb52514107',
    'terminalUniqueId': '-1',
    'bearType': 'WLAN',
    'x-tptoken': 'haVH1BpkcCKsQbTXJt3ZBgQFHlE5PDLmRY9CgJA3OxoaRENdb4e+OtB9tRduNZpO',
    'Origin': 'https://bmigucitic.cmread.com:8517',
    'Content-Length': '57',
    'TokenID': 'fae6a3d8c7e7fbe3da49214ac1243433',
    'Connection': 'keep-alive',
    'CpID': '1',
    'Client-Agent': 'CMREADBC_iPhone_WH_Zhongxin_V7.4.0_220506/640*960/Viva_MEB',
    'Dev-Resolution': '390*844',
    'x-random': '8752',
    'Accept-Language': 'zh-cn',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json; charset=UTF-8',
    'x-tokenId': 'undefined',
    'x-api-version': '1',
    'msisdn': 'RpNbjKu7uFhpmICuze31xA==',
    'Accept-Encoding': 'gzip, deflate, br',  
}

shoppeIds = ['590610026', '590610027', '590610028', '590610029']
shoppeId = random.choice(shoppeIds)

body = {
    "shoppeId" : f"{shoppeId}",
    "pageIndex" : 1,
    "type" : 1,
    "count" : 19
}

resp = requests.post(url=url, headers=header, data=json.dumps(body)).json()
ids = []
names = []
for i in resp['data']['ebookList']:
    ebookId = i['ebookId']
    ebookName = i['ebookName']
    ids.append(ebookId)
    names.append(ebookName)
#print(f'多个列表为：' + str(lsts))
ebookId = random.choice(ids)
namebookNamee = random.choice(names)
# print(f'随机抽取书名为：' + str(ebookName) + f'，随机抽取ID为：' + str(ebookId))

# url2 = 'https://cmigucitic.cmread.com:8511/migu-cportal/book/bookcase/getSystemBookmark?bookId=581966053'
# resp2 = requests.get(url=url2, headers=header).json()
# print(url2)


# 获取章节id
url2 = 'https://cmigucitic.cmread.com:8511/migu-cportal/book/bookread/getEBookDetailNew'

body2 = {
    "ebookId":f'{ebookId}'
}
resp2 = requests.post(url=url2, headers=header, data=json.dumps(body2)).json()
chapterID = resp2['data']['chapterID']
print(chapterID)

# 读书细节
url3 = 'https://cmigucitic.cmread.com:8511/v1/interaction-facade/bookRead/putReadBookInfo'
body3 = {
  "readList" : [
    {
      "startTime" : "20220823190346",
      "bookId" : f'{ebookId}',
      "endTime" : "20220823191014",
      "type" : "1"
    },
    {
      "startTime" : "20220823185747",
      "bookId" : f'{ebookId}',
      "endTime" : "20220823185854",
      "type" : "1"
    },
    {
      "startTime" : "20220823185854",
      "bookId" : f'{ebookId}',
      "endTime" : "20220823190346",
      "type" : "1"
    }
  ]
}
resp3 = requests.post(url=url3, headers=header, data=json.dumps(body3)).json()
print(resp3)

url4 = 'https://cmigucitic.cmread.com:8511/migu-cportal/book/bookcase/addSystemBookmark'
body4 = [
    {
        "ebookId" : f"{ebookId}",
        "chapterId" : f"{chapterID}",
        "offset" : "609"
    },
    {
        "ebookId" : f"{ebookId}",
        "chapterId" : f"{chapterID}",
        "offset" : "0"
    },
    {
        "ebookId" : "591066163",
        "chapterId" : f"{chapterID}",
        "offset" : "601"
    },
]
resp4 = requests.post(url=url4, headers=header, data=json.dumps(body4)).json()
print(resp4)

# url5 = 'https://cmigucitic.cmread.com:8511/migu-cportal/book/bookcase/addSystemBookmark'
# body5 = {
#     "ebookId":f'{lst}'
# }
# resp5 = requests.post(url=url5, headers=header, data=json.dumps(body5)).json()
# print(resp5)
