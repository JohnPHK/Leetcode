class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        tmp = score.copy()
        mem = {}
        tmp.sort(reverse=True)
        
        for i in range(1,len(tmp) + 1):
            if i == 1:
                mem[tmp[i-1]] = "Gold Medal"
            elif i == 2:
                mem[tmp[i-1]] = "Silver Medal"
            elif i == 3:
                mem[tmp[i-1]] = "Bronze Medal"
            else:
                mem[tmp[i-1]] = str(i)
            
            
        to_return = []
        for i in score:
            to_return.append(mem[i])
        
        return to_return
