n, m = map(int, input().split())
x,y,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,0,1,0] #북 동 남 서
dy = [0,1,0,-1]
answer = 0

while True:
    if arr[x][y] == 0:
        answer += 1
        arr[x][y] = 2
    
    # 현재 위치에서 청소할 수 있는 칸의 유무를 확인
    cleaned = False
    for _ in range(4):
        # 현재 방향에서 왼쪽으로 회전
        d = (d + 3) % 4
        nx, ny = x + dx[d], y + dy[d]
        if arr[nx][ny] == 0:  # 청소할 수 있는 칸이 존재
            cleaned = True
            x, y = nx, ny
            break

    if cleaned:
        continue

    # 네 방향 모두 청소할 수 없는 경우
    # 후진 가능한지 확인
    bx, by = x - dx[d], y - dy[d]
    if arr[bx][by] != 1:  # 후진 가능
        x, y = bx, by
    else:
        break

print(answer)