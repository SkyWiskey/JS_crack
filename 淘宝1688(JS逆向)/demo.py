# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/24 16:26
# @File : demo.py
# @SoftWare : Pycharm

"""
"""
from requests_html import HTMLSession
from urllib.parse import unquote,quote

headers = {
    'cookie': '__wpkreporterwid_=68a557ef-44b7-491f-8027-2e0e6050da3f; cna=hHwgG5o3xQsCAbZ0Hb+uY5xj; lid=%E5%AE%89%E8%BF%AA%E6%88%91%E6%98%AF%E6%9F%A0%E6%AA%AC%E6%A0%91; xlly_s=1; cookie2=20273dd26073ebd3cf4faf504698c3e7; sgcookie=E100gKrShwvmXHyFh6i7vXsg4o2bWoCEPo2PO8GtaCuVtyfLaLEhQzQwkiUKeftTeRpj%2BZ93ParG3dCOYHGqHHLHf%2Fs5nqj%2BSTgKc5rNR90C1jRUlHqMcQ4kgIFWN2Y8V7G8; t=624b9e0eae8ca8102a4406a8839f5669; _tb_token_=e70ef8eeb8713; uc4=id4=0%40U2OT7Lj%2BxNPvAb8rJYi6R3JKnGrH&nk4=0%400UmH9NJX%2BK49gHoBz5WGJgoDaG72Zl1Ifw%3D%3D; __cn_logon__=false; _m_h5_tk=6da0b27e890b4ab07f222a86562b0d34_1656068970828; _m_h5_tk_enc=11dc7301e15d9d20ae8597c4f25a83e6; alicnweb=touch_tb_at%3D1656058893975; ali_ab=42.226.86.102.1656058912668.5; _csrf_token=1656058913812; tfstk=cR2cBQV7USlbMyhuOtMfB6l5tHJGZ-KrkPzbUiWkoeC_a0yPixdyTqM1Z4bCuC1..; l=eBPqX3lqL6OGt0GsBO5Bourza77TVIRb8oVzaNbMiInca6GNFFz_VNChPIsXcdtjgtfjYetP0_WjjdhwJvaLRbMDBeYQARjSHDJ9-; isg=BAwMweVAguoW9ZaLh2f7FUgF3Wo-RbDvbc26u2bNs7dU8a37jlV1f_kLkflJvehH',

'referer': 'https://zy.1688.com/',

'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}
# url = 'https://search.1688.com/service/marketOfferResultViewService?keywords=%E5%85%85%E6%B0%94%E5%A8%83%E5%A8%83%20%E7%94%B7%E7%94%A8&n=y&spm=a260k.635.3262836.d102&sug=2_0&beginPage=3&async=true&asyncCount=20&pageSize=60&startIndex=0&pageName=major&offset=0&sessionId=66dc696083fd48e99ee3a20e14a27be6&_bx-v=1.1.20'
# session = HTMLSession()
# resp = session.get(url,headers=headers).text
# print(resp)
print(quote('充气娃娃 男用'))
print(unquote('%BC%FC%C5%CC'))