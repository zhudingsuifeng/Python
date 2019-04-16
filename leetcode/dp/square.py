#!/usr/bin/env python3
#coding = utf-8

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i and j:
                    grid[i][j] += min(grid[i][j-1], grid[i-1][j])
                elif i:
                    grid[i][j] += grid[i-1][j]
                elif j:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]
    
    def myPathSum(self, grid: [[int]]) -> int:
        test = [[0]*3]*4   # Python 赋值，copy,deepcopy 使用[[0]]*n形式生成的高维list，每个维度之间共用一个内存空间，改变之后都会变
        test[0][1] = 1
        print(test)

if __name__ == "__main__":
    m = int(input())
    grid = []
    for i in range(m):
        grid.append(list(map(int, input().split())))
    s = Solution()
    print(s.minPathSum(grid))
    # s.myPathSum(grid)
