#Project Euler: Problem 3: Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the given number?




def isPrime(n):
    for i in range(3,n):
        if n % i == 0:
            return False
    return True

def largestPrimeFactor(number):

    if number % 2 == 0:
        step1 = int(number / 2)
        if isPrime(step1):
            return step1
        else:
            return largestPrimeFactor(step1)
    divide = 3
    while(True):
        if number % divide == 0:
            step1 = int(number / divide)
            if isPrime(step1):
                return step1
            else:
                return largestPrimeFactor(step1)
        else:
            divide += 2
            while(isPrime(divide) is False):
                divide+=2




res1 = largestPrimeFactor(13195) #29.
res2 = largestPrimeFactor(600851475143) #6857.
print(res1,res2)
