class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        
        n = len(matrix[0])
        
        left, right = 0, (m * n) - 1
        
        while left <= right:
            pivot = (left + right) // 2
            pivotElement = matrix[pivot // n][pivot % n]
            if target == pivotElement:
                return True
            else:
                if target < pivotElement:
                    right = pivot - 1
                else:
                    left = pivot + 1
        
        return False
