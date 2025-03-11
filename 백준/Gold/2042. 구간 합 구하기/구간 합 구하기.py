import sys


def make_segment(left, right, node):
    if left == right:
        st[node] = lst[left]
        return st[node]

    mid = (left + right) // 2

    left_sum = make_segment(left, mid, node * 2)
    right_sum = make_segment(mid+1, right, node * 2 + 1)

    st[node] = left_sum + right_sum
    return st[node]


def find_sum(left, right, node, find_l, find_r):
    mid = (left + right)//2
    tmp = 0

    if find_l <= left and right <= find_r:
        return st[node]

    if find_l <= mid:
        tmp += find_sum(left, mid, node*2, find_l, find_r)
    if mid+1 <= find_r:
        tmp += find_sum(mid+1, right, node*2+1, find_l, find_r)

    return tmp


def update(left, right, node, update_leaf, new_value):
    if left == right:
        st[node] = new_value
        return st[node]

    mid = (left + right) // 2

    if update_leaf <= mid:  # 왼쪽에 있는 경우
        st[node*2] = update(left, mid, node*2, update_leaf, new_value)
    else:  # 오른쪽에 있는 경우
        st[node*2 + 1] = update(mid+1, right, node*2+1, update_leaf, new_value)

    st[node] = st[node*2] + st[node*2+1]
    return st[node]


n, m, k = map(int, sys.stdin.readline().split())
lst = [0] * (n+1)
for i in range(1, n+1):
    x = int(sys.stdin.readline())
    lst[i] = x
st = [0] * (4*n + 2)

make_segment(1, n, 1)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 1:
        update(1, n, 1, b, c)
    else:
        print(find_sum(1, n, 1, b, c))
