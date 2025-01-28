import sys
sys.setrecursionlimit(10**6)

def make_segment(current_node, left, right) :
    if left == right :
        segment[current_node] = (lst[left],lst[left])
        return
    mid = (left + right) // 2
    make_segment(current_node*2, left, mid)
    make_segment(current_node*2 + 1, mid+1, right)
    tmp_min = min(segment[current_node*2][0],segment[current_node*2+1][0])
    tmp_max = max(segment[current_node*2][1],segment[current_node*2+1][1])
    segment[current_node] = (tmp_min,tmp_max)
    return

def find_min_max(start, end, idx) :
    if end < a or b < start :
        return (float('inf'),0)
    
    if a <= start and end <= b :
        return segment[idx]

    mid = (start + end) // 2
    left = find_min_max(start,mid,idx*2)
    right = find_min_max(mid+1,end,idx*2+1)

    return (min(left[0],right[0]),max(left[1],right[1]))

n, m = map(int,sys.stdin.readline().split())
lst = []
for _ in range(n) :
    x = int(sys.stdin.readline())
    lst.append(x)
segment = [0] * (4*n + 1)
make_segment(1,0,n-1)

for _ in range(m) :
    a, b = map(int,sys.stdin.readline().split())
    a -= 1
    b -= 1
    print(*find_min_max(0,n-1,1))
