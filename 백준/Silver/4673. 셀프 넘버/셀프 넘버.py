no = set()

for i in range(1, 10000):
    if i not in no:
        now = i
        next = now
        while now < 10000:
            now = str(now)
            for j in range(len(now)):
                next += int(now[j])
            if next not in no:
                no.add(next)
            now = next
    if i not in no:
        print(i)
