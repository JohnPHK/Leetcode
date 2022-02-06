class Solution:
    def checkRecord(self, s: str) -> bool:
        absents = 0
        con_lates = 0
        for c in s:
            if c == 'A':
                absents += 1
                con_lates = 0
            elif c == 'L':
                con_lates += 1
            else:
                con_lates = 0
            
            
            
            if absents >= 2 or con_lates >= 3:
                return False
        return True
            
