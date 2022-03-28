class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        numOfOperations = 0
        while target > startValue:
            numOfOperations += 1
            if target % 2: target += 1
            else: target //= 2
        
        return numOfOperations + startValue - target
        
