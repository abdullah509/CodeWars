#Given an array, find the int that appears an odd number of times.
#There will always be only one integer that appears an odd number of times.

#My solution

from collections import Counter

def find_it(seq):
    count = Counter(seq)

    for x in count:
        if count[x] % 2 != 0:
          return x

#Sample Tests:
#1
#test.describe("Example")
#2
#test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
