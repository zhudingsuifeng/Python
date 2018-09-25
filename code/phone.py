#!/usr/bin/env python3
#coding=utf-8

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = input()
        # unique character
        n2 = s.count('Z')
        n4 = s.count('W')
        n6 = s.count('U')
        n8 = s.count('X')
        n0 = s.count('G')
        # introduced by known quantity
        n3 = s.count('O')-n2-n4-n6
        n5 = s.count('T')-n0-n4
        n7 = s.count('F')-n6
        n9 = s.count('S')-n8
        n1 = s.count('I')-n7-n8-n0
        print('0'*n0+'1'*n1+'2'*n2+'3'*n3+'4'*n4+'5'*n5+'6'*n6+'7'*n7+'8'*n8+'9'*n9)

