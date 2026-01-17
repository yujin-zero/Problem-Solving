import sys

def input_seg(start, end, node, input_value, input_cnt) :
    if start == end :
        seg_tree[node] += input_cnt
        return seg_tree[node]

    mid = (start + end) // 2
    if input_value <= mid :
        left_seg = input_seg(start, mid, node*2, input_value, input_cnt)
        right_seg = seg_tree[node*2 + 1]
    else :
        left_seg = seg_tree[node*2]
        right_seg = input_seg(mid+1, end, node*2 + 1, input_value, input_cnt)
    
    seg_tree[node] = left_seg + right_seg
    return seg_tree[node]

def find_seg(start, end, node, find_idx) :
    if start == end :
        return start

    mid = (start + end) // 2
    left_cnt = seg_tree[node*2]
    if find_idx <= left_cnt :
        return find_seg(start, mid, node*2, find_idx)
    else :
        return find_seg(mid+1, end, node*2 + 1, find_idx - left_cnt)

n = int(sys.stdin.readline())
seg_tree = [0] * (4 * 1000000 + 1)

for _ in range(n) :
    input_lst = list(map(int, sys.stdin.readline().split()))

    a = input_lst[0]
    if a == 2 :
        b, c = input_lst[1], input_lst[2]
        input_seg(1, 1000000, 1, b, c)
    else :
        b = input_lst[1]
        value = find_seg(1, 1000000, 1, b)
        print(value)
        input_seg(1, 1000000, 1, value, -1)
