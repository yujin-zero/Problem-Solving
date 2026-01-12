import sys

def make_seg(start, end, node) :
    if start == end :
        value = lst[start]
        if value % 2 == 0 :
            seg_tree[node][0] = 1
        else :
            seg_tree[node][1] = 1
        return seg_tree[node] # [1,0]
    
    mid = (start + end) // 2
    left_seg = make_seg(start, mid, node*2) # [1,0]
    right_seg = make_seg(mid + 1, end, node*2 + 1) #[0,1]

    seg_tree[node][0] = left_seg[0] + right_seg[0]
    seg_tree[node][1] = left_seg[1] + right_seg[1]

    return seg_tree[node]

def find_seg(start, end, node, is_even) :
    if a <= start <= b and a <= end <= b :
        if is_even :
            return seg_tree[node][0]
        else :
            return seg_tree[node][1]
    
    mid = (start + end) // 2
    left_seg = 0
    right_seg = 0

    if mid >= a :
        left_seg = find_seg(start, mid, node * 2, is_even)
    if mid+1 <= b :
        right_seg = find_seg(mid+1, end, node*2 +1, is_even)

    return left_seg + right_seg

def update_seg(start, end, node, update_value, update_idx) :
    if start == end :
        if update_value % 2 == 0 :
            seg_tree[node][0] = 1
            seg_tree[node][1] = 0
        else :
            seg_tree[node][0] = 0
            seg_tree[node][1] = 1
        return seg_tree[node]
    
    mid = (start + end) // 2
    if update_idx <= mid :
        left_seg = update_seg(start, mid, node*2, update_value, update_idx)
        right_seg = seg_tree[node*2 + 1]
    else :
        left_seg = seg_tree[node*2]
        right_seg = update_seg(mid+1, end, node*2 +1, update_value, update_idx)
    
    seg_tree[node][0] = left_seg[0] + right_seg[0]
    seg_tree[node][1] = left_seg[1] + right_seg[1]

    return seg_tree[node]


N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
seg_tree = [[0,0] for _ in range(4*N + 1)] # 짝수, 홀수
make_seg(0, N-1, 1)

for _ in range(M) :
    num, l, r = map(int, sys.stdin.readline().split())

    if num == 1 :
        update_seg(0, N-1, 1, r, l-1)
    elif num == 2 :
        a = l - 1
        b = r - 1
        print(find_seg(0, N-1, 1, True))
    else :
        a = l - 1
        b = r - 1
        print(find_seg(0, N-1, 1, False))