# 17086 아기 상어 2

from collections import deque

DX = [-1,-1,0,1,1,1,0,-1]
DY = [0,1,1,1,0,-1,-1,-1]

def bfs(i,j,graph):
    q = deque()
    q.append((i,j,0))
    visited = [[False] * m for _ in range(n)]

    visited[i][j] = True

    while q:
        x, y, dist = q.popleft()
        
        if graph[x][y] == 1:
            return dist

        for d in range(8):
            nx = x + DX[d]
            ny = y + DY[d]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                q.append((nx,ny,dist+1))
                visited[nx][ny] = True



n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


res = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt = bfs(i,j,graph)
            res.append(cnt)

print(max(res))