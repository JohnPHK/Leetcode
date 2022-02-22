class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        _dict = {}
        for i, letter in enumerate(string.ascii_uppercase):
            _dict[letter] = i+1
        res = 0
        for i in range(len(columnTitle) -1, -1, -1):
            
            res += _dict[columnTitle[i]] * (26 ** (len(columnTitle) - 1 - i))
        
        return res
            