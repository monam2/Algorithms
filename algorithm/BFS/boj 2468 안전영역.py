#2468 안전영역
from collections import deque
def bfs(x,y,maps,k,visited):
    q = deque()
    q.append((x,y))
    visited[x][y]=True
    dx,dy = [-1,0,1,0], [0,1,0,-1]
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if visited[nx][ny]==False and maps[nx][ny]>k:
                    q.append((nx,ny))
                    visited[nx][ny]=True

n = int(input())
maps = []
maxV = 0
for _ in range(n):
    a = list(map(int, input().split()))
    maps.append(a)
    maxV = max(maxV, max(a))

result = []
for k in range(maxV+1):
    count = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False and maps[i][j] > k:
                bfs(i,j,maps,k,visited)
                count += 1
    result.append(count)
print(max(result))
