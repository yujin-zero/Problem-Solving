import sys

def make_seg(start, end, node) :
    if start == end :
        seg_tree[node] = lst[start]
        return seg_tree[node]

    mid = (start + end) // 2
    left_seg = make_seg(start, mid, node*2)
    right_seg = make_seg(mid+1, end, node*2 +1)
    seg_tree[node] = min(left_seg, right_seg)
    return seg_tree[node]

def update_seg(start, end, node, update_idx, update_value) :
    if start == end :
        seg_tree[node] = update_value
        return seg_tree[node]
    
    mid = (start + end) // 2
    if update_idx <= mid :
        left_min = update_seg(start, mid, node*2, update_idx, update_value)
        right_min = seg_tree[node*2 + 1]
    else :
        left_min = seg_tree[node*2]
        right_min = update_seg(mid+1, end, node*2 +1, update_idx, update_value)

    seg_tree[node] = min(left_min, right_min)
    return seg_tree[node]

def find_seg(start, end, node) :
    if range_a <= start <= range_b and range_a <= end <= range_b :
        return seg_tree[node]
    
    left_num = float('inf')
    right_num = float('inf')

    mid = (start + end) // 2
    if range_a <= mid :
        left_num = find_seg(start, mid, node*2)
    if range_b >= mid+1 :
        right_num = find_seg(mid+1, end, node*2 + 1)

    return min(left_num, right_num)

N = int(sys.stdin.readline())
lst = [0] + list(map(int, sys.stdin.readline().split()))
seg_tree = [0] * (4*N + 1)
make_seg(1, N, 1)

M = int(sys.stdin.readline())
for _ in range(M) :
    a, b, c = map(int, sys.stdin.readline().split())
    
    if a == 1 :
        update_seg(1, N, 1, b, c)
    else :
        range_a = b
        range_b = c
        print(find_seg(1, N, 1))
