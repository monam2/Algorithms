from collections import deque

def solution(home):
    answer = 0
    if home%5==0:
        answer = home//5
    else:
        if home%5>=3:
            answer += (home//5)+1
            answer += 5 - home%5
        else:
            answer += home//5
            answer += home%5

    return answer
            
print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))
