'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 15:14:08
LastEditors: Clark
LastEditTime: 2021-12-29 15:44:06
Description: file content
'''

list1 = [1, 3, 5, 7, 100]
print(list1)

list2 = ['hello'] * 3
print(list2)
print(len(list2))

print(list1[0])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] = 300
print(list1)

for elem in list1:
    print(elem)

for index, elem in enumerate(list1):
    print(index, elem)

# 添加元素
list1.append(200)
list1.insert(1, 400)
list1 += [1000, 2000]
print(list1)
print(len(list1))

# 删除元素
if 3 in list1:
    list1.remove(3)

if 1234 in list1:
    list1.remove(1234)
print(list1)

list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)
list1.clear()
print(list1)

# 切片
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
fruits2 = fruits[1:4] # 1~3
print(fruits2)
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits3[-3:-1] # 逆取
print(fruits4)
fruits5 = fruits[::-1]  # 逆序
print(fruits5)

list2 = sorted(fruits) # 返回排序后的拷贝
list3 = sorted(list1, reverse=True)
list4 = sorted(list1, key=len)
print(fruits)
print(list2)
print(list3)
print(list4)
fruits.sort(reverse=True)
print(fruits)

# 创建列表
f = [x for x in range(1, 10)]
print(f)

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)

import sys
f =[x ** 2 for x in range(1, 10)] # 2次方
print(sys.getsizeof(f)) # 查看对象占用内存字节数
print(f)

