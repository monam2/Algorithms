#백준 7576 토마토
from collections import deque

m,n = map(int,input().split())

graph = []
tomato = []
for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(m):
        if arr[j] == 1:
            tomato.append((i,j))
    graph.append(arr)

visited = [[False]*m for _ in range(n)]
q = deque()
for x,y in tomato:
    visited[x][y] = True
    q.append((x,y))
maxDay = 0

while q:
    x,y = q.popleft()
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
            if graph[nx][ny] != -1:
                graph[nx][ny] = graph[x][y] + 1
                maxDay = max(maxDay, graph[x][y] + 1)-1
                visited[nx][ny] = True
                q.append((nx,ny))

def last(graph:list):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

print(maxDay) if last(graph) else print(-1)
