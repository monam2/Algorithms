#SWEA 최대수 구하기

T = int(input())
for t in range(1,T+1):
    print(f"#{t} {max(list(map(int, input().split())))}")