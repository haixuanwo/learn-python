'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-30 15:08:32
LastEditors: Clark
LastEditTime: 2021-12-30 15:16:24
Description: file content
'''

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):
    def make_voice(self):
        print('%s: 汪汪。。。' % self._nickname)

class Cat(Pet):
    def make_voice(self):
        print('%s: 喵喵。。。' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('阿花'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()

# 通过`abc`模块的`ABCMeta`元类和`abstractmethod`包装器来达到抽象类的效果，如果一个类中存在抽象方法
# 那么这个类就不能够实例化（创建对象）。上面的代码中，`Dog`和`Cat`两个子类分别对`Pet`类中的`make_voice`
# 抽象方法进行了重写并给出了不同的实现版本，当我们在`main`函数中调用该方法时，这个方法就表现出了多态行为（同样的方法做了不同的事情）。

