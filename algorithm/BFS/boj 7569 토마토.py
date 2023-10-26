#백준 7569 토마토
from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
maps = []

one = []
for l in range(h):
    graph = []
    for i in range(n):
        a = list(map(int, input().split()))
        for k in range(m):
            if a[k] == 1:
                one.append((l,i,k))
        graph.append(a)
    maps.append(graph)
q = deque()
visited = [[[False]*m for _ in range(n)] for _ in range(h)]
for z,x,y in one:
    visited[z][x][y] = True
    q.append((z,x,y,1))
maxCnt = 0
while q:
    z,x,y,cnt = q.popleft()
    dz = [-1, 1, 0, 0, 0, 0] #위 아래 왼쪽 오른쪽 앞 뒤
    dx = [0, 0, -1, 0, 1, 0]
    dy = [0, 0, 0, 1, 0, -1]
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx<n and 0<= ny < m and 0<= nz < h:
            if visited[nz][nx][ny] == False and maps[nz][nx][ny]!=-1:
                visited[nz][nx][ny] = True
                maps[nz][nx][ny] = cnt
                maxCnt = cnt
                q.append((nz,nx,ny,cnt+1))

for l in range(h):
    for i in range(n):
        for j in range(m):
            if maps[l][i][j] == 0:
                maxCnt = -1
print(maxCnt)
