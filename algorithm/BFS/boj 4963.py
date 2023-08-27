#4963 섬의 개수
from collections import deque
import sys

input = sys.stdin.readline

def BFS(maps,visited, x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        dx = [-1,-1,0,1,1,1,0,-1]
        dy = [0,1,1,1,0,-1,-1,-1]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < len(maps) and 0 <= ny < len(maps[0]):
                if visited[nx][ny] == False and maps[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = True

while True:
    n,m = map(int, input().split())
    
    if n==0 and m==0:
        break
    if n==1 and m==1:
        k = int(input())
        print(k)
        continue

    maps = []
    for i in range(m):
        maps.append(list(map(int, input().split())))
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    count = 0
    for i in range(m):
        for j in range(n):
            if maps[i][j]==1 and visited[i][j]==False:
                BFS(maps,visited, i,j)
                count += 1
    print(count)
