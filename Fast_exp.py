from math import pow
from timeit import default_timer as timer

def binaryMultiplicationCount(exponent):
    binary = ""
    while exponent > 0:   
        binary =  binary + str(exponent % 2)
        exponent = exponent//2
    return binary

def binaryExponentiation(x, exponent):
    count = 0
    ans = 1
    hold = x
    mul = 1
    for exp in range(len(exponent)):
        if exponent[exp] == "1":
            if exp == 0:
                ans = x
            else:
                for i in range(mul):
                    hold = hold ** 2
                    count += 1
                ans = ans * hold
                mul = 1
                count += 1
        else:
            if exp != 0:
                mul += 1
    return ans, count

def exponentiation():
    x = int(input("Enter chosen base number: "))
    exponent = int(input("Enter chosen exponent: "))
    
    t1 = timer()
    multipliers = binaryMultiplicationCount(exponent)
    data = binaryExponentiation(x, multipliers)
    t2 = timer()
    t = (t2 - t1) * 10**3
    ans = data[0]
    count = data[1]
    print("The answer to " + str(x) + "^" + str(exponent) + " is ")
    print(ans)
    print()
    print("This was found using " + str(count) + " calculations")
    print("And " + str(t) + " miliseconds")
    print()
    print("Press enter for result using standard method: ")
    input()
    n = 1
    t1 = timer()
    for i in range(1,exponent): 
        n = x * n 
    t2 = timer()
    t = (t2 - t1) * 10**3
    print(n)
    print()
    print("This was found using " + str(exponent - 1) + " calculations")
    print("And " + str(t) + " miliseconds")

exponentiation()
