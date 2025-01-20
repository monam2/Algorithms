# 3040 백설 공주와 일곱 난쟁이
from itertools import combinations

# 일곱 난쟁이의 모자에 쓰여있는 숫자의 합 : 100
# 아홉 난쟁이 모자의 수. 이 중에서 일곱 난쟁이를 찾기
# -> 아홉 개의 수 중에서 합이 100이 되는 7개의 수 찾기

arr = [int(input()) for _ in range(9)]
visited = set()

# 조합 -> 9개 중 7개 뽑기

for comb in combinations(arr, 7):
    if sum(comb)==100:
        for num in comb:
            print(num)
        break
