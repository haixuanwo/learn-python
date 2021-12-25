'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 18:08:05
LastEditors: Clark
LastEditTime: 2021-12-25 18:10:08
Description: file content
'''

# 输出九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d*%d=%d' % (i, j, i*j), end='\t')
    print()
