'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 15:00:06
LastEditors: Clark
LastEditTime: 2021-12-29 15:12:09
Description: file content
'''

s1 = 'hello, world'
s2 = 'hello, world'
s3 = """hello,
world!
"""
print(s1, s2, s3, end='')

# 可以在字符串中使用`\`（反斜杠）来表示转义，也就是说`\`后面的字符不再是它原来的意义
s1 = '\'hello, world\''
s2 = '\n\\hello, world\\\n'
print(s1, s2, end='')

# 在`\`后面还可以跟一个八进制或者十六进制数来表示字符，例如`\141`和`\x61`都代表小写字母`a`，
# 前者是八进制的表示法，后者是十六进制的表示法。也可以在`\`后面跟Unicode字符编码来表示字符，
# 例如`\u9a86\u660a`代表的是中文“骆昊”
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

# Python为字符串类型提供了非常丰富的运算符，我们可以使用`+`运算符来实现字符串的拼接，
# 可以使用`*`运算符来重复一个字符串的内容，可以使用`in`和`not in`来判断一个字符串是
# 否包含另外一个字符串（成员运算），我们也可以用`[]`和`[:]`运算符从字符串取出某个字符或某些字符（切片运算）
s1 = 'linus '*3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)
str2 = 'abcd123456'
print(str2[2])
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])

# 对字符串的处理
str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1)) # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize()) # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper()) # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('hel')) # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())


# format
a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

a, b = 5, 10
print(f'{a} * {b} = {a * b}')
