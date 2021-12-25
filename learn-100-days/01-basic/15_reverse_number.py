'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 18:22:28
LastEditors: Clark
LastEditTime: 2021-12-25 18:26:02
Description: file content
'''

num = int(input('input num = '))
reversed_num = 0

while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print(reversed_num)