#백준 16953 A->B
from collections import deque

a, b = map(int, input().split())
q = deque()
level = 0
q.append((a,level))
while q and a!=b:
    a, level = q.popleft()

    if a*2 <= b:
        q.append((a*2, level+1))
    if a*10+1 <= b:
        q.append((a*10+1, level+1))

if a==b:
    print(level+1)
else:
    print(-1)
