class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        alpha = string.ascii_lowercase
        res = ""
        
        for i in range(n):
            positionsLeft = (n - i - 1)
            if k > positionsLeft * 26:
                add = k - (positionsLeft * 26)
                res += alpha[add - 1]
                k -= add
            else:
                res += 'a'
                k -= 1
        
        return res
