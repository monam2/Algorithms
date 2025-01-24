# 2605 줄 세우기

N = int(input())
order = list(map(int, input().split()))
ans = [0] * N

for i in range(N):
    pos = i - order[i]  # 들어갈 위치

    for j in range(i, pos, -1):
        ans[j] = ans[j - 1]

    ans[pos] = i + 1

print(" ".join(map(str, ans)))
