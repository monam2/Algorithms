#swea 1824 혁진이의 프로그램 검증
from collections import deque

T = int(input())
for t in range(1,1+T):
    n ,m = map(int, input().split())
    graph = [list(input()) for _ in range(n)]
    
    answer = 'NO'
    memory = 0
    head = 0
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dh = ['>','v','<','^'] #우:0 / 하:1 / 좌:2 / 상:3
    x,y = 0,0
    q = deque()
    q.append((x,y,head,memory))
    visited = [[[0]]*m for _ in range(n)]

    visited[x][y].append((head, memory))
    while q:
        #명령 수행 부분
        x,y,head,memory = q.popleft()
        command = graph[x][y]
        if command == '@':
            answer = 'Yes'
            break
        if command != '?': #물음표가 아닐 때
            if command == '.':
                pass
            elif command in dh: #방향 바꾸기(head 변경)
                head = dh.index(command)
            elif command in ['_', '|']:
                if command == '_' and memory == 0:
                    head = 0
                elif command == '_' and memory != 0:
                    head = 2
                elif command == '|' and memory == 0:
                    head = 1
                elif command == '|' and memory != 0:
                    head = 3
            elif command in ['0','1','2','3','4','5','6','7','8','9']:
                memory = int(command)
            elif command == '+':
                if memory == 15:
                    memory = 0
                else:
                    memory += 1
            elif command == '-':
                if memory == 0:
                    memory = 15
                else:
                    memory -= 1

            nx = x + dx[head] #이동 부분
            ny = y + dy[head]
            if 0<= nx < n and 0<= ny<m:
                pass
            else: #x,y가 둘다 범위 밖인 경우는 없음(대각이동은 x)
                if 0<=nx<n: #y가 범위 밖인 경우
                    if ny<0: ny=m-1
                    elif ny>=m: ny=0
                elif 0<=ny<n: #x가 범위 밖인 경우
                    if nx<0: nx=n-1
                    elif nx>=n: nx=0
            q.append((nx,ny,head,memory))
            visited[nx][ny].append((head,memory))

        else: #물음표 일 때
            for i in range(4):
                if i == head:
                    continue
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m: #범위 체크 + 방문 여부 체크
                    if (head, memory) not in visited[nx][ny]:
                        q.append((nx,ny,i,memory))
                        visited[nx][ny].append(head,memory)
                elif nx<0 or ny<0 or nx>=n or ny>=m:
                    if 0<=nx<n: #y가 범위 밖인 경우
                        if ny<0: ny=m-1
                        elif ny>=m: ny=0
                    elif 0<=ny<n: #x가 범위 밖인 경우
                        if nx<0: nx=n-1
                        elif nx>=n: nx=0
                    if (head, memory) not in visited[nx][ny]:
                        q.append((nx,ny,i,memory))
                        visited[nx][ny].append(head,memory)

    print(f"#{t} {answer}")
