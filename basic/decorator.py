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

# We can not call the __call__ function if we not init the class
class make_bold(object):
    def __init__(self):
        pass

    def __call__(self, func):
        #@wraps(self.func)
        def inner2():
            return '<b>{}</b>'.format(func())
            print("success")
        return inner2
        
class class_test:
    @classmethod
    def test(cls, func):
        @wraps(func)
        def inner1():
            return '<b>{}</b>'.format(func())
        return inner1

temp = make_bold()
# Every functions could be the decorator
#@class_test.test
#@make_bold
@temp
def get_content():
    #print(get_content.__name__)
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
