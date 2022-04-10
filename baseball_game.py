class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scoresBuffer = []
        for i in range(len(ops)):
            if ops[i] == "+":
                scoresBuffer.append(scoresBuffer[-1] + scoresBuffer[-2])
            elif ops[i] == "D":
                scoresBuffer.append(scoresBuffer[-1] * 2)
            elif ops[i] == "C":
                scoresBuffer.pop()
            else:
                scoresBuffer.append(int(ops[i]))
        
        return sum(scoresBuffer)