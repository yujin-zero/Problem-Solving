import sys

E, S, M = map(int,sys.stdin.readline().split())

i,j,k = 1,1,1
year = 1
while True :
    if i == E and j == S and k == M :
        break

    i += 1
    j += 1
    k += 1

    if i > 15 :
        i = 1
    if j > 28 :
        j = 1
    if k > 19 :
        k = 1

    year += 1

print(year)