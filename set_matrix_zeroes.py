class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zerosRow = []
        zerosCol = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zerosRow.append(i)
                    zerosCol.append(j)
        
        print(zerosRow)
        print(zerosCol)
        
        for row in zerosRow:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        
        for col in zerosCol:
            for i in range(len(matrix)):
                matrix[i][col] = 0
        
        return
            