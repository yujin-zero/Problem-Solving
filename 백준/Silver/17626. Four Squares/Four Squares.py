
n = int(input())
squares = set([i*i for i in range(1, n+1)])

if n in squares:
    print(1)
    exit()

for i in range(1, int(n**0.5) + 1):
    if (n-i**2) in squares:
        print(2)
        exit()

for i in range(1, int(n**0.5) + 1):
    for j in range(1, int(int(n - i**2)**0.5) + 1):
        if (n - i*i - j*j) in squares:
            print(3)
            exit()

print(4)
