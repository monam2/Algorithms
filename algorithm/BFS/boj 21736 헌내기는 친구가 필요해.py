#백준 21736 헌내기는 친구가 필요해
# o : 빈 공간
# x : 벽
# I : 도연
# P : 사람. 몇명의 사람을 만날 수 있는지 출력.
from collections import deque
n,m = map(int, input().split())
graph = []
for i in range(n):
    ipt = list(input())
    graph.append(ipt)
    for j in range(len(ipt)):
        if ipt[j] == 'I':
            doyean = [i,j] #도연이 좌표

visited = [[False]*m for _ in range(n)]
count = 0 #사람을 만난 횟수
q=deque()
x, y = doyean
visited[x][y] = True
q.append(doyean)

while q:
    x,y = q.popleft()
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0<= ny < m:
            if visited[nx][ny] == False and graph[nx][ny]!='X':
                visited[nx][ny] = True
                q.append((nx,ny))
                if graph[nx][ny]=='P': #사람 만나면 +1
                    count += 1

answer = 'TT' if count==0 else count
print(answer)
