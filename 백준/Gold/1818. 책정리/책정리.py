import sys

def find_idx(x) :
    left = 0
    right = len(queue)-1

    while left <= right :
        mid = (left + right) // 2

        if queue[mid] == x :
            return mid
        elif x < queue[mid] :
            right = mid - 1
        else :
            left = mid + 1
    
    return left

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

queue = []

for value in lst :
    if not queue :
        queue.append(value)
    
    if queue[-1] < value :
        queue.append(value)
    else :
        tmp = find_idx(value)
        queue[tmp] = value

answer = N - len(queue)
print(answer)