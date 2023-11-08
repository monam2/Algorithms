#백준 4179 불!
# #: 벽 / .: 지나갈 수 있는 공간 / J: 지훈이의 미로에서의 초기위치 (지나갈 수 있는 공간)
# F: 불이 난 공간
# 불이 여러개일 수도 있을듯
from collections import deque
import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = []
q = deque()
for i in range(n):
    arr = list(input().rstrip())
    graph.append(arr)
    for j in range(m):
        if arr[j] == 'J':
            q.append((i,j,0))
            graph[i][j] = '.' #지훈이가 있는 위치도 . 으로 바꿈

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'F':
            q.append((i,j,-1))

answer = "IMPOSSIBLE"
dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    x,y,dist = q.popleft()
    if dist > -1 and (x==0 or y==0 or x==n-1 or y==m-1) and graph[x][y] != '#' and graph[x][y] != 'F':
        answer = dist + 1
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] != '#':
            if dist == -1 and graph[nx][ny] != 'F': #불 확산
                graph[nx][ny] = 'F'
                q.append((nx,ny,-1))
            elif dist >-1 and graph[nx][ny] == '.': #지훈이 이동
                graph[nx][ny] = 'j'
                q.append((nx,ny,dist+1))

print(answer)

# while q and flag:
#     x,y,dist = q.popleft()
#     dx = [-1,0,1,0]
#     dy = [0,1,0,-1]
#     if dist==-1: #불이면 확산
#         for i in range(4):
#             px = x + dx[i]
#             py = y + dy[i]
#             if 0<=px<n and 0<=py<m and (graph[px][py] == '.' or graph[px][py] == 'j'):
#                 graph[px][py] == 'f'
#                 q.append((px,py,-1))
#     else: #지훈이면 이동
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (nx==0 or nx == n-1 or ny == 0 or ny == m-1) and graph[nx][ny]=='.':
#                 answer = dist+2 #끝 행/열이 빈칸이면 종료
#                 flag = False
#                 break
#             if 0<=nx<n and 0<=ny<m and graph[nx][ny] == '.': #이동
#                 graph[nx][ny] = 'j'
#                 q.append((nx,ny,dist+1))

# print(answer)