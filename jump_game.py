from typing import List


# Dyanmic Algorithm solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = [0 for _ in range(len(nums))]
        mem[-1] = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                mem[i] = 1
            else:
                for j in range(i+1, i + nums[i]+1):
                    if mem[j] == 1:
                        mem[i] = 1
                        break
                if mem[i] == 0:
                    mem[i] = -1
                
        
        return mem[0] == 1
                
# Greedy solution
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_position:
                last_position = i
        
        return last_position == 0
