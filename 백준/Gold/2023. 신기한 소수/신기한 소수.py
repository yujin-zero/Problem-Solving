import sys

def isPrime(x) :
    for i in range(2,int(x**0.5) + 1) :
        if x%i == 0 :
            return False
    return True

def wow(idx, num) :
    if isPrime(num) :
        if idx == n :
            print(num)
        else: 
            wow(idx+1, num*10+1)
    if num%10 != 9 :
        wow(idx, num+1)

n = int(sys.stdin.readline())
wow(1,2)
