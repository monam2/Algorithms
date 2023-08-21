#1325 효율적인 해킹
import sys
n,m = map(int,sys.stdin.readline().split())
graph = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[b-1].append(a-1)

count_arr=[0 for i in range(n)]
stack = []

for i in range(n):
    visited = [0]*n
    visited[i] = 1
    stack.append(i)
    while stack:
        count_arr[i] += 1
        v = stack.pop()
        
        for j in range(len(graph[v])):
                if visited[graph[v][j]] == 1:
                     continue
                stack.append(graph[v][j])
                visited[graph[v][j]] = 1

maxV = max(count_arr)
result = []
for i in range(len(count_arr)):
     if count_arr[i] == maxV:
        print(i+1, end=' ')
