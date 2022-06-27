# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/21 17:06
# @File : jzsc_spider.py
# @SoftWare : Pycharm

"""
url:http://jzsc.mohurd.gov.cn/data/company
查看接口的响应数据，发现数据是加密的
思路分析：
1、对接口的url路径进行XHR断点 然后进行调试找数据的解密算法
2、在找到疑似数据或者JS解密算法之后 做断点调试 控制台输出数据
3、python模拟解密算法
"""
''' 主要js解密函数
function h(t) {  # t就是加密数据data 
    var e = d.a.enc.Hex.parse(t)
      , n = d.a.enc.Base64.stringify(e)
      , a = d.a.AES.decrypt(n, f, {  # n-明文，等待被加密   f-密钥
        iv: m,  # iv-偏移量 至少 16 位，或者为 16 的倍数
        mode: d.a.mode.CBC,  #CBC加密模式
        padding: d.a.pad.Pkcs7  # Pkcs7填充方法
    })
      , r = a.toString(d.a.enc.Utf8);
    return r.toString()
}
'''

import json
import time
from requests_html import HTMLSession
from Crypto.Cipher import AES


class JZSCCrackSpide:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
        # 更换接口url、和参数 即可爬取不同类型的数据
        self.start_url = 'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/project/ecLicence?pg={}&pgsz=15&total=450'
    def get_response(self):
        for page in range(5):
            print(f'============================正在爬取page{page}==============================')
            url = self.start_url.format(page)
            response = self.session.get(url).content.decode()
            self.aes_decrypt(response)
            time.sleep(1)

    def aes_decrypt(self,response):
        """
        AES解密过程
        :param response:
        :return:
        """
        key = b'jo8j9wGw%6HbxfFn'  #密钥
        iv = b'0123456789ABCDEF'   #偏移量
        mode = AES.MODE_CBC        #加密/解密模式

        # 创建AES解密套件
        cipher = AES.new(key,mode,iv)
        # 将数据转成bytes类型 然后进行解密
        decrypted_data = cipher.decrypt(bytes.fromhex(response))
        # 数据是进行过pkcs7填充的 需要取消填充
            # 方式一
        unpad = lambda s:s[:-ord(s[len(s)-1:])]
        results = unpad(decrypted_data)
            # 方式二
        # length = len(result) # 字符串长度
        # unpadding = ord(result[length-1]) #获取最后一个字符串的ASCII
        # result = result[0:length-unpadding]

        # 将数据转成字典
        results = json.loads(results)['data']['list']
        for res in results:
            print(res)

    def save_data(self):
        pass

if __name__ == '__main__':
    J = JZSCCrackSpide()
    J.get_response()