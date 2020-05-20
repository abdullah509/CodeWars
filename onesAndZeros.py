#Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.


def binary_array_to_number(arr):
  # your code
  result = 0
  index = 0
  value = 2 ** (len(arr) - 1)
  while index < len(arr):
    if arr[index] == 1:
      result += value
    index += 1
    value /= 2
  return result
  #Sample Tests:
#1
Test.describe("One's and Zero's")
#2
Test.it("Example tests")
#3
Test.assert_equals(binary_array_to_number([0,0,0,1]), 1)
#4
Test.assert_equals(binary_array_to_number([0,0,1,0]), 2)
#5
Test.assert_equals(binary_array_to_number([1,1,1,1]), 15)
#6
Test.assert_equals(binary_array_to_number([0,1,1,0]), 6)
