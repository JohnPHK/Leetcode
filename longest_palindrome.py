class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_length = 0
        longest_pal = ""
        
        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_length:
                    longest_pal = s[l:r+1]
                    longest_length = r - l + 1
                l -= 1
                r += 1
            
            # even
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > longest_length:
                    longest_pal = s[l:r+1]
                    longest_length = r - l + 1
                l -= 1
                r += 1
        
        return longest_pal

