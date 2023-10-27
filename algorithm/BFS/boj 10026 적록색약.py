#백준 10026 적록색약
from collections import deque

def rg_no(x,y,graph,visited): #적록색맹 아닌 사람
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny]==False and graph[x][y]== graph[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return True

def rg_yes(x,y,graph,visited): #적록색맹
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    while q:
        x,y = q.popleft()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==False:
                if graph[x][y]=='B' and graph[nx][ny]=='B':
                    q.append((nx,ny))
                    visited[nx][ny] = True
                elif (graph[x][y]=='R' or graph[x][y]=='G') and (graph[nx][ny]=='R' or graph[nx][ny]=='G'):
                    q.append((nx,ny))
                    visited[nx][ny] = True
    return True

n = int(input())
no_graph = [list(input()) for _ in range(n)]
yes_graph = no_graph
no_visited = [[False]*n for _ in range(n)]
yes_visited = [[False]*n for _ in range(n)]

no = 0
yes = 0

for i in range(n):
    for j in range(n):
        if no_visited[i][j] == False and rg_no(i,j,no_graph,no_visited):
            no += 1
        if yes_visited[i][j] == False and rg_yes(i,j,yes_graph,yes_visited):
            yes += 1

print(no, yes)