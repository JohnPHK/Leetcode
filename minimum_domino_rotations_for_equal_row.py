class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tmp = []
        
        for num in range(1,7): 
            topCount = 0
            botCount = 0
            record = True
            for i in range(len(tops)):
                if bottoms[i] != num and tops[i] != num:
                    record = False
                    break
                if bottoms[i] == num or tops[i] == num:
                    if bottoms[i] == num and tops[i] != num:
                        topCount += 1
                    if bottoms[i] != num and tops[i] == num:
                        botCount += 1
                    
            if record:
                tmp.append(topCount)
                tmp.append(botCount)
        print(tmp)
        if len(tmp) > 0:
            return min(tmp)
        else:
            return -1
                        
                    
                    
