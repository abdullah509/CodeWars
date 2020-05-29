#Project Euler: Problem 2: Even Fibonacci Numbers
#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed n,
#find the sum of the even-valued terms.

def fiboEvenSum(n):
    sum = 0
    a, b = 0,1  #a=0 b=1
    while b < n:
        a, b = b, a+b  # a = b and b = a+b
        if b % 2 == 0:
            sum+=b
    return sum


res1 = fiboEvenSum(10) #10.
res2 = fiboEvenSum(60) #44.
res3 = fiboEvenSum(1000) #798.
res4 = fiboEvenSum(100000) #60696.
res5 =fiboEvenSum(4000000) #4613732.

print(res1,res2,res3,res4,res5)