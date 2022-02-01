from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        to_return = []
        
        for interval in intervals:
            if len(to_return) == 0:
                to_return.append(interval)
            else:
                if interval[0] <= to_return[-1][1]:
                    to_return[-1][1] = max(interval[1], to_return[-1][1])
                else:
                    to_return.append(interval)
        
        return to_return
            
            