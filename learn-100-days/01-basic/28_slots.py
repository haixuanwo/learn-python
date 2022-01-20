'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-30 11:48:23
LastEditors: Clark
LastEditTime: 2021-12-30 11:54:31
Description: file content
'''

class Person(object):
    # 限定绑定_name, _age, _gender属性
    __slots__ = ('_name', '_age', '_gender')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在看日本大片。' % self._name)
        else:
            print('%s正在看欧美大片。' % self._name)

def main():
    person = Person('谭纳什', 12)
    person.play()
    person._gender = '男'

if __name__ == '__main__':
    main()
