'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 17:55:47
LastEditors: Clark
LastEditTime: 2021-12-25 18:03:03
Description: file content
'''

import random

answer = random.randint(1, 100)
counter = 0

print('欢迎来到猜数字[1, 100]的游戏')
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break

print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')
