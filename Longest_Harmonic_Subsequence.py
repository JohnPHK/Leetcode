class Solution:
    def findLHS(self, nums: List[int]) -> int:
        mem = {}
        maxCount = 0 
        for num in nums:
            if num in mem:
                mem[num] += 1
            else:
                mem[num] = 1
            
            if num + 1 in mem:
                maxCount = max(maxCount, mem[num] + mem[num+1])
            if num - 1 in mem:
                maxCount = max(maxCount, mem[num] + mem[num-1])
            
        
        return maxCount
    
