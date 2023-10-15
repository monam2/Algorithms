# SWEA 1215 회문1
def check(arr: list):
    if arr == arr[::-1]:
        return True
    return False


for t in range(10):
    answer = 0
    n = int(input())
    maps = [list(input()) for _ in range(8)]

    # 행 체크
    for i in range(8):
        for j in range(8-n+1):
            row = []  # 행
            for k in range(n):
                row.append(maps[i][j+k])
            if check(row):
                answer += 1
    # 열 체크
    for i in range(8-n+1):
        for j in range(8):
            col = []  # 열
            for k in range(n):
                col.append(maps[i+k][j])
            if check(col):
                answer += 1

    print(f"#{t+1}", answer)
