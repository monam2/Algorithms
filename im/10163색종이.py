# 10163 색종이

N = int(input())
board = [[0] * 1001 for _ in range(1001)]

for n in range(1, N + 1):
    a, b, c, d = map(int, input().split())
    for i in range(a, a + c):
        for j in range(b, b + d):
            board[i][j] = n


# 빈도수 배열
cnts = [0] * (n + 1)
for lst in board:
    for ele in lst:
        cnts[ele] += 1
print(*cnts[1:], sep="\n")
