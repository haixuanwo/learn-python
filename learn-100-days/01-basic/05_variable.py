'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-25 11:20:43
LastEditors: Clark
LastEditTime: 2021-12-25 11:52:45
Description: file content
'''

a = 321
b = 12
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# type()检查变量的类型
c = 'tanxiaohai'
print(type(a))
print(type(c))

# `int()`：将一个数值或字符串转换成整数，可以指定进制。
# `float()`：将一个字符串转换成浮点数。
# `str()`：将指定的对象转换成字符串形式，可以指定编码。
# `chr()`：将整数转换成该编码对应的字符串（一个字符）。
# `ord()`：将字符串（一个字符）转换成对应的编码（整数）。

# 使用input()函数获取键盘输入(字符串)
# 使用int()函数将输入的字符串转换成整数
# 使用print()函数输出带占位符的字符串

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' %(a, b, a+b))
print('%d - %d = %d' %(a, b, a-b))
print('%d * %d = %d' %(a, b, a*b))
print('%d / %d = %d' %(a, b, a/b))
print('%d %% %d = %d' %(a, b, a%b))
print('%d ** %d = %d' %(a, b, a**b))

# | 运算符                                                       | 描述                           |
# | ------------------------------------------------------------ | ------------------------------ |
# | `[]` `[:]`                                                   | 下标，切片                     |
# | `**`                                                         | 指数                           |
# | `~` `+` `-`                                                  | 按位取反, 正负号               |
# | `*` `/` `%` `//`                                             | 乘，除，模，整除               |
# | `+` `-`                                                      | 加，减                         |
# | `>>` `<<`                                                    | 右移，左移                     |
# | `&`                                                          | 按位与                         |
# | `^` `\|`                                                      | 按位异或，按位或               |
# | `<=` `<` `>` `>=`                                            | 小于等于，小于，大于，大于等于 |
# | `==` `!=`                                                    | 等于，不等于                   |
# | `is`  `is not`                                               | 身份运算符                     |
# | `in` `not in`                                                | 成员运算符                     |
# | `not` `or` `and`                                             | 逻辑运算符                     |
# | `=` `+=` `-=` `*=` `/=` `%=` `//=` `**=` `&=` `|=` `^=` `>>=` `<<=` | （复合）赋值运算符             |

a += b;
print(a)

### 比较运算符和逻辑运算符
# 比较运算符有的地方也称为关系运算符，包括`==`、`!=`、`<`、`>`、`<=`、`>=`，我相信没有什么好解释的，大家一看就能懂，
# 唯一需要提醒的是比较相等用的是`==`，请注意这个地方是两个等号，因为`=`是赋值运算符，我们在上面刚刚讲到过，`==`才是比较相等的比较运算符。
# 比较运算符会产生布尔值，要么是`True`要么是`False`。
# 逻辑运算符有三个，分别是`and`、`or`和`not`。`and`字面意思是“而且”，所以`and`运算符会连接两个布尔值，如果两个布尔值都是`True`，
# 那么运算的结果就是`True`；左右两边的布尔值有一个是`False`，最终的运算结果就是`False`。相信大家已经想到了，
# 如果`and`左边的布尔值是`False`，不管右边的布尔值是什么，最终的结果都是`False`，所以在做运算的时候右边的值会被跳过（短路处理），
# 这也就意味着在`and`运算符左边为`False`的情况下，右边的表达式根本不会执行。`or`字面意思是“或者”，所以`or`运算符也会连接两个布尔值，
# 如果两个布尔值有任意一个是`True`，那么最终的结果就是`True`。当然，`or`运算符也是有短路功能的，在它左边的布尔值为`True`的情况下，
# 右边的表达式根本不会执行。`not`运算符的后面会跟上一个布尔值，它的作用是得到与该布尔值相反的值，也就是说，后面的布尔值如果是`True`运算结果就是`False`，
# 而后面的布尔值如果是`False`则运算结果就是`True`。

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1!=2)
print('flag0 =', flag0)
print('flag1 =', flag1)
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =', flag5)



