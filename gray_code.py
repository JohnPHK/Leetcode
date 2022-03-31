class Solution:
    def grayCode(self, n: int) -> List[int]:
        def grayCodeHelper(result, k):
            if k == 0:
                result.append(0)
                return
            
            grayCodeHelper(result, k - 1)
            mask = 1 << (k-1)
            for i in range(len(result) - 1, -1, -1):

                result.append(result[i] | mask)
        
        res = []
        grayCodeHelper(res,n)
        return res