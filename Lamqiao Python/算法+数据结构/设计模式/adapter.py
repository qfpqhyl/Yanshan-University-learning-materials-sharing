#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)



class BankPay:
    def cost(self, money):
        print("银联支付%d元." % money)


class ApplePay:
    def cost(self, money):
        print("苹果支付%d元." % money)


# # 类适配器
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)


# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = PaymentAdapter(BankPay())
p.pay(100)


# 组合

# class A:
#     pass
#
# class B:
#     def __init__(self):
#         self.a = A()
