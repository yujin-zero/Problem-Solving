import sys

n = int(sys.stdin.readline())
m = sys.stdin.readline()
one = int(m[2])
ten = int(m[1])
hun = int(m[0])
print(n*one)
print(n*ten)
print(n*hun)
ten *= 10
hun *= 100
print((one+ten+hun)*n)
