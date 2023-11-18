#swea 1227 미로2
from collections import deque

for t in range(1,11):
    T = int(input())
    graph = []
    for i in range(100):
        arr = list(input())
        if '2' in arr:
            start = (i, arr.index('2'))
        graph.append(arr)

    q = deque()
    visited = [[False]*100 for _ in range(100)]
    q.append(start)
    visited[start[0]][start[1]] = True
    answer = 0

    while q:
        x, y = q.popleft()
        if graph[x][y] == '3':
            answer = 1
            break
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < 100 and 0<= ny < 100:
                if visited[nx][ny] == False and graph[nx][ny] != '1':
                    q.append((nx,ny))
                    visited[nx][ny] = True
    print(f"#{t} {answer}")