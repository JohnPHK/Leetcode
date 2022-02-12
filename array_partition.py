class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        tmp = []
        summed = 0
        for i in range(0, len(nums), 2):
            tmp.append((nums[i], nums[i+1]))
        
        for pair in tmp:
            summed += min(pair)
        
        return summed
