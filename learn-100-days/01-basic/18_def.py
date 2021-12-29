'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 12:45:23
LastEditors: Clark
LastEditTime: 2021-12-29 14:55:18
Description: file content
'''

### 定义函数

# 在Python中可以使用`def`关键字来定义函数，和变量一样每个函数也有一个响亮的名字，而且命名规则跟变量的命名规则是一致的。
# 在函数名后面的圆括号中可以放置传递给函数的参数，这一点和数学上的函数非常相似，程序中函数的参数就相当于是数学上说的函数
# 的自变量，而函数执行完成后我们可以通过`return`关键字来返回一个值，这相当于数学上说的函数的因变量。

from random import randint

def add(a=0, b=0, c=0):
    return a+b+c

print(add(1,2,3))

# 可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

print(add(5,6,7,8))

# 模块管理函数 import
# module1.py
# def foo():
#     print('hello1')

# module2.py
# def foo():
#     print('hello2')

# from module1 import foo
# import module1 as m1
# m1.foo()

# 需要说明的是，如果我们导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
# 事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话
# 除非直接运行该模块，if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是&quot;\_\_main\_\_&quot;。

# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('hello, linus')

### 变量的作用域
def foo():
    global a # 指示全局变量
    a = 200
    print(a)
