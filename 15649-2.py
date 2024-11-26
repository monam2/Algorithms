# 15649 N과 M
from itertools import permutations

N, M = map(int, input().split())
comb = list(permutations([i for i in range(1,N+1)], M))
for c in comb:
    print(*c)