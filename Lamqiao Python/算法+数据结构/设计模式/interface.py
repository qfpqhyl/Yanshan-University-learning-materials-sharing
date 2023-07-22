#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1

# class Payment:
#     def pay(self, money):
#         raise NotImplementedError

from abc import ABCMeta, abstractmethod


# 接口
# class Payment(metaclass=ABCMeta):
#     # abstract class
#     @abstractmethod
#     def pay(self, money):
#         pass
#
#
# class Alipay(Payment):
#     def pay(self, money):
#         print("支付宝支付%d元." % money)
#
#
# class WechatPay(Payment):
#     def pay(self, money):
#         print("微信支付%d元." % money)
#
#
#
# p = WechatPay()
# p.pay(100)

#
# class User:
#     def show_name(self):
#         pass
#
# class VIPUser(User):
#     def show_name(self):
#         pass
#
# def show_user(u):
#     res = u.show_name()

class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass


class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print("老虎走路")


class Frog(LandAnimal, WaterAnimal):
    pass
