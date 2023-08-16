import sys

n = int(sys.stdin.readline())

zero = 0
one = 1
for _ in range(n-1):
    temp = one
    one = zero
    zero += temp
print(one+zero)
