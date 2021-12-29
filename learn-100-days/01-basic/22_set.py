'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 15:55:03
LastEditors: Clark
LastEditTime: 2021-12-29 16:02:58
Description: file content
'''

# 不允许重复元素，可交、并、差集等

set1 = {1, 2, 3, 4}
print(set1)
print(len(set1))

set2 = set(range(1, 10))
print(set2)
print(set1, set2)

set1.add(4)
set1.add(5)
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set2.pop())
print(set2)

# 交、并、差集，对称差运算
print(set1 & set2)
print(set1 | set2)
print(set1 - set2)
print(set1 ^ set2)
print(set1 <= set2)
