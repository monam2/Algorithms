#프로그래머스 1844
from collections import deque

def BFS(x,y,maps):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    q=deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()
        if x==len(maps)-1 and y==len(maps[0])-1:
            return maps[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < len(maps) and ny < len(maps[0]):
                if visited[nx][ny] == False and maps[nx][ny] !=0:
                    q.append((nx,ny))
                    visited[nx][ny]=True
                    maps[nx][ny] = maps[x][y]+1
    return -1

def solution(maps):
    return BFS(0,0,maps)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
