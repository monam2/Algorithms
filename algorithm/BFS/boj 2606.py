#2606 바이러스
from collections import deque
def BFS(v,graph):
    global count
    q = deque()
    q.append(v)
    visited = [False]*len(graph)
    visited[v]=True

    while q:
        v = q.popleft()
        count += 1
        for i in range(len(graph[v])):
            if visited[graph[v][i]]==False:
                q.append(graph[v][i])
                visited[graph[v][i]] = True

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
count = 0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
BFS(1,graph)
print(count-1)
