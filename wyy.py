# 1、扎到未加密的参数          # windows.arsea(参数,XXX,XXX)
# 2、想办法把参数进行加密（必须参考网易云的逻辑，params = emcText，encSecKey = emcSecKey）
# 3、请求到网络，拿到评论信息
# 需要安装pycrypto

import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json

url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
# 请求方式post
data = {
    "csrf_token": "80660703c249c8955c723d3aecdb3b66",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_29095694",
    "threadId": "R_SO_4_29095694"
}
# 服务于d的
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g = "0CoJUm6Qyw8W8jud"
i = "xGPhSPE1Gvsxhdgt"  # 手动固定，人家函数是随机的

def get_encSecKey():  # 由于i是固定的，那么encSecText就是固定的，c()函数的结果就是固定的
	return "27be8af77a55bd744d6817789665b681cdf18905cd19f0447d9197a61632129719bd89f2d43ca9963db7252c1210086392d8cb4489c6c88c8ad79acb94818c0a604d5c0659826a11d2b4e036f5963d785c3083900c9655db599838fd847825e57917390f5cc9862e32d03733bbc76a0e09099e8969268ac6df82f88d46552604"

# 把参数进行加密
def get_params(data):  # 默认收到的是字符串
    first = enc_params(data,g)
    second = enc_params(first,i)
    return second  # 返回的就是params

# 转化成16的倍数，为下发的算法服务
def to_16(data):
    pad = 16 - len(data) % 16
    data += chr(pad)*pad
    return data

# 加密过程
def enc_params(data,  key):
    IV = "0102030405060708"
    data =to_16(data)
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode('utf-8'), mode=AES.MODE_CBC)  # 创造加密器
    bs = aes.encrypt(data.encode("utf-8"))  # 加密，加密的长度必须为16的倍数
    return (b64encode(bs),"utf-8")  #  转化为字符串返回

# 处理加密过程
""""    function a(a =16) {  # 随机16位字符串
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length, # 取随机数 例如1.234
            e = Math.floor(e),  # 取整 结果1
            c += b.charAt(e);  # 取字母中的XXX位置 结果b
        return c
    }
    function b(a, b) {  # a是要加密的数据
        var c = CryptoJS.enc.Utf8.parse(b)  # c是b，b即为秘钥
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)  # e是数据
          , f = CryptoJS.AES.encrypt(e, c, { # c是加密的秘钥
            iv: d, #  AES中的偏移量
            mode: CryptoJS.mode.CBC  # AES中的加密模式：CBC
        });
        return f.toString()  # 变成字符串返回
    }
    function c(a, b, c) {  # c里面不产生随机数
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {  d: 数据,  e: 010001,   f: 很长,  g : 见上面
        var h = {}  # 空对象
          , i = a(16);   # 16位随机数，把i设置为固定值
        return h.encText = b(d, g), # g也是秘钥  两次加密：数据+g => b => 第一次加密+i => b => params
        h.encText = b(h.encText, i),  # 得到的是 params  i也是秘钥
        h.encSecKey = c(i, e, f),  # 得到的是 encSecKey ，e和f是固定值，如果把i固定，得到的key一定是固定值
        h
    }
    """

# 发送请求，得到结果
resp = requests.post(url, data={
    "params" : get_params(json.dumps(data)),
    "encSecKey" : get_encSecKey()
})

print(resp.text)
