#백준 2589 보물섬
#sys + pypy3로 제출시 통과
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y):
    global dist
    q = deque()
    q.append((x,y,0))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    while q:
        x,y,d = q.popleft()
        dist = max(dist, d)
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny]==False and graph[nx][ny] == 'L':
                    q.append((nx,ny,d+1))
                    visited[nx][ny] = True

n,m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
dist = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            bfs(i,j)
print(dist)
