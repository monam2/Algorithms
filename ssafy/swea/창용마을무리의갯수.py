#SWEA 창용마을 무리의 개수
from collections import deque

def bfs(i,graph, visited):
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        v = q.popleft()
        for j in graph[v]:
            if graph[j] and visited[j] == False:
                visited[j] = True
                q.append(j)

T = int(input())
for t in range(1,1+T):
    n, m = map(int, input().split()) #n:노드 / m:간선
    graph = [[] for _ in range(n+1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b) #그래프 생성
        graph[b].append(a)

    count = 0
    visited = [False]*(n+1)
    for i in range(1,n+1):
        if visited[i] == False:
            bfs(i,graph, visited)
            count += 1
    print(f"#{t} {count}")