#Project Euler: Problem 20: Factorial digit sum
#n! means n × (n − 1) × ... × 3 × 2 × 1

#For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
#and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

#Find the sum of the digits n!

def multiply(number):
    total = 1
    for x in number:
        total *= x
    return total

def sumFactorialDigits(n):
    numbers = []
    answer = []

    for i in range(1, n+1):
        numbers.append(i)

    add = multiply(numbers)
    answer.append(add)
    output = list(map(int, str(answer[0])))

    return sum(output)

res1 = sumFactorialDigits(10)
res2 = sumFactorialDigits(25)
res3 = sumFactorialDigits(50)
res4 = sumFactorialDigits(75)
res5 = sumFactorialDigits(100)

print(res1,res2,res3,res4,res5)
