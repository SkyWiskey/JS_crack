# -*- codingutf8 -*-
# @Author  Sky
# @Time  2022/6/24 1830
# @File  migu_spider.py
# @SoftWare  Pycharm

"""
加密参数 i:sha1加密
"""
import re
import time
import hashlib
from requests_html import HTMLSession

class MiguSpider:
    def __init__(self):
        self.time1 = int(time.time())
        self.session = HTMLSession()
    def sha1_encrypt(self):
        """
        c 001002A
            f html
            k ffa5ebc8-059f-4f46-86af-b6db5f8b89d7-n41656066296389
            keyword Left%20and%20Right
            s 1656077766
            u Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36/220001
            v 3.23.1
        """
        i = f'c001002Afhtmlkffa5ebc8-059f-4f46-86af-b6db5f8b89d7-n41656066296389keyword%E5%83%8F%E6%88%91%E8%BF%99%E6%A0%B7%E7%9A%84%E4%BA%BAs{self.time1}uMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36/220001v3.23.1'
        data = hashlib.sha1(i.encode('utf8')).hexdigest()
        print(data)
        self.run(data)

    def run(self,data):
        url = 'https://music.migu.cn/v3/search?'
        headers = {
            'cookie': 'migu_cookie_id=ffa5ebc8-059f-4f46-86af-b6db5f8b89d7-n41656066296389; mg_uem_user_id_9fbe6599400e43a4a58700a822fd57f8=7f0dffb6-d5b8-4722-933a-1b222c449ed4; cookieId=CQ4jHvqfYAZR0Qn7hMJeU1X6qXp7yfw1656066872905; idmpauth=true@passport.migu.cn; player_stop_open=0; playlist_adding=1; audioplayer_new=1; addplaylist_has=1; add_play_now=1; playlist_change=0; audioplayer_exist=1; audioplayer_open=0; WT_FPC=id=2d2df843dec3d05ff5a1656066297328:lv=1656080837464:ss=1656074132509',
            'referer': f'https://music.migu.cn/v3/search?page=1&type=song&i={data}&f=html&s={self.time1}&c=001002A&keyword=%E5%83%8F%E6%88%91%E8%BF%99%E6%A0%B7%E7%9A%84%E4%BA%BA&v=3.23.1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
        }
        params = {
            'page': 1,
            'type': 'song',
            'f': 'html',
            's': self.time1,
            'c': '001002A',
            'keyword': '像我这样的人',
            'v':'3.23.1'
        }
        params['i'] = data
        response = self.session.get(url,params=params,headers=headers).text
        print(response)


if __name__ == '__main__':
    Migu = MiguSpider()
    Migu.sha1_encrypt()