class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        mem = [[0 for _ in range(col)] for _ in range(row)]
        
        mem[0][0] = grid[0][0]
        
        for i in range(1, col):
            mem[0][i] = mem[0][i-1] + grid[0][i]
        
        for i in range(1, row):
            mem[i][0] = mem[i-1][0] + grid[i][0]
        
        for i in range(1, row):
            for j in range(1, col):
                mem[i][j] = min(mem[i-1][j], mem[i][j-1]) + grid[i][j]
            
        
        return mem[row - 1][col - 1]