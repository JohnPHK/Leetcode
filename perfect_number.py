def checkPerfectNumber(num: int) -> bool:
    if num <= 1:
        return False
    divisors = [1]
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            divisors.append(i)
            divisors.append(num//i)
    
    return sum(divisors) == num

if __name__ == "__main__":
    print(checkPerfectNumber(6))