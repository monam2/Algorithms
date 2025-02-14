# 5691 평균 중앙값 문제

import sys

input = sys.stdin.read
data = input().splitlines()

for line in data:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    print(2 * a - b)
