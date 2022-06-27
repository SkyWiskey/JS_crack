# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/24 14:16
# @File : mt_spider.py
# @SoftWare : Pycharm

"""
请求参数：_token加密 （二进制压缩）
目前最主要的密码压缩分为二进制压缩(返回数组)和十六进制压缩(返回字节)
关键字搜索 找到源文件 找主题函数
根据函数嵌套 缺啥补啥 最后使用python实现
"""
import time
import base64
import zlib
from requests_html import HTMLSession


class MTSpider:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {
            'Cookie': 'uuid=9ffd2bba19834bad9443.1656047928.1.0.0; _lx_utm=utm_source%3Dbaidu%26utm_medium%3Dorganic%26utm_term%3D%25E7%25BE%258E%25E5%259B%25A2%25E7%25BE%258E%25E9%25A3%259F; _lxsdk_cuid=181942605c1c8-009bf8db503cd6-26021b51-13c680-181942605c1c8; ci=50; rvct=50; __mta=107371197.1656047937719.1656047937719.1656047937719.1; client-id=2e443066-03a8-4e75-871f-53d7f2a6207e; mtcdn=K; userTicket=yNSRzNvlWNjUKPcSfKQoUtlrAOjcuJacoGfRVCnm; _yoda_verify_resp=DceP2kQZwGnqtNsqE%2FPawFl7x6BUpbUEcoCu8jxVulyCKbYv4OLoiEiIa3diwYdu5Rn9eC67MAKWsT4TNmpZG0GK8xpJcd4clxRr7cvPu3EnwZRYBSKZ39GQ2NP4%2FFRGFpLj6jafCkVPR1luVJhQWxLE23mcxctSnBBYwfUXuP%2BAF9wDzFVaJG7MWbvgv%2FNUQLxC8hdbA%2Bs1cHUY59ajteVFjHv40N6O%2B%2BSCpyZPrqdkb%2F2mlxHAVcVrtEuhOMRY8VMKj8MeXqpfae7lxGA8OIE%2F7aRNM9mQ2GPFyAauM32xC7R7xBqAKdJckrgCK%2BtvbolY3LgGAKYdWTYROnU5oAY%2FepYCu5MEJKm1BVCbtAtGVVjTj5TSH85Pz7NZnTkq; _yoda_verify_rid=155fe6a55c416024; u=2513934978; n=KGO493205445; lt=1JKPG_I2R2E-EfC0mkAXF01j3_wAAAAAexIAAJfYb9oGdGYrHoStf8rIPj_BF3J3TEQLFIZo3p2M2RWyIUSLUY2rS7Hv4lcdQOHJDw; mt_c_token=1JKPG_I2R2E-EfC0mkAXF01j3_wAAAAAexIAAJfYb9oGdGYrHoStf8rIPj_BF3J3TEQLFIZo3p2M2RWyIUSLUY2rS7Hv4lcdQOHJDw; token=1JKPG_I2R2E-EfC0mkAXF01j3_wAAAAAexIAAJfYb9oGdGYrHoStf8rIPj_BF3J3TEQLFIZo3p2M2RWyIUSLUY2rS7Hv4lcdQOHJDw; token2=1JKPG_I2R2E-EfC0mkAXF01j3_wAAAAAexIAAJfYb9oGdGYrHoStf8rIPj_BF3J3TEQLFIZo3p2M2RWyIUSLUY2rS7Hv4lcdQOHJDw; firstTime=1656048037867; unc=KGO493205445; _lxsdk=181942605c1c8-009bf8db503cd6-26021b51-13c680-181942605c1c8; _lxsdk_s=181942605c2-eca-9c5-351%7C%7C32',
            'Referer': 'https://hz.meituan.com/meishi/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
        self.city_name = input('请输入城市名称<例如：杭州>')
        self.pagenum = int(input('请输入页数，每页15条美食<例如：3>'))

    # 二进制解压
    def binary_compression(self,data):
        # base编码
        encode1 = str(data).encode()
        # 二进制压缩
        compress = zlib.compress(encode1)
        b_encode = base64.b64encode(compress)
        # 转变str
        cmpned_data = str(b_encode, encoding='utf8')
        return  cmpned_data

    def get_token(self):
        for page in range(1,self.pagenum+1):
            params = {
                "cityName": self.city_name,
                "cateId": "0",
                "areaId": "0",
                "sort": "",
                "dinnerCountAttrId": "",
                "page": page,
                "userId": "2513934978",
                "uuid": "9ffd2bba19834bad9443.1656047928.1.0.0",
                "platform": "1",
                "partner": "126",
                "originUrl": f"https://hz.meituan.com/meishi/pn{page}/",
                "riskLevel": "1",
                "optimusCode": "10"
            }
            # 第一次加密（二进制压缩） ==》 sign
            sign = self.binary_compression(params)
            ip = {
                "rId": 100900,
                "ver": "1.0.6",
                "ts": int(time.time()*1000),
                "cts": int(time.time()*1000) + 2000,
                "brVD": [1440, 150],
                "brR": [[1440, 900], [1440, 852], 24, 24],
                "bI": [f"https://hz.meituan.com/meishi/pn{page}/", "https://hz.meituan.com/meishi/"],
                "mT": [],
                "kT": [],
                "aT": [],
                "tT": [],
                "aM": "",
                "sign": sign
            }
            # 第二次加密（二进制压缩）==》得到token
            token = self.binary_compression(ip)
            params['_token'] = token
            yield params

    def get_response(self,params):
        url = 'https://hz.meituan.com/meishi/api/poi/getPoiList?'
        response = self.session.get(url,params=params,headers=self.headers).json()
        self.parse_data(response)

    def parse_data(self,response):
        for res in response['data']['poiInfos']:
            print(res)

if __name__ == '__main__':
    Mt = MTSpider()
    params = Mt.get_token()
    # yield调用
    for param in params:
        Mt.get_response(param)
        time.sleep(2)
        print('='*30)