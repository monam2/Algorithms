#7562 나이트의 이동
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [[0]*n for _ in range(n)]
    x,y = map(int, input().split())
    a,b = map(int, input().split())
    q = deque()

    dx = [-1,-2,-2,-1,1,2,2,1]
    dy = [-2,-1,1,2,2,1,-1,-2]

    q.append((x,y))
    visited[x][y]=1

    while q:
        x,y = q.popleft()
        if x==a and y==b:
            result = visited[x][y]
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny>= 0 and nx < n and ny < n and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y]+1
    print(result-1)
