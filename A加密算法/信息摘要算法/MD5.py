# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/16 12:26
# @File : MD5.py
# @SoftWare : Pycharm

import hashlib
"""
MD5是一种信息摘要算法
从一个字符串或文件按照一定规则生成特殊字符串
特点：
1.固定长度128bit的0和1
2.按照4bit32组，每一组按16机制计算数值，字符输出
3.不可逆
4,有可能碰撞
5.长度32
"""
def get_md5(keyword):
    # 创建md5对象
    m = hashlib.md5()
    # 待加密信息 必须encode编码
    m.update(keyword.encode('utf8'))
    # 进行加密
    keyword_md5 = m.hexdigest()

    print(f'MD5加密前：{keyword}')
    print(f'MD5加密后：{keyword_md5}')
    print(f'密文长度：{len(m.hexdigest())}')

    return m.hexdigest()

if __name__ == '__main__':
    keyword = 'wskwsk20000617'
    get_md5(keyword)
