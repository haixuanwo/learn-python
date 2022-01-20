'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-30 11:39:26
LastEditors: Clark
LastEditTime: 2021-12-30 11:47:01
Description: file content
'''

# 通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
# 如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法

class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在看日本大片.' % self._name)
        else:
            print('%s正在看欧美大片.' % self._name)

def main():
    person = Person('谭孝海', 32)
    person.play()
    person.age = 15
    person.play()

if __name__ == '__main__':
    main()
