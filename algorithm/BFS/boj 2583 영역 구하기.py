#2583 영역 구하기
from collections import deque

def bfs(x,y,maps,visited):
    q = deque()
    q.append((x,y))
    visited[x][y]=True
    count = 1
    while q:
        x,y = q.popleft()
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(maps) and 0<= ny < len(maps[0]):
                if maps[nx][ny]==0 and visited[nx][ny]==False:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    count += 1
    return count

m,n,k=map(int, input().split())
maps=[[0]*m for _ in range(n)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            maps[i][j] = 1

visited = [[False]*m for _ in range(n)]
result = []
for i in range(n):
    for j in range(m):
        if maps[i][j]==0 and visited[i][j]==False:
            result.append(bfs(i,j,maps,visited))

result.sort()
print(len(result))
print(' '.join(map(str, result)))
