import sys


def quack(sound):
    index = []
    look = 'q'
    i = 0
    while (i < len(sound)):
        if sound[i] == 'q' and look == 'q':
            index.append(i)
            look = 'u'
        elif sound[i] == 'u' and look == 'u':
            index.append(i)
            look = 'a'
        elif sound[i] == 'a' and look == 'a':
            index.append(i)
            look = 'c'
        elif sound[i] == 'c' and look == 'c':
            index.append(i)
            look = 'k'
        elif sound[i] == 'k' and look == 'k':
            index.append(i)
            look = 'q'
        i += 1

    if len(index) % 5 != 0:
        print(-1)
        sys.exit()

    for j in range(len(index)-1, -1, -1):
        sound.pop(index[j])


x = sys.stdin.readline()
sound = []
for i in range(len(x)-1):
    sound.append(x[i])

duck = 0
while sound != []:
    if sound[0] != 'q':
        print(-1)
        sys.exit()
    quack(sound)
    duck += 1

print(duck)
