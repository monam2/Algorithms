#백준 13913 숨바꾹질 4
#이동하는 방법 : x-1, x+1, x*2. x는 현재 위치
from collections import deque
def path(a,t):
    before = a
    path = []
    path.append(before)
    for i in range(t):
        before = gill[before]
        path.append(before)
    return path

def bfs(x, k):
    q = deque()
    q.append((x, 0))
    visited[x] = True
    gill[x] = 0
    
    while q:
        x, t = q.popleft() #현재 위치, 걸린 시간
        if x == k:
            print(t)
            print(*path(x,t)[::-1])
            return
            
        vec = [x-1, x+1, x*2]
        for i in range(3):
            nx = vec[i]
            if 0<= nx <= 100000:
                if visited[nx]==False:
                    visited[nx] = True
                    q.append((nx,t+1))
                    gill[nx] = x

n, k = map(int, input().split())

visited = [False]*100001
gill = [0]*100001
result = bfs(n, k)