import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    up = list(map(int, sys.stdin.readline().split()))
    down = list(map(int, sys.stdin.readline().split()))

    no_select = 0
    up_select = 0
    down_select = 0
    for i in range(n):
        temp_no = max(up_select, down_select)
        temp_up = max(no_select, down_select)
        temp_down = max(no_select, up_select)

        no_select = temp_no
        up_select = temp_up + up[i]
        down_select = temp_down + down[i]

    print(max(no_select, up_select, down_select))
