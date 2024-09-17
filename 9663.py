# boj 9663 N-Queen

N = int(input())
answer = 0
v0 = [0] * N
v1 = [0] * N
v2 = [0] * (2*N)
v3 = [0] * (2*N)

def dfs(n):
    global answer
    if (n == N):
        answer += 1
        return
    for j in range(N):
        if v0[n] == 1 or v1[j] == 1 or v2[n+j] == 1 or v3[n-j]:
            continue
        v0[n] = 1
        v1[j] = 1
        v2[n+j] = 1
        v3[n-j] = 1
        dfs(n+1)
        v0[n] = 0
        v1[j] = 0
        v2[n+j] = 0
        v3[n-j] = 0

dfs(0)
print(answer)