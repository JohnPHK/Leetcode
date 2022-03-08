class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(comb, start):
            if len(comb) == k:
                res.append(list(comb))
                return
            
            for i in range(start, n+1):
                comb.append(i)
                backtrack(comb, i+1)
                comb.pop()
        
        res = []
        backtrack([], 1)
        return res
            