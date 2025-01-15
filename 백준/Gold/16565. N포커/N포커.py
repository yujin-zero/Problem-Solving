import sys
from math import comb

N = int(sys.stdin.readline())

if N < 4 :
    print(0)
    exit()

part = [0 for _ in range(14)]
part[1] = 13 * comb(48,N-4)

for i in range(2,14) :
    if N < 4*i :
        break

    part[i] = comb(13,i) * comb(52-i*4,N-i*4)

end = N //4 

answer = 0 
for i in range(1,end+1) :
    if i%2 == 0 :
        answer -= part[i]
    else :
        answer += part[i]

print(answer%10007)