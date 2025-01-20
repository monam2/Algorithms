# 2563 색종이

N = int(input())
rectangles = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 101 for _ in range(101)]

for rec in rectangles:

    for r in range(rec[0], rec[0] + 10):
        for c in range(rec[1], rec[1] + 10):
            board[r][c] += 1

ans = 0
for x in range(len(board)):
    for y in range((len(board[x]))):
        if not board[x][y] == 0:
            ans += 1

print(ans)
