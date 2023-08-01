import sys

d, h, w = map(int, sys.stdin.readline().split())

a = (d**2/(h**2 + w**2))**(1/2)
print(int(h*a), int(w*a))
