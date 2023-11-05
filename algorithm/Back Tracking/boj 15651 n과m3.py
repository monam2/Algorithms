#백준 15651 n과m 3
#1부터 n까지의 자연수 중 M개를 고른 수열
#가지치기 : 같은 수를 여러번 골라도 된다. -> 수 사용체크 x?
def dfs(k):
    if k==m: #노드 레벨이 자릿수와 같으면
        print(' '.join(list(map(str, arr))))
        return
    for i in range(1,n+1):
        arr.append(i)
        dfs(k+1)
        arr.pop()

n,m = map(int, input().split())
arr = []
dfs(0)