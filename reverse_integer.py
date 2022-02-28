class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: 
            return 0
        
        to_return = 0
        pos = True
        if x < 0:
            pos = False
            x *= -1
        while x > 0: 
            to_return *= 10
            to_return += x % 10
            x //= 10
        
        if to_return >=  2**31-1 or to_return <= -2**31:
            return 0
        
        return to_return if pos else -to_return
            
