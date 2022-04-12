class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        tmp = []
        numRows = len(grid)
        numCols = len(grid[0])
        k = k % (numRows * numCols)
        
        for i in range(numRows):
            for j in range(numCols):
                tmp.append(grid[i][j])
        
        tmp = tmp[len(tmp) - k:] + tmp[:len(tmp)-k]
        
        print(tmp)
        
        toReturn = []
        for i in range(numRows):
            toReturn.append([tmp[j+(numCols*i)] for j in range(numCols)])
        
        return toReturn
                