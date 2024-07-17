import sys

n = int(sys.stdin.readline())
solution = list(map(int,sys.stdin.readline().split()))
solution.sort()
hap = float('inf')

for i in range(n-2) :
    start, end = i+1, n-1

    while start < end :
        tmp = solution[i] + solution[start] + solution[end]
        if abs(tmp) < hap :
            hap = abs(tmp)
            result = [i,start,end]
        
        if tmp < 0 :
            start += 1
        else :
            end -= 1

print(solution[result[0]], solution[result[1]], solution[result[2]])