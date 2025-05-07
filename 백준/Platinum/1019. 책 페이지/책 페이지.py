import sys

N = int(sys.stdin.readline())
value = N
num = [0] * 10
tmp = 1
back = 0
idx = 1

while N != 0:
    x = N % 10
    front = N // 10
    back = value % idx
    # print("x: ", x)
    # print("front: ", front)
    # print("idx: ", idx)
    # print("back: ", back)

    for i in range(10):
        if i == 0:
            if x == 0:
                # num[i] += front
                num[i] += (front - 1) * tmp + back + 1
            else:
                num[i] += front * tmp
            # if front != 0:
            #     num[i] += (front - 1) * tmp + back + 1
        elif i == x:
            num[i] += (front * tmp + back + 1)
        elif i < x:
            num[i] += (front + 1) * tmp
        else:
            num[i] += front * tmp

    N = front
    tmp *= 10
    idx *= 10

    # print("-----------------")
    # print(*num)

print(*num)
