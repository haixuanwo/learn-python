'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 17:51:47
LastEditors: Clark
LastEditTime: 2021-12-25 17:54:16
Description: file content
'''

# - `range(101)`：可以用来产生0到100范围的整数，需要注意的是取不到101。
# - `range(1, 101)`：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
# - `range(1, 101, 2)`：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# - `range(100, 0, -2)`：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

sum = 0
for x in range(101): # 取到[0, 100]
    sum += x

print(sum)
