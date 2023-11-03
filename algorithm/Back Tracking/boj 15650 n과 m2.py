#백준 15650 n과m 2
#1부터 n까지 자연수 중 중복없이 m개를 고른 수열
#고른 수열은 오름차순이어야 한다.

def dfs(k): #k는 자릿수
    if k == m: #자릿수가 m과 같으면
        print(' '.join(list(map(str, arr))))
        return
    for i in range(1,n+1):
        if visited[i]: #이미 쓴 수는 패스
            continue
        if arr and i < arr[-1]:
            continue
        arr.append(i)
        visited[i]=True
        dfs(k+1)
        arr.pop()
        visited[i]=False

n,m = map(int, input().split())
arr = [] #수열을 담을 배열
visited = [False] * (n+1)
dfs(0)