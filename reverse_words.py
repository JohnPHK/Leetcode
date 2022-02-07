class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(s):
            rev = ""
            for ch in s:
                rev = ch + rev
            return rev
        
        rev_sent = ""
        tmp = s.split(" ")
        print(tmp)
        for word in tmp:
            rev_sent += reverse(word)
            rev_sent += " "
        
        return rev_sent[:-1]
