#Write a function, persistence, that takes in a positive parameter num
 #and returns its multiplicative persistence,
 #which is the number of times you must multiply the digits in num until you reach a single digit.
#EXAMPLE
# persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 #persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 #persistence(4) => 0   # Because 4 is already a one-digit number.


def persistence(n):
    # your code

    if n < 10:
        return 0
    n_str = str(n)
    total = 1
    for x in n_str:
        total = total * int(x)
    return 1 + persistence(total)


    #Sample Tests:
1
Test.it("Basic tests")
2
Test.assert_equals(persistence(39), 3)
3
Test.assert_equals(persistence(4), 0)
4
Test.assert_equals(persistence(25), 2)
5
Test.assert_equals(persistence(999), 4)
