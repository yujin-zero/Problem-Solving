import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
s3 = sys.stdin.readline().rstrip()
s = [s1,s2,s3]

for i in range(3) :
    if s[i] != 'Fizz' and s[i] != 'Buzz' and s[i] != 'FizzBuzz' :
        num = int(s[i]) + 3 - i
        break

if num%3 == 0 and num%5 == 0:
    print('FizzBuzz')
elif num%3 == 0:
    print('Fizz')
elif num%5 == 0 :
    print('Buzz')
else :
    print(num)