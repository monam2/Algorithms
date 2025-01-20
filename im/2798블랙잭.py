# 2798 블랙잭
# N개의 카드 중 뽑은 3장 합이 M이하, 합을 가장 크게

from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 0

for perm in permutations(numbers, 3):
    if ans < sum(perm) <= m:
        ans = sum(perm)

print(ans)
