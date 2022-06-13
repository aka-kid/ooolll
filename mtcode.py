# -*- coding: utf-8 -*-
import json
import requests
import re
import time
from telethon import TelegramClient, events, sync
import os

def get_filename():
    url = 'http://青龙地址/api/logs/?'      # 更改青龙地址
    header = {'Authorization': 'token'}     # 更改token
    res = requests.get(url=url,headers=header).json()
    n = 1
    while n < 100 :
        if str(res['dirs'][n]['name']) == 'passerby-b_mt_fruit_mt_fruit' :
            filename = str(res['dirs'][n]['files'][0])
            url = f'http://青龙地址/api/logs/passerby-b_mt_fruit_mt_fruit/{filename}'
            resp = requests.get(url=url,headers=header).json()
            return resp
        else:
            n +=1


def get_code() :
    code = str(get_filename())
    obj = re.compile(r'/mt_fruit.*,', re.S)
    its = obj.finditer(code)
    for it in its :
        it = it.group()

# 向bot提交互助码
def tg_sign() :
    sign = get_code()
    api_id = [123]  # 输入api_id，一个账号一项
    api_hash = ['abc']  # 输入api_hash，一个账号一项
    session_name = api_id[:]
    for num in range(len(api_id)):
        session_name[num] = "id_" + str(session_name[num])
        client = TelegramClient(session_name[num], api_id[num], api_hash[num])
        client.start(+3) 
        client.send_message("@passerbybbot", "哈哈哈")    # 第一项是机器人ID，第二项是发送的文字
        time.sleep(5)  # 延时5秒，等待机器人回应（一般是秒回应，但也有发生阻塞的可能）
        client.send_read_acknowledge("@akakidBot")  # 将机器人回应设为已读
        print("Done! Session name:", session_name[num])
    os._exit(0)
    print("★★★提交助力码★★★:提交成功!✔")

def main():
    get_filename()
    get_code()
    tg_sign()

def main_handler(event, context):
    return main()

if __name__ == '__main__':
    main()
