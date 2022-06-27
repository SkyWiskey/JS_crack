# -*- coding:utf8 -*-
# @Author : Sky
# @Time : 2022/6/16 12:26
# @File : RSA.py
# @SoftWare : Pycharm

"""
"""
# 生成密钥对
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# 生成密钥对
def create_key_pair():
    key = RSA.generate(2048)
    # 提取私钥并存入文件
    private_key = key.export_key()
    file_out = open("private_key.pem", "wb")
    file_out.write(private_key)

    # 提取公钥存入文件
    public_key = key.publickey().export_key()
    file_out = open("public_key.pem", "wb")
    file_out.write(public_key)

# 加密
def RSA_encrypt(data):
    # 从文件中读取公钥
    public_key = RSA.import_key(open("public_key.pem").read())
    # 实例化加密套件
    cipher = PKCS1_OAEP.new(public_key)
    # 加密
    encrypted_data = cipher.encrypt(data)
    print(f'加密后结果：{encrypted_data}')

    # 将加密后的内容写入到文件
    file_out = open("encrypted_data.bin", "wb")
    file_out.write(encrypted_data)

# 解密
def RSA_decrypt():
    # 从私钥文件中读取私钥
    private_key = RSA.import_key(open("private_key.pem", "rb").read())
    # 实例化加密套件
    cipher = PKCS1_OAEP.new(private_key)
    # 从文件中读取加密内容
    encrypted_data = open("encrypted_data.bin", "rb").read()
    # 解密，如无意外data值为最先加密的b"1234567"
    decrypted_data = cipher.decrypt(encrypted_data)
    print(f'解密后结果：{decrypted_data}')

if __name__ == '__main__':
    # 要加密的内容
    data = b"1234567"
    print(f'加密前结果：{data}\n{"="*30}')
    create_key_pair()
    RSA_encrypt(data)
    print('='*30)
    RSA_decrypt()