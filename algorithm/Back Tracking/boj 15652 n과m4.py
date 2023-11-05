#백준 15652 N과 M 4
#1부터 N까지 M개를 고른 수열
#같은 수를 여러번 골라도 됨
#고른 수열은 비내림차순이어야 한다. -> 가지치기
def dfs(k):
    if k==m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1,n+1):
        if arr and i < arr[-1]:
            continue
        arr.append(i)
        dfs(k+1)
        arr.pop()

n,m = map(int, input().split())
arr = []
dfs(0)