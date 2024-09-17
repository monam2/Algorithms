#boj 15649 n과 m 1

N, M = map(int, input().split())
v = [0] * (N+1)

def dfs(n, lst):
    global N, M, answer, v
    if n==M:
        print(*lst)
        return
    for j in range(1, N+1):
        if v[j] == 0:
            lst.append(j)
            v[j] = 1
            dfs(n+1, lst)
            v[j] = 0
            lst.pop()

dfs(0, [])