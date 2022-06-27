# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/23 19:06
# @File : okline_spider.py
# @SoftWare : Pycharm

"""
请求头加密:x-apikey
关键字搜索 通过js源文件进行断点调试
找到主题函数 缺啥找啥
可以通过python模拟实现
也可以通过执行js代码实现
"""
import time
import random
import base64
from requests_html import HTMLSession

class OklineSpider:
    def __init__(self):
        self.session = HTMLSession()
        self.url = 'https://www.oklink.com/api/explorer/v1/btc/transactionsNoRestrict?'

    def get_x_apikey(self):
        """根据JS源码用python实现"""
        t = int(time.time()*1000)
        t1 = str(1 * t + 1111111111111)
        r = str(random.randint(0,9))
        n = str(random.randint(0,9))
        o = str(random.randint(0,9))
        new_t = t1 + r + n + o

        API_KEY = 'a2c903cc-b31e-4547-9299-b6d07b7631ab'
        key1 = API_KEY[:8]
        key2 = API_KEY[8:]
        new_key = key2 + key1

        res = new_key + '|' + new_t
        # 要对数据进行base64编码
        x_apikey = base64.b64encode(res.encode()).decode()

        self.get_response(x_apikey)

    def get_response(self,x_apikey):
        """请求接口，获取响应"""
        headers = {
            'Cookie': 'locale=zh_CN; _okcoin_legal_currency=CNY; aliyungf_tc=2bf06da85ffb691c7a15030758d4a8f724d4fa23a085a83ce8e397597917edc6; Hm_lvt_5244adb4ce18f1d626ffc94627dd9fd7=1655799134,1655822308,1655979457; first_ref=https%3A%2F%2Fwww.oklink.com%2Fzh-cn%2Fbtc%2Ftx-list%3Flimit%3D20%26pageNum%3D1; Hm_lpvt_5244adb4ce18f1d626ffc94627dd9fd7=1655989804',
            'devId': '9e4f8235-4597-49f7-bb24-a2e7985ba934',
            'Host': 'www.oklink.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.oklink.com/zh-cn/btc/tx-list?limit=20&pageNum=2',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
            'x-apiKey': x_apikey,}
        for page in range(11):
            params = {
                't': int(time.time()*1000),
                'limit': 20,
                'offset': page * 20
            }
            response = self.session.get(self.url,params=params,headers=headers).json()
            self.parse_data(response)
            time.sleep(1)

    def parse_data(self,response):
        for res in response['data']['hits']:
            transaction_hash = res['hash']
            block = res['blockHeight']
            realTransferValue = res['realTransferValue']
            print(transaction_hash,block,realTransferValue)

if __name__ == '__main__':
    Okline = OklineSpider()
    Okline.get_x_apikey()