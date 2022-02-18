class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def generate(comb, l, r):
            if len(comb) == 2*n:
                res.append("".join(comb))
                return
            
            if l < n:
                comb.append("(")
                generate(comb, l+1, r)
                comb.pop()
            if r < l:
                comb.append(")")
                generate(comb, l, r+1)
                comb.pop()
        
        generate([], 0, 0)
        
        return res
