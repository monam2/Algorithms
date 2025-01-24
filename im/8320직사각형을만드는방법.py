# 8320 직사각형을 만드는 방법

N = int(input())

ans = 0

for i in range(1, N + 1):
    for j in range(i, N + 1):
        if i * j <= N:
            ans += 1
print(ans)

# 세로 1칸 ㅁ ㅁㅁ ㅁㅁㅁ ㅁㅁㅁㅁ ㅁㅁㅁㅁㅁ ㅁㅁㅁㅁㅁㅁ 6 (N)
# 세로 2칸 2 (N/2)
# ㅁㅁ ㅁㅁㅁ
# ㅁㅁ ㅁㅁㅁ
# 세로 3칸 0 (0)
