'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 12:00:05
LastEditors: Clark
LastEditTime: 2021-12-25 12:02:11
Description: file content
'''

import math

radius = float(input('请输入圆的半径： '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长： %.2f' % perimeter)
print('面积： %.2f' % area)
