#프로그래머스 84512 모음사전
from itertools import product
def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    result = tuple(list(word))
    count = 1
    lst = []
    for j in range(1,6):
        for i in product(arr, repeat=j):
            lst.append(i)
            
    lst.sort()
    for i in lst:
        if result==i:
            answer = count
            break
        count += 1
    return answer

print(solution("AAAAE"))