#1260 DFS와 BFS

from collections import deque
def DFS(graph, v):
    stack = []
    visited = [False] * (n+1)
    stack.append(v)
    visited[v] = True

    while stack:
        v = stack.pop()
        


def BFS(graph, v):
    q=deque()
n,m,k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
DFS(graph, k)
BFS(graph, k)
