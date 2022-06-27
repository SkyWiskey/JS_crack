# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/15 17:38
# @File : spider.py
# @SoftWare : Pycharm

"""
1、访问url 获取响应 发现是加密数据
2、根据关键字搜索原生js文件 然后进行调试,知道到加密参数 看它被传给了那个函数他就是主体函数
3、找到主体解密函数 将解密函数复制到js文件中 删除掉JSON.parse 这在python中没有 自己调用json.loads()即可
4、分析主体解密函数 将额外需要用到的js代码也复制到js文件中
5、缺啥找啥 然后补充到js代码中
"""
# pip install PyExecJS
import time

from requests_html import HTMLSession
import json
import execjs
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO,
    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
session = HTMLSession()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
def parse_url():
    url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
    data = {
        'page': 1,
        'num': 20
    }
    resp = session.post(url,headers=headers,data=data).json()
    encrypt_data = resp['encrypt_data']
    encrypt(encrypt_data)

def encrypt(encrypt_data):
    # 读取js文件
    with open('./decryption.js', 'r', encoding='utf8') as f:
        jscode = f.read()

    # 加密数据
    # data = "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"

    # 执行js代码 解密
    ctx = execjs.compile(jscode).call('s', encrypt_data)
    json_data = json.loads(ctx)
    items = []
    for i in json_data['list']:
        items.append(i)
    save_to_csv(items)

def save_to_csv(items):
    for i in items:
        logging.info(f'{i["product"]}========存储成功')
    data = pd.DataFrame(items)
    data.to_csv('chaungyexiangmu.csv',encoding='utf8')

if __name__ == '__main__':
    parse_url()
