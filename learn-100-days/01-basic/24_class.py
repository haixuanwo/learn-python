'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-29 16:27:33
LastEditors: Clark
LastEditTime: 2021-12-29 16:33:49
Description: file content
'''

### 类和对象

# 简单的说，类是对象的蓝图和模板，而对象是类的实例。这个解释虽然有点像用概念在解释概念，
# 但是从这句话我们至少可以看出，类是抽象的概念，而对象是具体的东西。在面向对象编程的世界中，
# 一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类（型）。
# 当我们把一大堆拥有共同特征的对象的静态特征（属性）和动态特征（行为）都抽取出来后，就可以定义出一个叫做“类”的东西。

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)

def main():
    stu1 = Student('海', 32)
    stu1.study('shit了吗')
    stu1.watch_movie()

    stu2 = Student('芳', 31)
    stu2.study('pspsps')
    stu2.watch_movie()

if __name__ == '__main__':
    main()
