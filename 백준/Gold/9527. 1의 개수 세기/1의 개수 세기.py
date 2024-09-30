import sys

## 1에서 n까지의 1의 갯수 구하는 함수
def hap_1_n(n) : 
    cnt = 0

    x = 1
    nextX = 2
    while True :
        if x > b :
            break

        cnt += (n // nextX) * x
        if (n % nextX) >= x :
            cnt += (n % nextX - x + 1) 

        x = nextX
        nextX *= 2

    return cnt


a, b = map(int,sys.stdin.readline().split())
hap_1_b = hap_1_n(b)
hap_1_a_1 = hap_1_n(a-1)
answer = hap_1_b - hap_1_a_1

print(answer)