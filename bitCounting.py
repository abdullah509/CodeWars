#Write a function that takes an integer as input,
#and returns the number of bits that are equal to
#one in the binary representation of that number.
#You can guarantee that input is non-negative.

#Example: The binary representation of 1234 is 10011010010,
#so the function should return 5 in this case.

#My solution.
def countBits(n):
    return bin(n).count('1') #bin() converts decimal value to corresponding binary value

    print(countBits(1234))

#Sample Tests:
#1
#test.assert_equals(countBits(0), 0);
#2
#test.assert_equals(countBits(4), 1);
#3
#test.assert_equals(countBits(7), 3);
#4
#test.assert_equals(countBits(9), 2);
#5
#test.assert_equals(countBits(10), 2);
