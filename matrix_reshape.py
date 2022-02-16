class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        res = [[0 for _ in range(c)] for _ in range(r)]
        print(res)
        
        count = 0 
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                res[count // c][count % c] = mat[i][j]
                count += 1
        
        return res
                
                
        
        