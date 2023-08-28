#2667 단지번호붙이기
from collections import deque

def BFS(maps, visited, x, y):
    q = deque()
    visited[x][y]=True
    q.append((x,y))
    count = 1

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(maps) and 0<= ny < len(maps[0]):
                if maps[nx][ny] == 1 and visited[nx][ny] == False:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    count += 1
    return count

n = int(input())
maps = []
for i in range(n):
    maps.append(list(map(int, input())))

result = []
visited = [[False]*len(maps[0]) for _ in range(len(maps))]

for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j]==1 and visited[i][j]==False:
            result.append(BFS(maps, visited, i,j))
print(len(result))
result.sort()
for i in result:
    print(i)

