#!/usr/bin/env python3
#coding = utf-8

from functools import wraps

def f1(fun):
    @wraps(fun)
    def inner1():
        return '<b>' + fun() + '</b>'
    return inner1

def f2(fun):
    @wraps(fun)
    def inner2():
        return '<i>' + fun() + '</i>'
    return inner2

@f1
@f2
def test():
    print(test.__name__)
    return 'hello python decorator'

class make_bold(object):
    def __init__(self, func):
        self.__name__ = make_bold
        self.func = func
    def __call__(self):
        return '<b>{}</b>'.format(self.func())

@make_bold
def get_content():
    print(get_content.__name__)
    return 'hello world'

def h():
    print("func")

def outer():
    print('Before def:',locals())
    def inner():
        pass
    print('After def:',locals())
    return inner

if __name__ == "__main__":
    #print(test())
    #print(id(h))
    print(get_content())
