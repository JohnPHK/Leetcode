class Solution:
    def validPalindrome(self, s: str) -> bool:
        def validPalindromeHelper(subS):
            lo = 0
            hi = len(subS) - 1
            
            while hi > lo:
                if subS[hi] != subS[lo]:
                    return False
                else:
                    hi -= 1
                    lo += 1
            
            return True
        
        high = len(s) - 1
        low = 0
        
        while high > low:
            if s[high] != s[low]:
                return validPalindromeHelper(s[low:high]) or validPalindromeHelper(s[low+1: high+1])
            else:
                high -= 1
                low += 1
        
        return True
            
                