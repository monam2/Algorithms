#swea 1210 Ladder1
from collections import deque
for t in range(10):
    T = int(input())
    graph = []
    for i in range(100):
        arr=list(map(int, input().split()))
        if i == 99:
            n = arr.index(2)
        graph.append(arr)

    answer = 0
    q = deque()
    visited = [[False]*100 for _ in range(100)]
    q.append((99,n))
    visited[99][n] = True
    while q:
        x,y = q.popleft()
        if x == 0:
            answer = y
            break
        dy = [-1,1]
        for i in range(2): #현재칸에서 왼쪽/오른쪽 칸으로 이동 가능한 경우
            nx = x
            ny = y+dy[i]
            if 0<=nx<100 and 0<=ny<100 and visited[nx][ny] == False:
                if graph[nx][ny]==1:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    break
        else: #현재칸에서 이동 가능한 칸이 윗칸 밖에 없는 경우
            nx = x - 1
            ny = y
            if visited[nx][ny] == False and 0<=nx<100 and 0<=ny<100:
                if graph[nx][ny]==1:
                    q.append((nx,ny))
                    visited[nx][ny] = True

    print(f"#{t+1}", answer)