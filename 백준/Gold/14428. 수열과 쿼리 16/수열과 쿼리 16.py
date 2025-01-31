import sys

def make_segment(current_node, left, right) :
    if left == right :
        segment_tree[current_node] = (A[left],left)
        return segment_tree[current_node]
    mid = (left+right)//2
    tmp1 = make_segment(current_node*2, left, mid)
    tmp2 = make_segment(current_node*2 +1,mid+1,right)
    if tmp1[0] <= tmp2[0] :
        segment_tree[current_node] = tmp1
    else :
        segment_tree[current_node] = tmp2
    return segment_tree[current_node]

def find_min(current_node, left, right) :
    if right < a or left > b :
        return (float('inf'),-1)
    elif a <= left and right <= b :
        return segment_tree[current_node]
    
    mid = (left+right)//2
    tmp1 = find_min(current_node*2,left,mid)
    tmp2 = find_min(current_node*2+1,mid+1,right)
    if tmp1[0] <= tmp2[0] :
        return tmp1
    else :
        return tmp2

def update_segment(current_node, left, right) :
    if left == right :
        segment_tree[current_node] = (b,a)
        return
    
    mid = (left+right)//2
    if left <= a <= mid :
        update_segment(current_node*2,left,mid)
    else :
        update_segment(current_node*2+1,mid+1,right)

    if segment_tree[current_node*2][0] <= segment_tree[current_node*2+1][0] :
        segment_tree[current_node] = segment_tree[current_node*2]
    else :
        segment_tree[current_node] = segment_tree[current_node*2+1]

N = int(sys.stdin.readline())
A = [0] + list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
segment_tree = [(float('inf'),-1)] * (4*N +1)

make_segment(1,1,N)

for _ in range(M) :
    num, a, b = map(int,sys.stdin.readline().split())
    if num == 2 :
        print(find_min(1,1,N)[1])
    else :
        update_segment(1,1,N)