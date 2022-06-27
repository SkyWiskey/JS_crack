# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/20 15:38
# @File : tbrm_spider.py
# @SoftWare : Pycharm

"""
sign加密
"""
import time
import json
import execjs
from requests_html import HTMLSession

c = {"pNum":0,"pSize":"60","refpid":"mm_10011550_0_0","variableMap":"{\"q\":\"休闲男裤\",\"navigator\":true,\"union_lens\":\"recoveryid:201_33.5.169.247_5294685_1655711616119;prepvid:201_33.5.169.247_5294685_1655711616119\",\"recoveryId\":\"201_33.53.204.179_5299941_1655713408208\"}","qieId":"34374","spm":"a2e1u.19484427.29996460","app_pvid":"201_33.53.204.179_5299941_1655713408208","ctm":"spm-url:a2e1u.13363363.1998559106.3.635a7466oo0YHk;page_url:https%3A%2F%2Fai.taobao.com%2Fsearch%2Findex.htm%3Fspm%3Da2e1u.13363363.1998559106.3.635a7466oo0YHk%26pid%3Dmm_10011550_0_0%26source_id%3Dsearch%26key%3D%25E4%25BC%2591%25E9%2597%25B2%25E7%2594%25B7%25E8%25A3%25A4%26union_lens%3Drecoveryid%253A201_33.5.169.247_5294685_1655711616119%253Bprepvid%253A201_33.5.169.247_5294685_1655711616119"}
r = {"pNum":0,"pSize":"60","refpid":"mm_10011550_0_0","variableMap":"{\"q\":\"休闲男裤\",\"navigator\":true,\"union_lens\":\"recoveryid:201_33.5.169.247_5294685_1655711616119;prepvid:201_33.5.169.247_5294685_1655711616119\",\"recoveryId\":\"201_33.44.171.56_7051120_1655712242262\"}","qieId":"34374","spm":"a2e1u.19484427.29996460","app_pvid":"201_33.44.171.56_7051120_1655712242262","ctm":"spm-url:a2e1u.13363363.1998559106.3.635a7466oo0YHk;page_url:https%3A%2F%2Fai.taobao.com%2Fsearch%2Findex.htm%3Fspm%3Da2e1u.13363363.1998559106.3.635a7466oo0YHk%26pid%3Dmm_10011550_0_0%26source_id%3Dsearch%26key%3D%25E4%25BC%2591%25E9%2597%25B2%25E7%2594%25B7%25E8%25A3%25A4%26union_lens%3Drecoveryid%253A201_33.5.169.247_5294685_1655711616119%253Bprepvid%253A201_33.5.169.247_5294685_1655711616119"}

sign = '261bdc1b5a1f0bfdb09deb46b360858a' + '&' + str(int(time.time()*1000)) + '&' + '12574478' + '&' + r'{"pNum":0,"pSize":"60","refpid":"mm_10011550_0_0","variableMap":"{\"q\":\"休闲男裤\",\"navigator\":true,\"union_lens\":\"recoveryid:201_33.5.169.247_5294685_1655711616119;prepvid:201_33.5.169.247_5294685_1655711616119\",\"recoveryId\":\"201_33.44.171.56_7051120_1655712242262\"}","qieId":"34374","spm":"a2e1u.19484427.29996460","app_pvid":"201_33.44.171.56_7051120_1655712242262","ctm":"spm-url:a2e1u.13363363.1998559106.3.635a7466oo0YHk;page_url:https%3A%2F%2Fai.taobao.com%2Fsearch%2Findex.htm%3Fspm%3Da2e1u.13363363.1998559106.3.635a7466oo0YHk%26pid%3Dmm_10011550_0_0%26source_id%3Dsearch%26key%3D%25E4%25BC%2591%25E9%2597%25B2%25E7%2594%25B7%25E8%25A3%25A4%26union_lens%3Drecoveryid%253A201_33.5.169.247_5294685_1655711616119%253Bprepvid%253A201_33.5.169.247_5294685_1655711616119"}'

with open('./tbrm.js','r',encoding='utf8')as f:
    jscode = f.read()
etx = execjs.compile(jscode).call('h',sign)
print(etx)

