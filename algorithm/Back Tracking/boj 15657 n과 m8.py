#백준 15657 n과 m 8
#n개의 자연수 중 m개를 고른 수열
#같은 수 여러번 골라도 됨
#비내림차순
def dfs(k):
    if k==m:
        print(' '.join(list(map(str, s))))
        return
    for i in arr:
        if s and i < s[-1]:
            continue
        s.append(i)
        dfs(k+1)
        s.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = []
dfs(0)