class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        for j in range(len(nums)):
            if j < len(nums) - 1 and nums[j+1] - nums[j] == 1:
                continue
            else:
                if i == j:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[i]) + "->" + str(nums[j]))
                i = j + 1
        
        return res
                
