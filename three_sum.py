class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def twoSum(nums, target):
            res = []
            lo = 0
            hi = len(nums)-1
            while hi > lo:
                if target + nums[hi] + nums[lo] < 0:
                    lo += 1
                elif target + nums[hi] + nums[lo] > 0:
                    hi -= 1
                else:
                    res.append([nums[hi], nums[lo]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
            return res
        
        for i in range(len(nums)-2):
            if i == 0 or nums[i-1] != nums[i]:
                for tmp in twoSum(nums[i+1:], nums[i]):
                    tmp.append(nums[i])
                    res.append(tmp)
        return res