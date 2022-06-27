# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/16 12:26
# @File : BASE64.py
# @SoftWare : Pycharm

"""
Base64是网络上最常见的用于传输8Bit[字节码](https://baike.baidu.com/item/字节码/9953683)的编码方式之一
Base64就是一种基于64个可打印字符来表示[二进制](https://baike.baidu.com/item/二进制/361457)数据的方法
Base64编码是从二进制到字符的过程
可用于在[HTTP](https://baike.baidu.com/item/HTTP)环境下传递较长的标识信息
采用Base64编码具有不可读性，需要解码后才能阅读
"""
import base64

def get_base64():
    keyword = 'HC'
    # 编码
    en_kd = base64.b64encode(keyword.encode()).decode()  #编码后结果：'SEM='
    print(en_kd)

    # 解码
    de_kd = base64.b64decode(en_kd).decode()  # 解码后结果： 'HC' == keyword
    print(de_kd)

if __name__ == '__main__':
    get_base64()
