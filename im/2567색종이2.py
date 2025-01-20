# 2567 색종이2


def calculate(arr):
    length = 0
    for x in range(len(arr)):
        before = 0
        for y in range(len(arr[x])):
            if not arr[x][y] == before:
                length += 1
            before = arr[x][y]

    return length


N = int(input())
rectangles = [list(map(int, input().split())) for _ in range(N)]
board = [[0] * 101 for _ in range(101)]

for rec in rectangles:
    for r in range(rec[0], rec[0] + 10):
        for c in range(rec[1], rec[1] + 10):
            board[r][c] = 1

board_t = list(zip(*board))
ans = calculate(board) + calculate(board_t)

print(ans)
