#백준 1068 트리
def dfs(rm): #제거할 노드의 모든 자식을 재귀로 제거
    while graph[rm]:
        a = graph[rm].pop()
        dfs(a) #제거 노드 & 자식 -> 전부 []
    graph[rm].append(False)
    #제거 노드와 자손들을 전부 False로 바꿔줌

n = int(input())
arr = list(map(int, input().split()))
rm = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    if arr[i] != -1 and i != rm:
        graph[arr[i]].append(i)

dfs(rm)

leaf = 0
for i in range(n):
    if not graph[i]:
        leaf += 1
print(leaf)