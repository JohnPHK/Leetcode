class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        limit = len(candyType) / 2
        count = 0
        candyType.sort()
        
        for i in range(len(candyType)):
            if i > 0 and candyType[i] == candyType[i-1]:
                continue
            else:
                count += 1
                if count >= limit:
                    break
        
        return count