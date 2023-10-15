#백준 14620 꽃길

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

result = float('inf') #초기 비용을 최대로 설정

def solution(lst):
    dx = [0,-1,0,1,0] #5칸의 방향벡터 정의
    dy = [0, 0,1,0,-1]
    flower = [] #꽃의 위치 배열
    price = 0 #최소 비용

    for locate in lst:
        x = locate//n #36칸을 n으로 나눠서 x좌표
        y = locate%n #36칸을 n으로 나눈 나머지로 y좌표
        if x==0 or x==n-1 or y==0 or y==n-1:
            return float('inf') #범위를 벗어나면 이전값 리턴
        for d in range(5):
            flower.append((x+dx[d], y+dy[d]))
            price += maps[x+dx[d]][y+dy[d]]
    
    if len(set(flower)) != 15: #3개의 꽃이 있지 않거나, 겹치는 꽃이 있으면
        return float('inf') #최솟값 아님
    return price #꽃이 3개고 안겹치면 구한 최소비용 리턴

#꽃 3개 위치를 전부 탐색. 좌표가 아닌, 1차원으로(0~36)
for i in range(n*n):
    for j in range(i+1, n*n):
        for k in range(j+1, n*n):
            result = min(result, solution([i,j,k]))
print(result)
