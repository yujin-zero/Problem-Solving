import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
mod = 1000000003
answer = 0

prepick_yes = {1:1}
prepick_no = {0:0}

for _ in range(N-1) :
    current_yes = dict()
    current_no = dict()

    for i in prepick_no :
        if i+1 <= K :
            current_yes[i+1] = prepick_no[i]

    for i in prepick_yes :
        current_no[i] = prepick_yes[i]
    for i in prepick_no :
        if i in current_no :
            current_no[i] = (current_no[i] + prepick_no[i]) % mod
        else :
            current_no[i] = prepick_no[i]
    
    prepick_yes = current_yes
    prepick_no = current_no

if K in prepick_no :
    answer += prepick_no[K]

prepick_yes = {0:0}
prepick_no = {0:1}

for _ in range(N-1) :
    current_yes = dict()
    current_no = dict()

    for i in prepick_no :
        if i+1 <= K :
            current_yes[i+1] = prepick_no[i]

    for i in prepick_yes :
        current_no[i] = prepick_yes[i]
    for i in prepick_no :
        if i in current_no :
            current_no[i] = (current_no[i] + prepick_no[i]) % mod
        else :
            current_no[i] = prepick_no[i]
    
    prepick_yes = current_yes
    prepick_no = current_no

if K in prepick_no :
    answer += prepick_no[K]
if K in prepick_yes : 
    answer += prepick_yes[K]

print(answer%mod)