#2960 에라토스테네스의 체
from collections import deque

n,k = map(int, input().split())
p = 0
arr = [i for i in range(2,n+1)]
result = []
while arr:
    p = arr[0]
    for i in arr:
        if i%p == 0:
            result.append(i)
            arr.remove(i)
print(result[k-1])
