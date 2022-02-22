from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = []
        if len(intervals) == 0:
            return [newInterval]
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            inserted.append(intervals[i])
            i += 1
        
        while i < len(intervals) and ((intervals[i][1] >= newInterval[0] and intervals[i][1] <= newInterval[0]) or (intervals[i][0] <= newInterval[1])):
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        inserted.append(newInterval)
        while i < len(intervals):
            inserted.append(intervals[i])
            i += 1
        return inserted
            
        
        
        