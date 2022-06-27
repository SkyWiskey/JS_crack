# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/16 18:44
# @File : bdSpider.py
# @SoftWare : Pycharm

"""
加密参数:sign:'551517.821612'   #js函数逆向分析 i值的获取 == 320305.131321201
        token:'e6c8c710902838207039bb62ce86dd7f'  #服务器传参 请求接口 提取token
"""
import execjs
from requests_html import HTMLSession
import re
from jsonpath import jsonpath

session = HTMLSession()

def parse_sign(keyword):
    with open('./bdeyt.js', 'r', encoding='utf8') as f:
        jscode = f.read()
    ctx = execjs.compile(jscode).call('e', keyword)
    sign = ctx
    return sign
def parse_token():
    url = 'https://fanyi.baidu.com/?aldtype=16047'
    headers = {
        'Cookie': 'BIDUPSID=244F7E236F42633EEB445682EF54A0AF; PSTM=1653979428; BAIDUID=244F7E236F42633E8A204F177AE20CD0:FG=1; APPGUIDE_10_0_2=1; SOUND_SPD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=VAzZXVKdEloV1VaTXI2MU9OQkNKWmZBU3l1a2hZMzRheS1sd2Q3bWZDNFJCdEZpRVFBQUFBJCQAAAAAAAAAAAEAAAApnj990NzS1bey1~bO0sPDw8MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABF5qWIRealiV; BDUSS_BFESS=VAzZXVKdEloV1VaTXI2MU9OQkNKWmZBU3l1a2hZMzRheS1sd2Q3bWZDNFJCdEZpRVFBQUFBJCQAAAAAAAAAAAEAAAApnj990NzS1bey1~bO0sPDw8MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABF5qWIRealiV; BDSFRCVID_BFESS=vW-OJexroG0CpmnDminrUP-mymKKvV3TDYLEdBExdG8EnLIVgxoREG0Pt_NFmZK-oxmHogKKBeOTHnLF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJkfoCDKtCt3HnRY-P4_-tAt2qoXetJyaR0t5KnvWJ5TMCoJQhbb0T-vhfrXWlQTHCj8Xpv7btt5ShPC-tnRDl08Dp6u2P3OQ6QdLb6j3l02VMjae-t2yU_VbUOX5tRMW23G0l7mWnrdsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCajTcyja_Hq-o2bI5qB4bXHJnhHt3NMtbShnLOqxby26nqQ-j9aJ5y-J7nhhOxhtTUhtFHKRoTe4r8am3iLfLbQpbZ8h5gLxoWbMbbQfTrBl5MMIONKl0MLPbr8lQzWx4VhnkDyMnMBMnG5mOnanr13fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-XjjJXDHQP; H_PS_PSSID=36425_36550_36459_36503_36454_31253_36452_36423_36166_36075_36620_36519_26350_36469; BAIDUID_BFESS=A02719BEBF1A5DA77BC7DFE7D6DBBB07:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655310124,1655338734,1655351199,1655355196; delPer=0; PSINO=2; BA_HECTOR=0401akak0k20ag0ga01halijv15; ZFY=Rkrml9xU:BTUXnIkKwjUGsQTPpRntqp0BfJuTBfsT0TY:C; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1655377208; ab_sr=1.0.1_MjllOGZjYjUzYzc3NzE2ODkxZWJkZGUzZmY4NjYwNWFkYTYyNzRmMjE1ZGYyNzE2ZWVmNjRiMTM4MzYwODVjNGI1NGM2ZmY3YmEwOThhNTEzYTAzNDYyMzkxYTIwNzNhM2JlZGM3MTM1Yjk2OTBjZGQ4MTE0NTEzMmVjMDdhNzIzYzRmOTI5ZjZkZTFjNjFlMmI2OTAxZDczNDJjMmZiYzQxNjdlYzhjNWRlMzkxYjhjY2ZkZWE4NGNkZmE5YmM2',
        'Host': 'fanyi.baidu.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    resp = session.get(url, headers=headers).text
    token = re.findall("token: '(.*?)'", resp)[0]
    return token

def translate(ttype,sign,token):
    url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
    headers = {
        'Cookie': 'BIDUPSID=244F7E236F42633EEB445682EF54A0AF; PSTM=1653979428; BAIDUID=244F7E236F42633E8A204F177AE20CD0:FG=1; APPGUIDE_10_0_2=1; SOUND_SPD_SWITCH=1; REALTIME_TRANS_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=VAzZXVKdEloV1VaTXI2MU9OQkNKWmZBU3l1a2hZMzRheS1sd2Q3bWZDNFJCdEZpRVFBQUFBJCQAAAAAAAAAAAEAAAApnj990NzS1bey1~bO0sPDw8MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABF5qWIRealiV; BDUSS_BFESS=VAzZXVKdEloV1VaTXI2MU9OQkNKWmZBU3l1a2hZMzRheS1sd2Q3bWZDNFJCdEZpRVFBQUFBJCQAAAAAAAAAAAEAAAApnj990NzS1bey1~bO0sPDw8MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABF5qWIRealiV; BDSFRCVID_BFESS=vW-OJexroG0CpmnDminrUP-mymKKvV3TDYLEdBExdG8EnLIVgxoREG0Pt_NFmZK-oxmHogKKBeOTHnLF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJkfoCDKtCt3HnRY-P4_-tAt2qoXetJyaR0t5KnvWJ5TMCoJQhbb0T-vhfrXWlQTHCj8Xpv7btt5ShPC-tnRDl08Dp6u2P3OQ6QdLb6j3l02VMjae-t2yU_VbUOX5tRMW23G0l7mWnrdsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCajTcyja_Hq-o2bI5qB4bXHJnhHt3NMtbShnLOqxby26nqQ-j9aJ5y-J7nhhOxhtTUhtFHKRoTe4r8am3iLfLbQpbZ8h5gLxoWbMbbQfTrBl5MMIONKl0MLPbr8lQzWx4VhnkDyMnMBMnG5mOnanr13fAKftnOM46JehL3346-35543bRTLnLy5KJYMDcnK4-XjjJXDHQP; H_PS_PSSID=36425_36550_36459_36503_36454_31253_36452_36423_36166_36075_36620_36519_26350_36469; BAIDUID_BFESS=A02719BEBF1A5DA77BC7DFE7D6DBBB07:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1655310124,1655338734,1655351199,1655355196; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1655355196; delPer=0; PSINO=2; BA_HECTOR=0401akak0k20ag0ga01halijv15; ZFY=Rkrml9xU:BTUXnIkKwjUGsQTPpRntqp0BfJuTBfsT0TY:C; ab_sr=1.0.1_OWQ5MjMzNTA3MTE1NzZmN2MwOTY0MWIwNzNlNmM0ZTVmOWFhYjZlYmZjYzNmNjFjODA4NDIxNDlhMDE0MTYyZDI2YTRjOTMwMGFlYmFkOTYwMjk0YjA2M2JhNWQwMWM5ZGYzZjY4Zjk3MzY4ZWE1MjkzOWJmMDk4ZWZiNjcxNWMzMWQ1M2JiZGUwYTcyODlkNDU4YzFjYjM0M2IxZjM4N2JkN2VjOTM0Y2U5MTM0NzBiZjlhMDBmM2EwOGMzNTMw',
        'Host': 'fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    data = {
        'from': 'zh',
        'to': 'en',
        'query': keyword,
        'transtype': 'translang',
        'simple_means_flag': 3,
        'sign': sign,
        'token': token,
        'domain': 'common'
    }
    if ttype == 2:
        data['from'] = 'en'
        data['to'] = 'zh'
    response = session.post(url,data=data,headers=headers).json()
    res = jsonpath(response,'$..dst')[0]
    print(f'”{keyword}“翻译结果为:{res}')

if __name__ == '__main__':
    while True:
        print("1:'汉语>>>英语'\n2:'英语>>>汉语'\n0:'退出'")
        ttype = int(input('请输入翻译类型>>>'))
        if ttype == 0:
            break
        keyword = input('请输入关键词>>>')
        sign = parse_sign(keyword)
        token = parse_token()
        translate(ttype,sign,token)


