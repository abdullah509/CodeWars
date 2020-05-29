#Project Euler: Problem 16: Power digit sum
#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2exponent?

def powerDigitSum(exponent):
    powerList = []
    answer = 2**exponent
    #32768
    anstring = str(answer)
    powerList.append(answer)
    output = list(map(int, str(powerList[0])))

    return sum(output)


res1 = powerDigitSum(15) # 26
res2 = powerDigitSum(128) #166.
res3 = powerDigitSum(1000) #1366.

print(res1,res2,res3)
