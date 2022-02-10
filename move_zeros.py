class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rep = 0
        
        for i in range(len(nums)):
            if 0 != nums[i]:
                nums[rep], nums[i] = nums[i], nums[rep]
                rep += 1
