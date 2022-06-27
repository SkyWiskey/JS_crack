# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/22 20:55
# @File : 1688_spider.py
# @SoftWare : Pycharm

"""
"""
import re
import time
from urllib.parse import quote

import execjs
from requests_html import HTMLSession


class TB1688Spider:
    def __init__(self):
        self.time = int(time.time()*1000)
        self.session = HTMLSession()
        self.headers = {
            'cookie': 'cna=hHwgG5o3xQsCAbZ0Hb+uY5xj; lid=%E5%AE%89%E8%BF%AA%E6%88%91%E6%98%AF%E6%9F%A0%E6%AA%AC%E6%A0%91; xlly_s=1; _m_h5_tk=c712be77dd8f918b23416b320d7c557e_1655987299906; _m_h5_tk_enc=74f0597e082a3ddacc572a01f73e5693; cookie2=20bceaf4ca59ca869597b23af6523b64; sgcookie=E100gKrShwvmXHyFh6i7vXsg4o2bWoCEPo2PO8GtaCuVtyfLaLEhQzQwkiUKeftTeRpj%2BZ93ParG3dCOYHGqHHLHf%2Fs5nqj%2BSTgKc5rNR90C1jRUlHqMcQ4kgIFWN2Y8V7G8; t=2add661280a28302077beac12fc569bc; _tb_token_=5a1351f517b39; uc4=id4=0%40U2OT7Lj%2BxNPvAb8rJYi6R3JKnGrH&nk4=0%400UmH9NJX%2BK49gHoBz5WGJgoDaG72Zl1Ifw%3D%3D; __cn_logon__=false; alicnweb=touch_tb_at%3D1655977941998; isg=BFFRhAOv19ToPTvcMkyO-uVuYF3rvsUwsBYXTDPnfJhZ2nAsewxGAWJ7fK48Ul1o; tfstk=cS6lB01f3_R7h-Ac1897p-i9r0BhZIm2yw753uPtMG1F-nBVi9hq_U9QiE4_zX1..; l=eBPqX3lqL6OGtjZJBO5ahurza77OyIOb8sPzaNbMiInca1yl_hMkNNChys228dtjgt5A0etP0_WjjdEpWP4U-AkDBeYIujcjfZJw8e1..',
            'referer': 'https://sale.1688.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
    def execute_js(self):
        # 读取js文件
        with open('./1688.js','r',encoding='utf8')as f:
            jscode = f.read()
        token = re.findall('_m_h5_tk=(.+?)_',self.headers['cookie'])[0]
        sign = token + "&" + str(self.time) + "&" + '12574478' + '&' + '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=10166&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\",\\"url\\":\\"https://sale.1688.com/factory/category.html?spm=a260k.22464671.home2019category.1.221a7a6eluE1Qq&mainId=10166\\"}"}'
        # sign = 'c712be77dd8f918b23416b320d7c557e' + "&" + str(1655978117335) + "&" + '12574478' + '&' + '{"cid":"TpFacRecommendService:TpFacRecommendService","methodName":"execute","params":"{\\"query\\":\\"mainCate=10166&leafCate=\\",\\"sort\\":\\"mix\\",\\"pageNo\\":\\"1\\",\\"pageSize\\":\\"20\\",\\"from\\":\\"PC\\",\\"trafficSource\\":\\"pc_index_recommend\\",\\"url\\":\\"https://sale.1688.com/factory/category.html?spm=a260k.22464671.home2019category.1.221a7a6eluE1Qq&mainId=10166\\"}"}'
        # 通过构造加密参数
        ctx = execjs.compile(jscode).call('h',sign)
        self.run(ctx)

    def run(self,ctx):
        urls = f'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/?jsv=2.6.1&appKey=12574478&t={self.time}&sign={ctx}&v=1.0&type=jsonp&isSec=0&timeout=20000&api=mtop.taobao.widgetService.getJsonComponent&dataType=jsonp&jsonpIncPrefix=mboxfc&callback=mtopjsonpmboxfc3&data=%7B%22cid%22%3A%22TpFacRecommendService%3ATpFacRecommendService%22%2C%22methodName%22%3A%22execute%22%2C%22params%22%3A%22%7B%5C%22query%5C%22%3A%5C%22mainCate%3D10166%26leafCate%3D%5C%22%2C%5C%22sort%5C%22%3A%5C%22mix%5C%22%2C%5C%22pageNo%5C%22%3A%5C%221%5C%22%2C%5C%22pageSize%5C%22%3A%5C%2220%5C%22%2C%5C%22from%5C%22%3A%5C%22PC%5C%22%2C%5C%22trafficSource%5C%22%3A%5C%22pc_index_recommend%5C%22%2C%5C%22url%5C%22%3A%5C%22https%3A%2F%2Fsale.1688.com%2Ffactory%2Fcategory.html%3Fspm%3Da260k.22464671.home2019category.1.221a7a6eluE1Qq%26mainId%3D10166%5C%22%7D%22%7D'
        resp = self.session.get(urls,headers=self.headers).text
        print(resp)

if __name__ == '__main__':
    tb = TB1688Spider()
    tb.execute_js()