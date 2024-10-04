# 좌표 압축 18870

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

newArr = sorted(list(set(arr)))

myDict = {}
for i in range(len(newArr)):
  myDict[newArr[i]] = i

# 출력
ans = []
for num in arr:
  ans.append(myDict[num])

print(*ans, sep=' ')