#1260 DFS와 BFS

from collections import deque
def DFS(graph, v):
    for i in graph:
        i.sort(reverse=True)
    stack = []
    result = []
    visited = [False] * (n+1)
    stack.append(v)
    while stack:
        v = stack.pop()
        if visited[v] == False:
            visited[v] = True
            result.append(v)
        else:
            continue
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == False:
                stack.append(graph[v][i])

    return result

def BFS(graph, v):
    for i in graph:
        i.sort()
    q=deque()
    result = []
    visited = [False] * (n+1)
    q.append(v)
    while q:
        v = q.popleft()
        if visited[v] == False:
            visited[v]=True
            result.append(v)
        else:
            continue
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == False:
                q.append(graph[v][i])

    return result

n,m,k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs_result = DFS(graph, k)
bfs_result = BFS(graph, k)
for j in dfs_result:
    print(j, end=' ')
print()
for j in bfs_result:
    print(j, end=' ')
