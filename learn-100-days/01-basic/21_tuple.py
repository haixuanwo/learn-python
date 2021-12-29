'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 15:46:35
LastEditors: Clark
LastEditTime: 2021-12-29 15:52:27
Description: file content
'''

# 元组的元素不能修改，存多种类型
t = ('谭纳虱', 32, True, '湖南郴州')
print(t)
print(t[0])
print(t[3])
for m in t:
    print(m)

l = list(t) # 转成列表
print(l)
t1 = tuple(l) # 转成元组
print(t1)




