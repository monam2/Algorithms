#백준 15654 n과 m 5
#n개의 자연수 중에서 m개를 고른 수열
def dfs(k):
    if k==m:
        print(' '.join(list(map(str, s))))
        return
    for i in arr:
        if visited[i] == True: #이미 사용했으면
            continue
        s.append(i)
        visited[i] = True
        dfs(k+1)
        s.pop()
        visited[i]=False

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False]*10000
s = []
dfs(0)