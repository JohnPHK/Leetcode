import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(n):
            mem[0][i] = 1
        
        for i in range(m):
            mem[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                mem[i][j] = mem[i-1][j] + mem[i][j-1]
        
        return mem[m-1][n-1]
        