import sys

def binarySearch(value) :
    left = 0
    right = len(lis) - 1

    while left <= right :
        mid = (left + right) // 2

        if lis[mid] == value :
            return mid
        elif lis[mid] > value :
            right = mid - 1
        else :
            left = mid + 1

    return left

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
lis = [0]

for value in a :
    if value > lis[-1] :
        lis.append(value)
    else :
        idx = binarySearch(value)
        lis[idx] = value

print(len(lis)-1)
