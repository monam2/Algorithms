#백준 14501 퇴사

n = int(input())
t = [0]*n
p = [0]*n

for i in range(n):
    t[i], p[i] = map(int, input().split())

dp = [0]*(n+1)
for k in range(n-1, -1, -1):
    if k+t[k] <= n:
        dp[k] = max(dp[k+1], dp[k+t[k]]+p[k])
    else:
        dp[k] = dp[k+1]

print(dp[0])