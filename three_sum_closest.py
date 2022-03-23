class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = float('inf')
        
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            while high > low:
                s = nums[i] + nums[low] + nums[high]
                if abs(diff) > abs(target - s):
                    diff = target - s
                    
                if target < s:
                    high -= 1
                elif target > s:
                    low += 1
                else:
                    return target
        
        return target - diff
