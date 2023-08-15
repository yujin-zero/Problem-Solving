import sys

n = int(sys.stdin.readline())
student = {}

for _ in range(n):
    name, kor, eng, math = sys.stdin.readline().split()
    student[name] = [int(kor), int(eng), int(math)]

student_sort = sorted(
    student.items(), key=lambda x: (-x[1][0], x[1][1], -x[1][2], x[0]))

for s in student_sort:
    print(s[0])
