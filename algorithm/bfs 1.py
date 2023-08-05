from collections import deque
def bfs(x,y):
    q = deque()
    q.append((x,y))
    arr[x][y]=0
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if nx<0 or ny<0 or nx>n-1 or ny>m-1 or arr[nx][ny] == 0:
                continue
            else:
                q.append((nx,ny))
                arr[nx][ny] = 0
                count += 1
    return count

n,m = map(int, input().split())
arr = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for _ in range(n):
    arr.append(list(map(int,input().split())))


All_count = 0
maxValue = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            maxValue = max(maxValue, bfs(i,j))
            All_count += 1
print(All_count, maxValue)
