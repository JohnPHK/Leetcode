class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        mem = {}
        for i in range(numRows):
            mem[i] = ''
        
        change = -1
        row = 0
        for ch in s:
            mem[row] += ch
            if (row == 0 or row == numRows - 1):
                change *= -1
            row += change
        
        res = ''
        for i in range(numRows):
            res += mem[i]
        
        
        return res

if __name__ == "__main__":
    print("test")
