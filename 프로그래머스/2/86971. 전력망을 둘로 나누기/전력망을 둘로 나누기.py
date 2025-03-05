from collections import deque

def solution(n, wires):
    answer = 201
    
    leaf = deque()
    zero = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    visit = [False] * (n+1)
    cnt = [0] * (n+1)
    
    for w in wires :
        a, b = w[0], w[1]
        zero[a] += 1
        zero[b] += 1
        graph[a].append(b)
        graph[b].append(a)
        
    for i in range(1,n+1) :
        if zero[i] == 1 :
            leaf.append(i)
    
    while leaf :
        current_node = leaf.popleft()
        print("current_node: ", current_node)
        
        tmp = 0
        for nodes in graph[current_node] :
            if not visit[nodes] :
                next_node = nodes
                tmp = 1
                break
                
        if tmp == 0 :
            break
        
        print("next_node: ", next_node)
        next_node_cnt = n - (cnt[current_node]+1)
        print("current_cnt: ", cnt[current_node]+1)
        print("next_cnt: ", next_node_cnt)
        answer = min(answer, abs(next_node_cnt - cnt[current_node] -1))
        zero[next_node] -= 1
        cnt[next_node] += cnt[current_node] + 1
        
        if zero[next_node] == 1 :
            leaf.append(next_node)

        visit[current_node] = True
    
    return answer