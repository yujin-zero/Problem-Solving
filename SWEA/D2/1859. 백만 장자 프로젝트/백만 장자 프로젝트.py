t = int(input())
result = []

for _ in range(t) :
    n = int(input())
    price = list(map(int,input().split()))
    i = 0
    cnt = 0
    money = 0
    max_index = 0
    for j in range(i, n):
        if price[max_index] < price[j] :
            max_index = j
    # print(max_index)
    while True :
        if i == n :
            break

        if i < max_index :
            cnt += 1
            money -= price[i]
        elif i == max_index :
            money += (price[i]*cnt)
            cnt = 0
            max_index = i+1
            for j in range(i+1,n) :
                if price[max_index] < price[j] :
                    max_index = j
            # print(max_index)

        i += 1

    result.append(money)

for i in range(t) :
    print('#%d %d'%(i+1,result[i]))