# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/24 14:43
# @File : 二进制解压缩.py
# @SoftWare : Pycharm

"""
"""
import base64
import zlib
import json

# 二进制压缩
def binary_compression(token_string):
    # base编码
    encode1 = str(token_string).encode()
    # 二进制压缩
    compress = zlib.compress(encode1)
    b_encode = base64.b64encode(compress)
    # 转变str
    str_token = str(b_encode,encoding='utf8')
    print(str_token)
    return str_token



# 二进制解压
def binary_decompression(data):
    data_encode = base64.b64decode(data.encode())
    # 解压
    decompression = zlib.decompress(data_encode).decode('utf8')
    print(decompression)

    # 递归调用
    sign = json.loads(decompression)['sign']
    binary_decompression(sign)

if __name__ == '__main__':
    token_string = "areaId=0&cateId=0&cityName=杭州&dinnerCountAttrId=&optimusCode=10&originUrl=https://hz.meituan.com/meishi/&page=1&partner=126&platform=1&riskLevel=1&sort=&userId=2513934978&uuid=9ffd2bba19834bad9443.1656047928.1.0.0"
    binary_compression(token_string)
    print('='*70)
    data = 'eJxVjt1ugkAQhd9lb0tkF9YFTHqBWgWMRUAJtfGC/0UEKWxBafru3abtRZNJzpkzXybnA7RmAmYIQg1CAfRpC2YATeCEAAGwjl/IlECsIaRJChJA/D/DWBJA1PpLMHtFGENBnuLTd+Ly4Cfhf0/Cj1Wn0kmQMJ9vxuQIoIw13UwU6Tip0oK9h/UkvlYi9x0tRN4BcLTac5Rr+avhr7K/fctLc7Yr8pq71Bou5wOyh1F3aCp69JjadUSbs+2sSH61unSrl3LrnedtVO7ROm97fenT0Tznhvs2pg3J5Bgvtqq9SJ5okot6VqB7bBJDSXfKg7i7evV6uc4OGKnj9Ba5b16ySdz7npLEL6zL+8VSx4ZFVZbckRy01XAzg4Wx8YYmwYrlWXKIWbnZj2vZIwE+PAyh2szvYR3WsdE/rZj6cjkGYbHqR4VgjXSmfWtgffCYcjxmhrYzbQlK80p9Dl+ctL3Zi2bselgy3/WMAM+p7m8c5/ERfH4B+cSQZA=='
    binary_decompression(data)
