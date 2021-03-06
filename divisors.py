# Create a function named divisors/Divisors that takes an
# integer n > 1 and returns an array with all of the integer's
# divisors(except for 1 and the number itself), from smallest
# to largest. If the number is prime return the string '(integer)
# is prime'

# examples
# divisors(12); #should return [2,3,4,6]
# divisors(25); #should return [5]
# divisors(13); #should return "13 is prime"

# https://www.codewars.com/kata/find-the-divisors/python

def divisors(integer):
    array = []
    for x in range(2, integer - 1):
        if integer % x == 0:
            array.append(x)

    if len(array) == 0:
        return str(integer) + " is prime"
    else:
        return array


# Tests
Test.assert_equals(divisors(15), [3, 5]);
Test.assert_equals(divisors(12), [2, 3, 4, 6]);
Test.assert_equals(divisors(13), "13 is prime");
