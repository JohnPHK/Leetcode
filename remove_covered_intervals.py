class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: (x[0], -x[1]))
        
        count = 1
        i, j = 0, 1
        while j < len(intervals):
            if intervals[i][1] < intervals[j][1]:
                count += 1
                i = j                
            j+=1
        return count
            