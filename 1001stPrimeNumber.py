#Project Euler: Problem 7: 10001st prime
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the nth prime number?

def nthPrime(n):
    prime_list = [2] #2 is a prime number
    num = 3 #so we start from 3
    while len(prime_list) < n: #we do not need to check against numbers > n
                               #as it is not going to be able to be divide by it
        for i in prime_list:  #index in prime list
            if num % i == 0:  # checking if number is not prime
                break
        else:
            prime_list.append(num) #if it is prime then add it do the list
        num += 2 #+2 because no even number is prime except 2 which is already
                 #on the list
    return prime_list[-1] #To find the last element in the list


res1 = nthPrime(6) #13
res2 = nthPrime(10)  #29.
res3 = nthPrime(100)  #541.
res4 = nthPrime(1000) #7919.
res5 = nthPrime(10001) #104743.
print(res1,res2,res3,res4,res5)
