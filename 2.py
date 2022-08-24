from wsgiref import headers
import requests

url = 'https://app.pd.nf.migu.cn/MIGUM3.0/bmw/singer/song/v1.0?pageNo=8&singerId=112&type=1'

header = {
    'Host': 'app.pd.nf.migu.cn',
    'language': 'zh-Hans-CN',
    'User-Agent': 'MGMobileMusic/7.14.0 (iPhone; iOS 14.8.1; Scale/3.00)',
    'Cookie': 'mgAppH5CookieId=4233137390-0c2vy1da7a954e4bfab4621f830f02-1642766905',
    'appId': '3DB1BD8559E54390B14A071E9181FD4A',
    'mgm-network-operators': '02',
    'signVersion': 'V004',
    'randomsessionkey': '1',
    'brand': 'iPhone 12',
    'channel': '0140070',
    'ua': 'Ios_migu',
    'version': '7.14.0',
    'bversionid': 'DF94879092A1A28A6B9A89A0D0ADA076989C8890979DD891629784A1B6AF9B6EC4C8888F8ED6D48C6A91B8D08D7C9EA29BDFD0D3DDB2B488699588AF8C76AA7AA7A981899AB5AA8566978BA481819C82A6A7968BA4A5B88A65DD879D847997719393818791A0A2856291879D817997719390848791A0A2886291879D8479E3729999858A92A3A28E63948EA5',
    'os': 'iOS',
    'subchannel': '0140070',
    'platform': 'iOS',
    'pkgName': 'iOSMigu',
    'uid': 'd9559496-f906-4bf4-ae48-fb480ac937a8',
    'logId': '1661313061.377627',
    'Accept-Language': 'zh-Hans-CN;q=1',
    'mgm-Network-standard': '',
    'mgm-Network-type': '03',
    'osVersion': '14.8.1',
    'timestamp': '1661349943806',
    'sign': 'ACB31ECEC5630691E93DB58FDC02B50E',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'recommendstatus': '1',
}

resp = requests.get(url=url, headers=header).json()

# print(resp)

file = open(r"D:\test.txt", "w")
file.write(resp)
print("存储完毕！！！")
file.close
