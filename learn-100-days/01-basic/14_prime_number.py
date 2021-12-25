'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 18:17:35
LastEditors: Clark
LastEditTime: 2021-12-25 18:19:40
Description: file content
'''

from math import sqrt

num = int(input('请输入一个正数:'))
end = int(sqrt(num))
is_prime = True

for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

