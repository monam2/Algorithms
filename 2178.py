from collections import deque
# 2178 미로 탐색

# 입력
# N * M 의 배열
#
# 출력
# 지나야 하는 최소의 칸 수
#
# 1은 갈 수 있고, 0은 벽임
# (1,1)에서 출발해서 (N,M)으로 이동하려고 함
# 이때 최소 칸의 수

# 이동은 4방위만 가능
# 첫 시작 칸부터 칸수 누적(1부터 시작)

N, M = map(int, input().split())
graph = [list(map(int, input())) for _ in range(N)]

# 최단거리 탐색이니 BFS를 이용

def bfs(graph, N, M):
  q = deque()
  visited = [[False] * M for _ in range(N)]

  q.append((0,0,1))
  visited[0][0] = True

  totalD = 0

  while q:
    x, y, dist = q.popleft()
    
    if x==N-1 and y==M-1:
      totalD = dist
      break 

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0<=nx<N and 0<=ny<M and visited[nx][ny] == False and graph[nx][ny] == 1:
        q.append((nx,ny,dist+1))
        visited[nx][ny] = True
  
  return totalD

result = bfs(graph, N, M)
print(result)