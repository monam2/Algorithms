#백준 3184 양
from collections import deque

def bfs(x,y,maps,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    wolf = 0 
    sheep = 0
    if maps[x][y] == 'v':
        wolf += 1
    elif maps[x][y] == 'o':
        sheep += 1
    while q:
        x,y = q.popleft()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny] != '#' and visited[nx][ny]==False:
                    if maps[nx][ny] == 'v':
                        wolf += 1
                    elif maps[nx][ny] == 'o':
                        sheep += 1
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return [sheep, wolf]


n, m = map(int, input().split())
maps = []
for _ in range(n):
    a = input()
    maps.append(list(a))

visited = [[False]*m for _ in range(n)]
result = [0, 0]

for i in range(n):
    for j in range(m):
        if maps[i][j] != '#' and visited[i][j] == False:
            [sheep, wolf] = bfs(i,j,maps,visited)
            if sheep > wolf:
                result[0] += sheep
            else:
                result[1] += wolf

print(result[0], result[1])
