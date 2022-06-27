# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/16 12:12
# @File : ydSpider.py
# @SoftWare : Pycharm

"""
通过 提交表单中的加密关键字进行全局搜索，找到js文件，还原
加密参数: salt:
         sign: 6ef5fa66472824b978e1c8cf4d33b2e5
         ts:
         bv: bdc0570a34c12469d01bfac66273680d

js源码：
var r = function(e) {
    var t = n.md5(navigator.appVersion)
      , r = "" + (new Date).getTime()
      , i = r + parseInt(10 * Math.random(), 10);
    return {
        ts: r,
        bv: t,
        salt: i,
        sign: n.md5("fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5")
    }
}
# parseInt(10 * Math.random(),10) #生成一个10*(0,1)的整数，为十进制
"""
import hashlib
import random
import time
from requests_html import HTMLSession
from jsonpath import jsonpath

session = HTMLSession()

headers = {
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1183256839@10.110.96.154; OUTFOX_SEARCH_USER_ID_NCOO=889480715.3813279; fanyi-ad-id=306808; fanyi-ad-closed=1; _ga=GA1.2.542048873.1654955055; hb_MA-AF8F-B2A48FFDAF15_source=www.baidu.com; P_INFO=15670096328|1655201141|1|youdaonote|00&99|null&null&null#hen&410600#10#0|&0||15670096328; STUDY_SESS="PbMkQHtvu6Db11RabXyxpX0KC9INb2hvw6/rRDL8k7eAWcG/L0t6RSc1wdQDyOXIoEDu7So8y7IjNhpg4Z7oSfv5GVWv326h9xRqsOevsE+Cv7DfIGDwt/9TuhJrow3VkgeRMzzDmDFptV6E2fDDhEZBGWVsYUCABaF/2aGY/j4nppr6KrivyjY6FmKs/Qou"; STUDY_INFO="wsk682706@163.com|-1|1414802944|1655352372341"; DICT_SESS=v2|QJrhPNuT_B6BkLJ40fg40JBP4PyhLgZ0lMRfgL64UG0gz0feLnMJy0zAh4qS0MOm0qFnMT4OLw40eLOLkMnf6y0qZO4ey0MTF0; DICT_LOGIN=1||1655352372403; ___rl__test__cookies=1655373445632',
    'Host': 'fanyi.youdao.com',
    'Referer': 'https://fanyi.youdao.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def get_md5():
    r = int(time.time() * 1000)
    i = r + int(random.random() * 10)
    lts = r
    salt = i
    sign_data = "fanyideskweb" + keyword + str(i) + "Ygy_4c=r#e#4EX^NUGUc5"
    sign = hashlib.md5(sign_data.encode('utf8')).hexdigest()
    bv_data = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    bv = hashlib.md5(bv_data.encode('utf8')).hexdigest()
    return salt,sign,lts,bv

def get_response(keyword,salt,sign,lts,bv):
    url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        'i': keyword,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'lts': lts,
        'bv': bv,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    response = session.post(url,data=data,headers=headers).json()
    parse_resp(response)

def parse_resp(response):
    result = jsonpath(response,'$..tgt')[0]
    print(f'"{keyword}"翻译结果为:{result}')

if __name__ == '__main__':
    while True:
        keyword = input('请输入要翻译的关键词<输入0 退出>>>>')
        if keyword == '0':
            break
        salt,sign,lts,bv = get_md5()
        get_response(keyword,salt,sign,lts,bv)