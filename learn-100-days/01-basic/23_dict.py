'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 16:04:08
LastEditors: Clark
LastEditTime: 2021-12-29 16:19:22
Description: file content
'''

scores = {'海':32, '芳':31, '恒':3}
print(scores)

items1 = dict(one=1, two=2, three=3, four=4)

# zip将序列压成字典
items2 = dict(zip(['a', 'b', 'c'], '123'))

# 创建字典
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)

# 按键获值
print(scores['海'])
print(scores['芳'])
print(scores['恒'])

# 按key值遍历
for key in scores:
    print(f'{key}:{scores[key]}')

scores['海'] = 18
scores.update(芳=16, 恒=4)
print(scores)
print(scores.get('海'))

# 删除
print(scores.popitem())
print(scores.popitem())
print(scores.pop('恒', 4))
print(scores)
scores.clear()
