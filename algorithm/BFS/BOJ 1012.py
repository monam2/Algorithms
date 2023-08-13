#1012 유기농 배추

from collections import deque

def BFS(x,y):
    arr[x][y] = 0
    q = deque()
    q.append((x,y))
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    while q:
        p = len(q)
        for o in range(p):
            x,y = q.popleft()
            for d in range(4):
                nx=x+dx[d]
                ny=y+dy[d]
                if nx>=0 and ny>=0 and nx<n and ny<m and arr[nx][ny]==1:
                    q.append((nx,ny))
                    arr[nx][ny] = 0


t = int(input())
for _ in range(t):
    count = 0
    m,n,k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]

    for _ in range(k):
        l,r = map(int,input().split())
        arr[r][l] = 1

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                BFS(i,j)
                count += 1
    print(count)
