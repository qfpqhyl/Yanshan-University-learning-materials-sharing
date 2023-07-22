# coding: utf-8
# author: ztypl
# date:   2018/12/27

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta): # 抽象订阅者
    @abstractmethod
    def update(self, notice): # notice 是一个Notice类的对象
        pass


class Notice:  # 抽象发布者
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self): # 推送
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice): # 具体发布者
    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify() # 推送


class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# Client

notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司今年业绩非常好，给大家发奖金！！！"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = "公司明天放假！！！"
print(s1.company_info)
print(s2.company_info)
