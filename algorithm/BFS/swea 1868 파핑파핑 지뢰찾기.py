# swea 1868 파핑파핑 지뢰찾기
from collections import deque
#최소 클릭 수를 구하려면?
#1) 시작점 찾기(클릭할 점) : 주변 8개에 지뢰가 없는 지점
#2) 시작점 주변 8개는 같이 클릭됨.

def search(x,y):
    #0인 점을 기준으로 탐색 시작
    # - *가 아닌 점 -> *로 바꿈
    # - 0인 점 -> *로 바꾸고, 큐에 넣어서 다음칸 탐색
    q = deque()
    q.append((x,y))
    graph[x][y] = '*'
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = '*'
                    q.append((nx,ny))
                elif graph[nx][ny] != '*':
                    graph[nx][ny] = '*'
                


dx = [-1,0,1,0,-1,1,1,-1]
dy = [0,1,0,-1,1,1,-1,-1]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    graph = []
    for i in range(n):
        arr = list(input())
        graph.append(arr)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '.':
                count = 0
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0<=ni<n and 0<=nj<n and graph[ni][nj] == '*':
                        count += 1
                graph[i][j] = count

#미리 숫자를 다 까놓고 시작하기
# [0, 2, '*', 2, 0]
# [1, 3, '*', 3, 1]
# [2, '*', 3, 2, '*']
# [3, '*', 3, 1, 1]
# [2, '*', 2, 0, 0]



    answer = 0
    for i in range(n): 
        for j in range(n):
            #클릭 시작점 -> * / 주변 8개 전부 *로 바꿈
            #주변에 0이 있으면 넘어가서 탐색
            if graph[i][j] == 0:
                answer += 1
                search(i,j)

# ['*', '*', '*', '*', '*']
# ['*', '*', '*', '*', '*']
# [2, '*', 3, 2, '*']
# [3, '*', '*', '*', '*']
# [2, '*', '*', '*', '*']

    for i in range(n):
        for j in range(n):
            if graph[i][j]!='*':
                answer += 1

    print(f"#{t}", answer)