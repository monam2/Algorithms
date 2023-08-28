#프로그래머스 Lv3 네트워크
from collections import deque
def bfs(graph, visited, v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        v = q.popleft()
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == False:
                q.append(graph[v][i])
                visited[graph[v][i]] = True

def solution(n, computers):
    answer = 0
    visited = [False]*n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i!=j:
                graph[i].append(j)
    
    for i in range(len(graph)):
        if visited[i] == False:
            bfs(graph, visited, i)
            answer+= 1
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(4,[[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]))
print(solution(7,[[1,0,0,0,0,0,1], [0,1,1,0,1,0,0], [0,1,1,1,0,0,0], [0,0,1,1,0,0,0],[0,1,0,0,1,1,0],[0,0,0,0,1,1,1],[1,0,0,0,0,1,1]]))
