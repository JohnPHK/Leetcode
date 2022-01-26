class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        base7 = ''
        if num < 0:
            num *= -1
            while num > 0:
                base7 = str(num%7) + base7
                num //= 7
            base7 = '-' + base7
        else: 
            while num > 0:
                base7 = str(num % 7) + base7
                num //= 7

        return base7
