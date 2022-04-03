class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        pivot = -1
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                pivot = i
                
                
        if pivot == -1:
            nums.sort()
            return
        
        j = pivot + 1
        nextPivotValue = 101
        nextPivotIndex = -1
        

        while j < len(nums):
            if nums[pivot] < nums[j] and nums[j] <= nextPivotValue:
                nextPivotValue = nums[j]
                nextPivotIndex = j
            j += 1
        
        
        if nextPivotIndex != -1:
            nums[pivot], nums[nextPivotIndex] = nums[nextPivotIndex], nums[pivot]
        
        
        # reverse
        start = pivot + 1
        end = len(nums) - 1
        
        while end > start:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        
        return