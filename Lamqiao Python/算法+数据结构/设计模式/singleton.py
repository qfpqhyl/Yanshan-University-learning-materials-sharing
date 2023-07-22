#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/12/1

from abc import abstractmethod, ABCMeta

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


a = MyClass(10)
b = MyClass(20)

print(a.a)
print(b.a)
print(id(a), id(b))

