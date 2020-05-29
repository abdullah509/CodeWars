
#Project Euler: Problem 1: Multiples of 3 and 5
#If we list all the natural numbers below 10 that
#are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5
#below the provided parameter value number.

def multiplesOf3and5(number):
    num = 0
    answer = 0
    while num < number:
        if num % 3 == 0 or num % 5 == 0:
            answer += num

        num+=1
    print(answer)

multiplesOf3and5(49) #543
multiplesOf3and5(1000) #233168
multiplesOf3and5(8456) #16687353.
multiplesOf3and5(19564) #89301183.
