#백준 1926 그림

from collections import deque
def bfs(x,y,visited):
    global fill
    max_val = 0
    q = deque()
    visited[x][y] = True
    q.append((x,y))

    while q:
        x,y = q.popleft()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        max_val += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                if graph[nx][ny] == '1':
                    q.append((nx,ny))
                    visited[nx][ny] = True

    fill = max(fill, max_val)
    return True

n,m = map(int, input().split())
graph = [list(map(str, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
paint = 0
fill = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]=='1' and visited[i][j]==False and bfs(i,j,visited):
            paint += 1

print(paint)
print(fill)