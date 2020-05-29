#Project Euler: Problem 10: Summation of primes
#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below n.

def primeSummation(n): #Function name
    numberList = [2]   #2 is the only even prime number so we add it to list
    num = 3            #We start at 3
    while num < n:     #While num is less than n which is the number in function
        for i in numberList: #index in numberList
            if num % i == 0:
                break
        else:
            numberList.append(num) #Add the prime number to the list
        num+=2 #No even number is prime except 2 so we add 2 to num
               #Which is 3 to start
    return "The sum of the prime numbers is: ", sum(numberList)
    #sum() adds all the elements in the list

res1 = primeSummation(17) #41.
res2 = primeSummation(2001) #277050.
#res3 = primeSummation(140759) #873608362.
#res4 = primeSummation(2000000) #142913828922.

print(res1,res2)
