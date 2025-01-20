# 2309 일곱 난쟁이
from itertools import combinations

heights = [int(input()) for _ in range(9)]

ans = []

for comb in combinations(heights, 7):
    if sum(comb) == 100:
        ans = sorted(list(comb))
        break

for num in ans:
    print(num)
