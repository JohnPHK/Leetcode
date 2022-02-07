class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo = 0
        hi = len(numbers) - 1
        
        while lo < hi:
            summed = numbers[hi] + numbers[lo]
            if summed > target:
                hi -= 1
            elif summed < target:
                lo += 1
            else:
                return lo+1, hi+1
            
        return -1, -1
        
