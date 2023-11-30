#백준 2630 색종이 색칠하기
def f(x,y,n):
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[x][y] != graph[i][j]:
                f(x,y,n//2)
                f(x+n//2,y,n//2)
                f(x,y+n//2,n//2)
                f(x+n//2,y+n//2,n//2)
                return
    if graph[x][y] == 0:
        answer.append(0)
    else:
        answer.append(1)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = []
f(0,0,n)

print(answer.count(0))
print(answer.count(1))