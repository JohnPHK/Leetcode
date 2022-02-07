class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mem_s = {}
        mem_t = {}
        for c in s:
            if c in mem_s:
                mem_s[c] +=1
            else:
                mem_s[c] = 1
        
        for c in t:
            if c in mem_t:
                mem_t[c] += 1
            else:
                mem_t[c] = 1
        
        for c in mem_t:
            if c not in mem_s or mem_t[c] > mem_s[c]:
                return c
        return ''
