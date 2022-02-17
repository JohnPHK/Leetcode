class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        toReturn = []
        
        for i in range(n):
            index = i + 1
            if index % 3 == 0 and index % 5 == 0:
                toReturn.append("FizzBuzz")
            elif index % 3 == 0:
                toReturn.append("Fizz")
            elif index % 5 == 0:
                toReturn.append("Buzz")
            else:
                toReturn.append(str(i+1))
        return toReturn