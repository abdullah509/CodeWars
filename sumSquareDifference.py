#Project Euler: Problem 6: Sum square difference
#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural
#numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first n natural numbers
#and the square of the sum.

def sumSquareDifference(n):
    numbers_squared_sum = 0
    numbers_sum = 0
    for i in range(1,n+1):
        numbers_squared_sum += i**2
        numbers_sum += i
    numbers_sum = numbers_sum**2
    answer = numbers_sum - numbers_squared_sum
    return answer

res1 = sumSquareDifference(10) #2640.
res2 = sumSquareDifference(20) #41230.
res3 = sumSquareDifference(100) #25164150.
print(res1,res2,res3)
