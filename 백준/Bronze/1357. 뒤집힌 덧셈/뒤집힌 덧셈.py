import sys

def rev(x) :
    tmp = 0
    while x != 0 :
        tmp = tmp*10 + (x%10)
        x //= 10
    return tmp

a, b = map(int,sys.stdin.readline().split())
print(rev(rev(a)+rev(b)))