# 백준 17484 진우의 달 여행 (small)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# i: 행, j: 열, k: 이전 방향 저장 - 0, 1, 2 (왼대각, 중앙, 우대각)
dp = [[[float("inf")] * 3 for _ in range(m)] for _ in range(n)]

# 첫번째 행은 초깃값 넣기
for j in range(m):
    dp[0][j][0] = graph[0][j]
    dp[0][j][1] = graph[0][j]
    dp[0][j][2] = graph[0][j]

# 2번째 행부터 dp 시작
for i in range(1, n):
    for j in range(m):
        # 왼대각에서 올때 -> 열이(j) 0보다 클때
        if j > 0:
            dp[i][j][0] = graph[i][j] + min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])

        # 중앙에서 올 때 -> k=0 또는 2
        dp[i][j][1] = graph[i][j] + min(dp[i - 1][j][0], dp[i - 1][j][2])

        # 우대각에서 올 때 -> 열(j)이 m-1보다 작을 때
        if j < m - 1:
            dp[i][j][2] = graph[i][j] + min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])

# 마지막 행에서 최소 연료 계산
min_value = float("inf")

for j in range(m):
    for k in range(3):
        min_value = min(min_value, dp[n - 1][j][k])

print(min_value)
