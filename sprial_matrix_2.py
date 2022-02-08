class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0 for _ in range(n)] for _ in range(n)]
        
        count = 1
        for layer in range((n + 1) // 2):
            for i in range(layer, n - layer):
                M[layer][i] = count
                count += 1
                
            for i in range(layer+1, n - layer):


                M[i][n - layer - 1] = count
                count += 1
            
            for i in range(n-layer-2, layer-1, -1):
                M[n-layer-1][i] = count
                count += 1
            
            for i in range(n-layer-2, layer, -1):
                M[i][layer] = count
                count += 1
        
        return M
            
            