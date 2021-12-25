'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 17:47:02
LastEditors: Clark
LastEditTime: 2021-12-25 17:49:40
Description: file content
'''

username = input('请输入用户名: ')
password = input('请输入口令: ')

if username == 'admin' and password == '123456':
    print('身份验证成功!')
else:
    print('身份验证失败!')

