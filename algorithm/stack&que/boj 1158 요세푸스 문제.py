#1158 요세푸스 문제
from collections import deque

n,k = map(int, input().split())
arr = [i for i in range(1,n+1)]
arr = deque(arr)
result = []

while arr:
    for i in range(k-1):
        p=arr.popleft()
        arr.append(p)
    result.append(arr.popleft())

print(f"<{', '.join(map(str, result))}>")
