class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid) 
        col = len(obstacleGrid[0])
        mem = [[0 for _ in range(col)] for _ in range(row)]
        
        mem[0][0] = 0 if obstacleGrid[0][0] == 1 else 1
        
        for i in range(1, col):
            if mem[0][i-1] == 0 or obstacleGrid[0][i] == 1:
                mem[0][i] = 0
            else:
                mem[0][i] = 1
        
        for i in range(1, row):
            if mem[i-1][0] == 0 or obstacleGrid[i][0] == 1:
                mem[i][0] = 0
            else:
                mem[i][0] = 1
        
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] == 1:
                    mem[i][j] = 0
                else:
                    mem[i][j] = mem[i-1][j] + mem[i][j-1]
        
        return mem[row-1][col-1]
                