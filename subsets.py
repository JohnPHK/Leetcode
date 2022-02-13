class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        mem = [[]]
        
        for i in range(len(nums)):
            original = mem.copy()
            for s in original:
                tmp.append(nums[i])
                mem += [tmp]
        
        
        return mem
       
