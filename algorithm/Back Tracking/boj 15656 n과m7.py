#백준 15656 n과 m 7
#n개의 자연수 중에서 m개를 고른 수열
#같은 수를 여러번 골라도 됨 -> 가지치기 제외
def dfs(k):
    if k==m:
        print(' '.join(list(map(str, s))))
        return
    for i in arr:
        s.append(i)
        dfs(k+1)
        s.pop()

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
dfs(0)