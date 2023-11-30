#백준 2624 동전 바꿔주기

coins = [(0, 0)] * 101
d = [[-1] * 101 for _ in range(10001)]

def dp(sum, idx):
    if sum == 0:
        return 1
    if idx > k:
        return 0
    if d[sum][idx] != -1:
        return d[sum][idx]

    result = 0
    for i in range(coins[idx][1] + 1):
        if sum - (coins[idx][0] * i) >= 0:
            result += dp(sum - (coins[idx][0] * i), idx + 1)

    d[sum][idx] = result
    return result

T = int(input())
k = int(input())

for i in range(1, 10001):
    for j in range(1, 101):
        d[i][j] = -1

for i in range(1, k + 1):
    v1, v2 = map(int, input().split())
    coins[i] = (v1, v2)

print(dp(T, 1))