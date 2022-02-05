class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        arr = [-2 for _ in range(2 * len(nums) + 1)]
        arr[len(nums)] = -1
        maxlen = 0
        count = 0
        for i in range(len(nums)):
            count = count - 1 if nums[i] == 0 else count + 1
            if arr[count + len(nums)] >= -1:
                maxlen = max(maxlen, i - arr[count + len(nums)])
            else:
                arr[count + len(nums)] = i
        return maxlen
        
            
