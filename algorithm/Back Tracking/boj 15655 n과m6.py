#백준 15655 n과 m 6
#n개의 자연수 중에서 m개를 고른 수열
#고른 수열은 오름차순이어야 한다. -> 가지치기
def dfs(k):
    if k==m:
        print(' '.join(list(map(str, s))))
        return
    for i in arr:
        if visited[i]:
            continue
        if s and i<=s[-1]:
            continue
        s.append(i)
        visited[i]=True
        dfs(k+1)
        s.pop()
        visited[i]=False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
visited = [False]*10000
dfs(0)