import sys

x = int(sys.stdin.readline())

n = 1
while n**2 + n < 2*x:
    n += 1
# n번째 대각선행에 위치헤 있음

k = (n-1)*n/2 + 1
if n % 2 == 0:
    i = 1
    j = n
    while k != x:
        i += 1
        j -= 1
        k += 1
else:
    i = n
    j = 1
    while k != x:
        i -= 1
        j += 1
        k += 1

print(str(i)+'/' + str(j))
