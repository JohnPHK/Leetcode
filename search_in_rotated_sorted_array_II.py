class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def binarySearch(lst, t):
            high = len(lst) - 1
            low = 0
            mid = (high + low) // 2
            print("lst:", lst)
            while high > low:
                mid = (high + low) // 2
                if lst[mid] > t:
                    high = mid
                elif lst[mid] < t:
                    low = mid + 1
                else:
                    return True
            
            return False or lst[low] == t
        
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                return binarySearch(nums[:i], target) or\
                       binarySearch(nums[i:], target)
        return binarySearch(nums, target)
