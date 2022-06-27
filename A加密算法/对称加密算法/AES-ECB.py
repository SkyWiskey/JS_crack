# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/19 0:02
# @File : AES-ECB.py
# @SoftWare : Pycharm

"""
AES加密只接受bytes类型数据
秘钥必须为16字节或者16字节的倍数的字节型数据。
明文必须为16字节或者16字节的倍数的字节型数据，如果不够16字节需要进行补全，
一个字符串，你可以直接使用 encode()函数 将其转换为 bytes类型数据。
"""
from Crypto.Cipher import AES

def AES_ECB():
    # 秘钥，b就是表示为bytes类型
    password = b'1234567812345678'
    # 需要加密的内容，bytes类型
    text = b'abcdefghijklmnhi'
    print('原文：',text)
    # 创建一个aes对象 传入密钥和加密模式
    aes = AES.new(password,AES.MODE_ECB)  # AES.MODE_ECB 表示模式是ECB模式
    # 加密明文
    en_text = aes.encrypt(text)
    # 加密明文，bytes类型
    print("密文：",en_text)

    # 解密密文
    den_text = aes.decrypt(en_text)
    print("明文：",den_text)

if __name__ == '__main__':
    AES_ECB()