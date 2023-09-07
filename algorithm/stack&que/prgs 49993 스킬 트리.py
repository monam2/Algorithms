#프로그래머스 스킬트리
from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        right = True
        skilldeq = deque(skill)
        for j in i:
            if skilldeq and j==skilldeq[0]:
                skilldeq.popleft()
            elif skilldeq and j in skilldeq: #j가 스킬덱의 맨앞꺼가 아닌데 스킬덱에 있으면 안됨->종료
                right = False
                break
            
        if right == False:
            continue
        else:
            answer += 1
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
