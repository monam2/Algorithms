#백준 2178 미로 탐색 2nd
from collections import deque

n,m = map(int, input().split())
maps = [list(input()) for _ in range(n)] #문자열 '0' 과 '1' 로 2차원배열 생성

visited = [[False]*m for _ in range(m)]
q = deque()
q.append((0,0,0)) #좌표와 이동횟수를 함께 기록
visited[0][0] = True #방문처리
answer = 0

while q:
    x,y,cnt = q.popleft()
    if x==n-1 and y == m-1: #목표지점 : (n-1,m-1)
        answer = cnt+1
        break

    dx = [-1,0,1,0] #방향벡터 정의
    dy = [0,1,0,-1]
    for i in range(4): #x,y점에서 북,동,남,서 방향의 +1칸을 살펴봄
        nx = x + dx[i]
        ny = y + dy[i]

        #다음 칸이 maps의 범위 내에 있고, 1(이동가능칸)일 경우
        if 0<= nx < n and 0<= ny < m and maps[nx][ny]=='1':
            if visited[nx][ny] == False: #아직 방문하지 않은 칸이라면
                visited[nx][ny] = True #
                q.append((nx,ny,cnt+1))
                
#큐가 비거나(=더이상 갈 곳이 없음), 목표지점에 다다랐다면 종료
print(answer)
