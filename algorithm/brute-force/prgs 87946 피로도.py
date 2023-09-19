#프로그래머스 피로도
from itertools import permutations

def solution(k, dungeons):
    result = []
    for arr in permutations(dungeons, len(dungeons)):
        piro = k
        count = 0
        for i in arr:
            if i[0] <= piro:
                piro -= i[1]
                count += 1
        result.append(count)
    return max(result)

print(solution(80, [[80, 20], [50, 40], [30, 10]]))
