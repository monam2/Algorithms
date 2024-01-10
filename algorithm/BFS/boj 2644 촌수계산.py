#백준 2644번 촌수계산
from collections import deque

def bfs(a,b,visited):
    q = deque()
    q.append(a)

    while q:
        v = q.popleft()
        for nd in graph[v]:
            if not visited[nd] and graph[nd]:
                visited[nd] = visited[v] + 1
                q.append(nd)

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a,b,visited)
if visited[b]:
    print(visited[b])
else: print(-1)