#2346 풍선 터뜨리기
from collections import deque

n = int(input())
arr = list(map(int, input().split()))
q= deque()
for idx,v in enumerate(arr):
    q.append((v,idx+1))
result = []
while q:
    v,idx = q.popleft()
    if v > 0 and q:
        for i in range(v-1):
            k = q.popleft()
            q.append(k)
    elif v < 0 and q:
        for i in range(abs(v)):
            k = q.pop()
            q.appendleft(k)
    result.append(idx)

for i in result:
    print(i, end=' ')

# n = int(input())
# arr = list(map(int, input().split()))
# q= deque()
# for idx,v in enumerate(arr):
#     q.append((v,idx+1))
# result = []
# while q:
#     v,idx = q.popleft()
#     if v > 0 and q:
#         q.rotate(-(v-1))
#     elif v < 0 and q:
#         q.rotate(-v)
#     result.append(idx)

# for i in result:
#     print(i, end=' ')
