#프로그래머스 43163 단어 변환
def solution(begin, target, words):
    from collections import deque
    if target not in words:
        return 0
    q = deque()
    words = list(map(lambda v : [v, 0, False], words))
    q.append([begin, 0, True])
    answer = 51
    
    while q:
        w, cnt,bln = q.popleft()
        if w == target:
            answer=min(cnt,answer)
            continue
        
        for i in range(len(words)):
            if words[i][2] == False:
                count=0
                for j in range(len(w)):
                    if words[i][0][j]!=w[j]:
                        count+=1
                if count == 1:
                    words[i][1] = cnt+1
                    words[i][2] = True
                    q.append(words[i])
    return answer

print(solution("hit","cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
