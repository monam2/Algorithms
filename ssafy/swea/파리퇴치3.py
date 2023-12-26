#swea 파리퇴치3

T = int(input())
for t in range(1,T+1):
    n,m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    mx = 0
    for i in range(n):
        for j in range(n):
            # x방향 d벡터
            xdx = [-1,-1,1,1]
            xdy = [-1,1,1,-1]
            # plus방향 d벡터
            pdx = [-1,0,1,0]
            pdy = [0,1,0,-1]
            x_total,p_total = graph[i][j], graph[i][j]

            for times in range(1,m):
                for k in range(4):
                    #x방향
                    if 0<= i+xdx[k]*times <n and 0<= j+xdy[k]*times <n:
                        x_total += graph[i+xdx[k]*times][j+xdy[k]*times]
                    #plus 방향
                    if 0<= i+pdx[k]*times <n and 0<= j+pdy[k]*times <n:
                        p_total += graph[i+pdx[k]*times][j+pdy[k]*times]
            mx = max(mx, x_total, p_total)
    print(f"#{t} {mx}")