# 백준 11725 트리의 부모찾기
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    visited = [[] for _ in range(n+1)]
    q.append(1)
    visited[1] = -1

    while q:
        v = q.popleft()
        for nd in graph[v]:
            if not visited[nd] and graph[nd]:
                q.append(nd)
                visited[nd] = v
    return visited
    

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs()
for i in range(2,n+1):
    print(result[i])