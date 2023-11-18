#swea 1954 달팽이 숫자
from collections import deque

T = int(input())
for t in range(1,T+1):
    n = int(input())
    if n == 1:
        print(f"#{t}")
        print(1)
        continue
    graph = [[0]*n for _ in range(n)]
    graph[0][0] = 1
    
    dx = [-1,0,1,0] #위0 오른1 아래2 왼3
    dy = [0,1,0,-1]

    q = deque()
    q.append((0,0,1))
    head = 1
    while q:
        x,y,val = q.popleft()
        nx = x + dx[head]
        ny = y + dy[head]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0: #범위 안에 있고 앞으로 갈 수 있는 경우
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny,val + 1))
        elif 0<=nx<n and 0<=ny<n and graph[nx][ny] != 0: #범위 안에 있으나 앞이 막혀서 못가는 경우
            #모든 칸이 다 찼는지?
            zero = False
            for i in graph:
                if 0 in i:
                    zero = True
                    break
            
            #0이 남아있으면 그냥 방향만 바꿈
            if zero:
                head += 1
                if head==4:
                    head = 0
                nx = x + dx[head]
                ny = y + dy[head]
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny,val + 1))
            else:
                break

        elif 0<=nx<n or 0<=ny<n: #x,y 둘중 하나가 범위를 벗어나는 경우
            head += 1
            if head==4:
                head = 0
            nx = x + dx[head]
            ny = y + dy[head]
            if graph[nx][ny] != 0:
                break
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx,ny,val + 1))

    print(f"#{t}")
    for i in range(n):
        for j in range(n):
            print(graph[i][j], end=' ')
        print()