#컴퓨터 개수

def solution(n, edges):
    answer = 0
    graph = [[] for _ in range(n)]
    
    for i in edges:
        [a,b] = i
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    stack = []
    visited = [0]*n
    stack.append(0)
    visited[0] = 1
    count = 1
    while stack:
        v = stack.pop()
        for k in graph[v]:
            if visited[k]==0:
                stack.append(k)
                visited[k] = 1
                count += 1
    return n - count
                    

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))

