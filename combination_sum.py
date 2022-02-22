from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(candidates, start, comb):
        print(comb)
        remainder = target - sum(comb)
        if remainder < 0:
            return
        elif remainder == 0:
            res.append(list(comb))
            return
        else:
            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(candidates, i, comb)     
                comb.pop()
        
    res = []
    backtrack(candidates, 0, [])
    return res
    

if __name__ == '__main__':
    combinationSum([3, 4, 5], 8)