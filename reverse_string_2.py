from typing import List

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reversed_str = ""
        if len(s) < k:
            for c in s:
                reversed_str = c + reversed_str
            return reversed_str
        elif len(s) >= k and len(s) < 2 * k:
            for i in range(k):
                reversed_str = s[i] + reversed_str
            return reversed_str + s[k:]
        else:
            for i in range(k):
                reversed_str = s[i] + reversed_str
            return reversed_str + s[k:2*k] + self.reverseStr(s[2*k:], k)
                
                