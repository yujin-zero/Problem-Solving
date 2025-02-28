from collections import deque

def canGo(word1, word2) :
    tmp = 0
    for i in range(len(word1)) :
        if word1[i] != word2[i] :
            tmp += 1
            if tmp > 1 :
                return False
    return True
        
def solution(begin, target, words):
    answer = 0
    word_cnt = len(words)
    visit = [False] * word_cnt
    queue = deque()
    queue.append((begin,0))
    
    while queue :
        current_word, step = queue.popleft()
        if current_word == target :
            answer = step
            break
            
        for i in range(word_cnt) :
            if not visit[i] and canGo(current_word, words[i]) :
                queue.append((words[i],step+1))
                visit[i] = True
    
    return answer