#!/usr/bin/env python3
#coding = utf-8

class Replacement:
    def replaceSpace(self, iniString, length):
        return iniString.replace(' ', '%20')

if __name__ == "__main__":
    s = input()
    p = Replacement()
    print(p.replaceSpace(s, len(s)))
