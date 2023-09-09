#프로그래머스 귤 고르기
from collections import Counter

def solution(k, tangerine):
    d = Counter(tangerine)
    value = list(d.values())
    value.sort(reverse=True)
    for i in range(len(tangerine)-k):
        value[-1] -= 1
        if value[-1] == 0:
            value.pop()
    return len(value)

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))

# 시간초과 풀이
# from collections import Counter

# def solution(k, tangerine):
#     d = Counter(tangerine)
#     how_del = len(tangerine)-k

#     while how_del > 0:
#         minV = min(d.values())
#         for key,v in d.items():
#             if v == minV:
#                 v -= 1
#                 if v == 0:
#                     d.pop(key)
#                 else:
#                     d[key] = v
#                 how_del -= 1
#                 break
#     return len(d)
    
# print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))
# print(solution(4,[1, 3, 2, 5, 4, 5, 2, 3]))
# print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))
