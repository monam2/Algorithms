# 백준 2573 빙산

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y, visited, carve):  # 빙산이 분리되었는지 판단
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and graph[nx][ny] != 0:
                q.append((nx, ny))
                visited[nx][ny] = True
            elif graph[nx][ny] == 0: #빙산을 깎을 횟수
                carve[x][y] += 1
    return True

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

year = 0
count = 0

while True:
    visited = [[False]*m for _ in range(n)]
    carve = [[0]*m for _ in range(n)]
    count = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j] != 0 and visited[i][j] == False:  # 빙산이 분리됐는지 판단
                if bfs(i, j, visited, carve):
                    count += 1
    if count > 1:
        answer = year
        break

    num = 0
    for i in range(n): #빙산 깎기
        for j in range(m):
            if graph[i][j] != 0:
                graph[i][j] -= carve[i][j]
                if graph[i][j] <0:
                    graph[i][j] = 0
            else:
                num += 1
    if num == n*m:
        answer = 0
        break
    year += 1

print(answer)


#빙산을 아래처럼 깎으면 무조건 시간초과남
# sea = []
#     num = 0
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j] == 0:
#                 num += 1
#                 di = [-1, 0, 1, 0]
#                 dj = [0, 1, 0, -1]
#                 for k in range(4):
#                     ni = i + di[k]
#                     nj = j + dj[k]
#                     if 0<=ni<n and 0<=nj<m:
#                         sea.append((ni, nj))
#     if num == n*m:
#         answer = 0
#         break
#     for a, b in sea:
#         graph[a][b] -= 1
#         if graph[a][b] < 0:
#             graph[a][b] = 0