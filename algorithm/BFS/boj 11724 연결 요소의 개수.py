#11724 연결 요소의 개수

from collections import deque
def bfs(v,graph,visited):
    q=deque()
    q.append(v)
    visited[v]=True

    while q:
        v = q.popleft()
        for i in range(len(graph[v])):
            if visited[graph[v][i]]==False:
                q.append(graph[v][i])
                visited[graph[v][i]]=True

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
for i in range(1,n+1):
    if visited[i] == False:
        bfs(i,graph,visited)
        count += 1
print(count)
