# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/23 18:11
# @File : cninfo_spider.py
# @SoftWare : Pycharm

"""
请求头：mcode加密
根据接口URL路径进行全局搜索定位js文件
找到主体函数进行分析

"""
import time
import execjs
from requests_html import HTMLSession
import pymongo

class CninfoSpider:
    def __init__(self):
        self.time = int(time.time()*1000)
        self.session = HTMLSession()
        self.conn = pymongo.MongoClient(host='localhost',port=27017)
        self.collection = self.conn['Cninfo']['infos']

    def run_js(self):
        with open('./cninfo.js','r',encoding='utf8')as f:
            jscode = f.read()
        mcode = execjs.compile(jscode).call('getResCode')
        self.get_response(mcode)

    def get_response(self,mcode):
        url = 'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1655279455,1655607357,1655798357,1655978934; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1655980460',
            'mcode': mcode,
            'Origin': 'http://webapi.cninfo.com.cn',
            'Referer': 'http://webapi.cninfo.com.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
        data = {'tdate': '2022-06-22', 'market': 'SZE'}
        response = self.session.post(url,data=data,headers=headers).json()
        self.parse_data(response)

    def parse_data(self,response):
        for res in response['records']:
            res['_id'] = res['证券代码']
            try:
                self.collection.insert_one(res)
                print(f"{res['证券简称']}存储成功")
            except:
                pass

if __name__ == '__main__':
    C = CninfoSpider()
    C.run_js()