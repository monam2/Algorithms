#swea 4615 재미있는 오셀로 게임

T = int(input())
for t in range(1,T+1):
    n, m = map(int, input().split())
    graph = [[0]*n for _ in range(n)]
    graph[n//2-1][n//2-1] = 2
    graph[n//2][n//2-1] = 1
    graph[n//2-1][n//2] = 1
    graph[n//2][n//2] = 2
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    for i in range(m):
        y, x, dol = map(int, input().split())
        x,y = x-1, y-1
        if dol == 1: #흑돌 B
            graph[x][y] = 1 #흑돌을 놓고, 탐색 시작
            for k in range(8): #8방향
                candidate = []
                for d in range(1,n): #뻗어나가기
                    nx = x + dx[k]*d
                    ny = y + dy[k]*d
                    if not (0<=nx<n and 0<=ny<n):
                        break
                    if graph[nx][ny] == 0:
                        break
                    elif graph[nx][ny] == dol: #같은걸 만나면 후보군을 다 나랑 같게 바꾸고 종료
                        while candidate:
                            tx, ty = candidate.pop()
                            graph[tx][ty] = dol
                        break
                    else: #다른걸 만나면 후보군에 넣고 다음 칸으로 뻗어 나가야 함
                        candidate.append((nx,ny))
                    #다른걸 만나다가 0을 만나면 그냥 종료

        else: #백돌 W
            graph[x][y] = 2 #백돌을 놓고, 탐색 시작
            for k in range(8): #8방향
                candidate = []
                for d in range(1,n): #뻗어나가기
                    nx = x + dx[k]*d
                    ny = y + dy[k]*d
                    if not (0<=nx<n and 0<=ny<n):
                        break
                    if graph[nx][ny] == 0:
                        break
                    elif graph[nx][ny] == dol: #같은걸 만나면 후보군을 다 나랑 같게 바꾸고 종료
                        while candidate:
                            tx, ty = candidate.pop()
                            graph[tx][ty] = dol
                        break
                    else: #다른걸 만나면 후보군에 넣고 다음 칸으로 뻗어 나가야 함
                        candidate.append((nx,ny))
                    #다른걸 만나다가 0을 만나면 그냥 종료

    black, white = 0,0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                black += 1
            elif graph[i][j] == 2:
                white += 1

    print(f"#{t} {black} {white}")