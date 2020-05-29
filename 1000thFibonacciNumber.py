#Project Euler: Problem 25: 1000-digit Fibonacci number
#The Fibonacci sequence is defined by the recurrence relation:

#Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#Hence the first 12 terms will be:

#F1 = 1
#F2 = 1
#F3 = 2
#F4 = 3
#F5 = 5
#F6 = 8
#F7 = 13
#F8 = 21
#F9 = 34
#F10 = 55
#F11 = 89
#F12 = 144
#The 12th term, F12, is the first term to contain three digits.

#What is the index of the first term in the Fibonacci sequence to contain n digits?

def digitFibonacci(n):
    result = 2
    a = 1
    b = 1
    c = 0
    length = 1
    while(length < n):
        result = result + 1
        c = a+b
        a = b
        b = c
        length = len(str(c))
    return result


digitFibonacci(5) #21.
digitFibonacci(10) #45.
digitFibonacci(15) #69.
digitFibonacci(20) #93
