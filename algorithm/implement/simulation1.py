'''
상하좌우

L 왼쪽으로 한칸 이동 
R 오른쪽으로 한칸 이동
U 위로 한칸 이동
D 아래로 한칸 이동
범위를 벗어나는 이동은 무시.

시뮬레이션 문제.
명령에 따른 방향벡터를 미리 정의해놓고, 이동한다.
범위를 벗어나는 명령은 무시한다.

0) 입력 / plan = 입력되는 명령 배열, move = 이동 방향

1) dx와 dy를 이동방향에 따라 정의한다.

2) 명령에 따라 반복문을 실행한다. for i in plan
2-1) 이동 방향 반복문을 실행한다. for j in range(len(move))
2-2) 만약 명령이 move[j]일 경우 nx = x + dx, ny = y + dy를 실행한다.(nx를 바로 x로 하지 않는 이유는 범위를 벗어나는지 체크해야 되기 때문)
2-3) 만약 nx가 범위를 벗어난다면 무시한다.continue
2-4) 벗어나지 않으면 x=nx가 된다. else문 안써도됨.
'''

n = int(input())
plan = list(map(str, input().split(' ')))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
move = ['U', 'R', 'D', 'L']

x = 1
y = 1
nx = 0
ny = 0
for i in plan:
    for j in range(len(move)):
        if i == move[j]:
            nx = x + dx[j]
            ny = y + dy[j]
        if nx > n or nx < 1 or ny > n or ny < 1:
            continue
        x = nx
        y = ny
print(x,y)