headers ={
    'cookie': 't=cc1596a197cd719d5f8329c35e9f659d; thw=cn; cna=hHwgG5o3xQsCAbZ0Hb+uY5xj; sgcookie=E100YEIBYrG7R2ox0ktcYOXVBIQ5Vq3CFTf5sY7%2Bxss9wd1M0M3KAJ5Qa8bpQ8O2D1Hxlay1ZpZuLby91jaUyQmNJs7%2FAgAX%2FbRcOZH7UcmZugMorlp%2BTMHef3GqlkZRg3kA; uc3=lg2=UIHiLt3xD8xYTw%3D%3D&id2=UUGk3PQHkpJR6g%3D%3D&nk2=0%2FI38h4FjmWtXqJXOwY%3D&vt3=F8dCvCISXMgd4slAli4%3D; lgc=%5Cu5B89%5Cu8FEA%5Cu6211%5Cu662F%5Cu67E0%5Cu6AAC%5Cu6811; uc4=nk4=0%400UmH9NJX%2BK49gHoBz5WGJgoDaG%2FsCcLC7w%3D%3D&id4=0%40U2OT7Lj%2BxNPvAb8rJYi6RmkX1wQh; tracknick=%5Cu5B89%5Cu8FEA%5Cu6211%5Cu662F%5Cu67E0%5Cu6AAC%5Cu6811; _cc_=VT5L2FSpdA%3D%3D; _m_h5_tk=261bdc1b5a1f0bfdb09deb46b360858a_1655721333777; _m_h5_tk_enc=0a01afdd5db90bcbb3384e84a99b1787; mt=ci=-1_0; cookie2=14b46e30862efd97a4f6e7b307ba5f40; _tb_token_=30e1e1e16e3fe; xlly_s=1; isg=BGZmzWBFOEGFCez7EzfrJcrat9zoR6oBo6-gbVAOFglk0wftuNW2EIPiK8_f-6IZ; l=eBjDyldgLkKVln05BO5Cnurza779rIOb8sPzaNbMiInca6OCOFGs4NChkOaH5dtjgt5XHetP0_Wjjd3D5caU-FkDBeYQlwrE1Lvw8e1..; tfstk=cNx1BJ_mW5Vsl6u4bdME7m5B0ujAZWE1LA1HCXKvireI2ev1iyZPNDk2nWIVH91..; uc1=cookie14=UoexN9SjXmUbBw%3D%3D',
    'referer': 'https://ai.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
session = HTMLSession()
url = 'https://h5api.m.taobao.com/h5/mtop.alimama.union.xt.en.api.entry/1.0/?'
params = {
    'jsv': '2.5.1',
    'appKey': '12574478',
    't': int(time.time()*1000),
    'sign': sign,
    'api': 'mtop.alimama.union.xt.en.api.entry',
    'v': '1.0',
    'AntiCreep': 'true',
    'timeout': '20000',
    'AntiFlood': 'true',
    'type': 'jsonp',
    'dataType': 'jsonp',
    'callback': 'mtopjsonp2',
    'data': '{"pNum":0,"pSize":"60","refpid":"mm_10011550_0_0","variableMap":"{\"q\":\"休闲男裤\",\"navigator\":true,\"union_lens\":\"recoveryid:201_33.5.169.247_5294685_1655711616119;prepvid:201_33.5.169.247_5294685_1655711616119\",\"recoveryId\":\"201_33.44.171.56_7051120_1655712242262\"}","qieId":"34374","spm":"a2e1u.19484427.29996460","app_pvid":"201_33.44.171.56_7051120_1655712242262","ctm":"spm-url:a2e1u.13363363.1998559106.3.635a7466oo0YHk;page_url:https%3A%2F%2Fai.taobao.com%2Fsearch%2Findex.htm%3Fspm%3Da2e1u.13363363.1998559106.3.635a7466oo0YHk%26pid%3Dmm_10011550_0_0%26source_id%3Dsearch%26key%3D%25E4%25BC%2591%25E9%2597%25B2%25E7%2594%25B7%25E8%25A3%25A4%26union_lens%3Drecoveryid%253A201_33.5.169.247_5294685_1655711616119%253Bprepvid%253A201_33.5.169.247_5294685_1655711616119"}'
}
resp = session.get(url,params=params,headers=headers).content.decode()
print(resp)