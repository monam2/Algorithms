from collections import deque

T = int(input())
for t in range(1,1+T):
    n = int(input())
    graph = []
    for i in range(n):
        arr = list(input())
        graph.append(list(map(int, arr)))

    result = 0
    visited = [[10000]*n for _ in range(n)]
    visited[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        x,y = q.popleft()
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] > visited[x][y] + graph[nx][ny]:
                    visited[nx][ny] = visited[x][y] + graph[nx][ny]
                    q.append((nx, ny))
    print(f"#{t} {visited[n-1][n-1]}")
