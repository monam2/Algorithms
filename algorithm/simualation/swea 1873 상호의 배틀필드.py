#swea 1873 상호의 배틀필드
from collections import deque

T = int(input())
for t in range(1,T+1):
    n,m = map(int, input().split())
    tank = deque()
    graph = []
    for i in range(n):
        arr = list(map(str, input()))
        graph.append(arr)
        for j in range(m):
            if arr[j] == '^':
                tank.append((i,j,0))
                graph[i][j] = '.'
                break
            elif arr[j] == '>':
                tank.append((i,j,1))
                graph[i][j] = '.'
                break
            elif arr[j] == 'v':
                tank.append((i,j,2))
                graph[i][j] = '.'
                break
            elif arr[j] == '<':
                tank.append((i,j,3))
                graph[i][j] = '.'
                break
            
    k = int(input())
    command = list(input())
    
    #0:위 / 1:오른쪽 / 2:아래 / 3:왼쪽
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    dh = ['^','>','v','<']
    h_arr = ['U','R','D','L']
    for com in command:
        x,y,head = tank.popleft()
        if com != 'S':
            head = h_arr.index(com) #U:0, R:1, D:2, L:3
            nx = x + dx[head]
            ny = y + dy[head]
            if 0<= nx < n and 0 <= ny < m and graph[nx][ny] == '.': #빈 칸이면 탱크의 위치 이동
                tank.append((nx,ny,head))
            else:
                tank.append((x,y,head))

        else: #포탄 발사
            px = x
            py = y
            while 0<= px < n and 0<= py < m:
                if graph[px][py] == '#':
                    break
                if graph[px][py] == '*':
                    graph[px][py] = '.'
                    break
                px += dx[head]
                py += dy[head]
            tank.append((x,y,head))
    
    x,y,head = tank.popleft()
    graph[x][y] = dh[head]

    print('#%d' % t, sep='', end=' ')
    for i in graph:
        print(*i, sep='')