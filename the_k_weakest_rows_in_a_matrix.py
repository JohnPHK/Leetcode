class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        
        for j in range(n):
            for i in range(m):
                if mat[i][j] == 0 and (j == 0 or mat[i][j-1] == 1):
                    res.append(i)
                if len(res) == k:
                    break
            if len(res) == k:
                break
        
        
        i = 0
        while len(res) < k:
            if mat[i][-1] == 1:
                res.append(i)
            i += 1
        
        return res
