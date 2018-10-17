#!/usr/bin/env python3
#coding = utf-8

class Reverse:
    @classmethod
    def reverseString(cls, iniString):
        return iniString[::-1]

if __name__ == "__main__":
    s = input()
    print(Reverse.reverseString(s))
