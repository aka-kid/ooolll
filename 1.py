import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

import requests
import json
import random


# 页码范围
page = str(random.randint(0,5499))
url = f"https://ranlv.lvfacn.com/api.php/Ranlv/index?access_token=f2e1d57418bb3d6a0439b494f3468a75&category=19&list_rows=1&member_id=1408390&page="+ page +f"&user_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJSYW5sdiBKV1QiLCJpYXQiOjE2NDg2MDE5NTcsImV4cCI6MzI5NzIwMzkxNCwiYXVkIjoiUmFubHYiLCJzdWIiOiJSYW5sdiIsImRhdGEiOnsibWVtYmVyX2lkIjoxNDA4MzkwLCJhdmF0YXIiOiJodHRwOlwvXC9yYW5sdi5sdmZhY24uY29tXC9zdGF0aWNcL21vZHVsZVwvYWRtaW5cL2ltZ1wvZGVmYXVsdF9oZWFkLmpwZyIsIm5pY2tuYW1lIjoiXHU3OTVlXHU5YTZjXHU2MGM1XHU1MWI1IiwibW9iaWxlIjoiMTM5MTEwMjk5MjMiLCJpc19jb3JwIjowfX0.mptkcU-dY6r1vUPKM7mC8hl4OgorPp9GSfZ_3x9u2jQ"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
resp = requests.post(url=url, headers=header)
dic = resp.json()
# 获取一个视频id
for i in dic['data']['data']:
    id = i['id']
    print(id)
