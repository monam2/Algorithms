#1920 수 찾기

# N개의 정수가 주어질 때, X라는 수가 이 안에 존재하는가 여부찾기

# 입력
# N과 N개의 숫자 / M과 M개의 숫자
# 출력
# M개의 각 수가 N 안에 있는가? 있으면 1, 없으면 0

# 브루투포스로 풀면 n^2이 된다. 그러면 10만 * 10만이므로 안됨
# -> 이분 탐색으로 접근

from bisect import *

N = int(input())
arrN = list(map(int, input().split()))
M = int(input())
arrM = list(map(int, input().split()))

arrN = sorted(arrN)
ans = []

for num in arrM:
  # num이 들어갈 자리
  # arrN의 길이보다 크다? -> 배열엔 없어서 맨 뒤에 새로 추가되는것 : 배열 내에 없는 것

  # 그래서 idx의 조건은 배열 요소 길이보다 작고,
  # 배열 내에 같은 수가 있을 것.
  idx = bisect_left(arrN, num)
  if idx < len(arrN) and arrN[idx] == num:
    ans.append(1)
    continue

  ans.append(0)

print(*ans, sep=" ")