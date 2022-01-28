class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            mem = [0,1]
            for i in range(2,n+1):
                mem.append(mem[-1] + mem[-2])

            return mem[-1]
