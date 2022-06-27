# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/15 17:28
# @File : AESdemo.py
# @SoftWare : Pycharm

"""
"""
from Crypto.Cipher  import AES
import base64


# 密钥（key）, 密斯偏移量（iv） CBC模式加密

BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

vi = '0102030405060708'

def AES_Encrypt(key, data):
    data = pad(data)
    # 字符串补位
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    encryptedbytes = cipher.encrypt(data.encode('utf8'))
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    encodestrs = base64.b64encode(encryptedbytes)
    # 对byte字符串按utf-8进行解码
    enctext = encodestrs.decode('utf8')
    return enctext


def AES_Decrypt(key, data):
    data = data.encode('utf8')
    encodebytes = base64.decodebytes(data)
    # 将加密数据转换位bytes类型数据
    cipher = AES.new(key.encode('utf8'), AES.MODE_CBC, vi.encode('utf8'))
    text_decrypted = cipher.decrypt(encodebytes)
    # 去补位
    text_decrypted = unpad(text_decrypted)
    text_decrypted = text_decrypted.decode('utf8')
    print(text_decrypted)
    return text_decrypted

if __name__ == '__main__':
    key = '5c44c819appsapi0'

    data = 'herish acorn'
    enctext = AES_Encrypt(key, data)
    print(enctext)

    AES_Decrypt(key, enctext)

