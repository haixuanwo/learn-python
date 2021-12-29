'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 12:39:45
LastEditors: Clark
LastEditTime: 2021-12-29 12:42:02
Description: file content
'''

a = 0
b = 1
n = int(input('请输入：'))
for i in range(n):
    a, b = b, a + b
    print(a, end=' ')
