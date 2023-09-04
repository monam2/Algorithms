#5567 결혼식
from collections import deque

def BFS(v,graph,visited):
    q = deque()
    visited[v]=True
    q.append(v)
    count = 0
    result = 0

    while q:
        count += 1
        for _ in range(len(q)):
            v = q.popleft()
            for i in range(len(graph[v])):
                if visited[graph[v][i]]==False:
                    visited[graph[v][i]] = True
                    result += 1
                    q.append(graph[v][i])
        if count == 2:
            break
    return result

n=int(input())
m=int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited =[False]*(n+1)
print(BFS(1,graph,visited))
