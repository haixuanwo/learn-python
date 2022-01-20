'''
Author: Clark
Email: haixuanwoTxh@gmail.com
Date: 2021-12-30 15:21:37
LastEditors: Clark
LastEditTime: 2021-12-30 19:52:07
Description: file content
'''

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    # 战斗者
    # 通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp # 生命值

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self, other):
        pass

    # @abstractmethod
    # def magic_attack(self, others):
    #     pass

class Ultraman(Fighter):
    # 奥特曼
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        # 究极必杀技
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        # 魔法攻击
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive():
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        # 恢复魔法值
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~~~%s奥特曼~~~~\n' % self._name + \
            '生命值: %d\n' % self._hp + \
            '魔法值: %d\n' % self._mp

class Monster(Fighter):
    # 小怪兽
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~~\n' % self._name + \
            '生命值: %d\n' % self._hp

def is_any_alive(monsters):
    # 是否有小怪兽活着
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    # 选一只活小怪兽
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    # 显示奥特曼和小怪兽信息
    print(ultraman)
    for monster in monsters:
        print(monster, end='')

def main():
    ultraman = Ultraman('谭恒', 1000, 120)
    monster1 = Monster('海', 250)
    monster2 = Monster('芳', 150)
    monster3 = Monster('玉', 50)
    monsters = [monster1, monster2, monster3]

    fight_round = 1
    while ultraman.alive and is_any_alive(monsters):
        print('===第%02d回合===' % fight_round)
        m = select_alive_one(monsters)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (ultraman.name, m.name))
            ultraman(m)
            print('%s的魔法值恢复了%d点' % (ultraman.name, ultraman.resume()))
        elif skill <= 9:
            if ultraman.magic_attack(m):
                print('%s使用了魔法攻击.' % ultraman.name)
            else:
                print('%s使用了魔法失败.' % ultraman.name)
        else:
            if ultraman.huge_attack(m):
                print('%s使用究极必杀技掠了%s.' % (ultraman.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (ultraman.name, m.name))
                print('%s的魔法值恢复了%d点.' % (ultraman.name, m.name))

        if m.alive > 0:
            print('%s回击了%s.' % (m.name, ultraman.name))
            m.attack(ultraman)

        display_info(ultraman, monsters)
        fight_round += 1

    print('\n================战斗结束================\n')
    if ultraman > 0:
        print('%s奥特曼胜利!' % ultraman.name)
    else:
        print('小怪兽胜利!')

if __name__ == '__main__':
    main()

