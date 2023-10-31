#swea 1219 길찾기
from collections import deque

for t in range(10):
    n, k = map(int, input().split())
    answer = 0
    graph = [[] for _ in range(100)]
    arr = list(map(int, input().split()))
    q = deque(arr)
    while len(q)>0:
        a = q.popleft()
        b = q.popleft()
        graph[a].append(b)

    que = deque()
    visited = [False]*100
    que.append(0)
    visited[0] = True
    while que:
        v = que.popleft()
        if v == 99:
            answer = 1
            break
        for i in range(len(graph[v])):
            if visited[graph[v][i]] == False:
                que.append(graph[v][i])
                visited[graph[v][i]] = True

    print(f"#{t+1}", answer)