#!/usr/bin/env python3
#coding = utf-8

class Solution:
    # 自上而下
    def miniTotal(self, triangle: [[int]]) -> int:
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i and j and j < len(triangle[i])-1:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
                if i and not j:
                    triangle[i][j] += triangle[i-1][j]
                if i and j == len(triangle[i])-1:
                    triangle[i][j] += triangle[i-1][j-1]
        print(triangle)
        return min(triangle[-1])

    # 自下而上
    def minimumTotal(self, triangle: [[int]]) -> int:
        for i in range(len(triangle)-2, -1, -1):  # 注意边界问题
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

if __name__ == "__main__":
    n = int(input())
    t = [ list(map(int, input().split())) for i in range(n)]
    s = Solution()
    print(s.minimumTotal(t))
