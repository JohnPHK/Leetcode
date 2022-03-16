class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        firstPassChars = []
        balance = 0
        openSeen = 0
        
        for c in s:
            if c == "(":
                balance += 1
                openSeen += 1
            elif c == ")":
                if balance == 0:
                    continue
                balance -= 1
            firstPassChars.append(c)
        
        result = []
        openToKeep = openSeen - balance
        
        for c in firstPassChars:
            if c == "(":
                if openToKeep <= 0:
                    continue
                openToKeep -= 1
            result.append(c)
        
        return "".join(result)
                
