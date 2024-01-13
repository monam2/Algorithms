#백준 2636 치즈
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    q = deque()
    q.append((0,0))
    rm = []

    while q:
        x,y = q.popleft()

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    rm.append((nx,ny))
    for x,y in rm:
        graph[x][y] = 0
    return len(rm)


n, m = map(int, input().split())
graph = []
count = 0
for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)
    count += sum(graph[i])

time = 1
while True:
    melt = bfs()
    count -= melt
    if count == 0:
        break
    time += 1


print(time)
print(melt)
