import sys

mod = 1000000007


def make_segment(left, right, current):
    if left == right:
        lst[current] = (num[left]) % mod
        return lst[current]

    mid = (left + right) // 2

    left_value = make_segment(left, mid, current*2)
    right_value = make_segment(mid+1, right, current*2+1)

    lst[current] = (left_value * right_value) % mod
    return lst[current]


def find_multi(left, right, current, start, end):
    if right < start or left > end:
        return 1
    if start <= left and right <= end:
        return lst[current]

    mid = (left + right) // 2

    left_value = find_multi(left, mid, current*2, start, end)
    right_value = find_multi(mid+1, right, 2*current+1, start, end)

    return (left_value * right_value) % mod


def update_segment(left, right, current, update_idx, new_value):
    if update_idx > right or update_idx < left:
        return lst[current]

    if left == right:
        lst[current] = new_value % mod
        return lst[current]

    mid = (left + right) // 2

    left_value = update_segment(left, mid, current*2, update_idx, new_value)
    right_value = update_segment(
        mid+1, right, current*2+1, update_idx, new_value)

    lst[current] = (left_value * right_value) % mod
    return lst[current]


N, M, K = map(int, sys.stdin.readline().split())
num = [0] * (N+1)
lst = [0] * (4*N + 1)
for i in range(1, N+1):
    x = int(sys.stdin.readline())
    num[i] = x

make_segment(1, N, 1)

for _ in range(M+K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update_segment(1, N, 1, b, c)
    else:
        print(find_multi(1, N, 1, b, c))
