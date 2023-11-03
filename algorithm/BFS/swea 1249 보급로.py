#swea 1249 보급로
from collections import deque

def bfs(x,y,graph,visited):
    q = deque()
    q.append((x,y))
    min_dist = 10000 #입력의 최댓값이 100^2
    while q:
        x,y= q.popleft()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n: #이미 방문했던 곳이 지금까지 온거 + 다음 칸보다 크면
                if visited[nx][ny] > visited[x][y] + graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + graph[nx][ny]
                    q.append((nx,ny))
    return min_dist


T = int(input())
for t in range(1,T+1):
    n = int(input())
    graph = []
    for i in range(n):
        arr = list(input())
        arr = list(map(int, arr))
        graph.append(arr)

    visited = [[10000]*n for _ in range(n)]
    visited[0][0] = 0
    bfs(0,0,graph,visited)
    answer = visited[n-1][n-1]
    print(f"#{t}", answer)