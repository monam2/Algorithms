#백준 15658 n과 m 9
#이전값과 비교, 방문처리 진행.
#방문처리를 값이 아닌 인덱스로 진행.

def dfs(k):
    prev = 0
    if k==m:
        print(' '.join(list(map(str, s))))
        return
    for i in range(n):
        if visited[i] or prev == arr[i]:
            continue
        s.append(arr[i])
        visited[i] = True
        prev = arr[i]
        dfs(k+1)
        s.pop()
        visited[i] = False
        
n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False]*n
s = []
dfs(0)